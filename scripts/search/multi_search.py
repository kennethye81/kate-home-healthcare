#!/usr/bin/env python3
"""Kate 多引擎并行搜索 v2.3 — 四档模式 + 中文穷尽搜索

用法:
  python3 kate_quant/multi_search.py "搜索关键词"
  python3 kate_quant/multi_search.py "关键词" --engines tavily,brave,bocha
  python3 kate_quant/multi_search.py "关键词" --zh        ← 中文政策搜索（新增）
  python3 kate_quant/multi_search.py --status

三档模式:
  默认（平衡）: tavily+brave+firecrawl+bocha       ~3-10秒  通用场景
  --zh         : bocha + baidu + 搜狗微信         ~5-12秒   中文政策/长护险/公众号
  --engines=...: 可加 qichacha           ~8-30秒  深挖

⚠️ 关键已知问题（2026.07.05）:
  Tavily/Brave 两引擎将中文"长期护理保险/长护险"误解析为英文"engine/fast"，
  对中文政策查询返回大量垃圾结果。
  中文/政策类搜索请使用 `--zh` 模式（Bocha-only，不受此问题影响）。
"""

import json, os, re, sys, time, urllib.request, urllib.parse, subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
try:
    import requests
    from bs4 import BeautifulSoup
    _HAS_SCRAPER = True
except ImportError:
    _HAS_SCRAPER = False

WORKSPACE = Path(__file__).resolve().parent.parent

# ── API Keys ──
ENV_PATH = Path.home() / ".hermes/profiles/kate-strategist/.env"
def _load_key(var):
    if ENV_PATH.exists():
        with open(ENV_PATH) as f:
            for line in f:
                if line.strip().startswith(var):
                    val = line.strip().split('=', 1)[1].strip().strip('"').strip("'")
                    if val and val != '***' and not val.startswith('#'):
                        return val
    return os.environ.get(var, "")

TAVILY_KEYS = [k for k in [_load_key('TAVILY_API_KEY'), _load_key('TAVILY_API_KEY_2'), _load_key('TAVILY_API_KEY_3')] if k]
BRAVE_KEY = _load_key('BRAVE_API_KEY')
SERPER_KEY = _load_key('SERPER_API_KEY')
BOCHA_KEY = _load_key('BOCHA_API_KEY')
FIRECRAWL_KEYS = [k for k in [_load_key('FIRECRAWL_API_KEY'), _load_key('FIRECRAWL_KEY_2'), _load_key('FIRECRAWL_KEY_3')] if k]
BOCHA_SCRIPT = Path.home() / ".hermes/profiles/kate-strategist/skills/bocha-search/scripts/search.sh"


def _tavily_one(key, key_num, query, limit):
    try:
        data = json.dumps({"api_key": key, "query": query, "search_depth": "advanced", "max_results": limit}).encode()
        req = urllib.request.Request("https://api.tavily.com/search", data=data, headers={"Content-Type": "application/json"}, method="POST")
        resp = json.loads(urllib.request.urlopen(req, timeout=15).read())
        return [{"source": f"tavily", "title": r.get("title",""), "url": r.get("url",""), "snippet": r.get("content","")[:300]} for r in resp.get("results",[])]
    except urllib.error.HTTPError as e:
        if e.code == 432:
            raise  # rate limit — caller handles fallback
        return [{"source": "tavily", "error": f"HTTP {e.code}"}]
    except Exception as e:
        return [{"source": "tavily", "error": str(e)}]

def search_tavily(query, limit=5):
    for i, key in enumerate(TAVILY_KEYS):
        try:
            result = _tavily_one(key, i+1, query, limit)
            if result and not result[0].get("error") and result[0].get("url"):
                return result
        except urllib.error.HTTPError:
            continue
    return [{"source": "tavily", "error": "All keys exhausted"}] if TAVILY_KEYS else [{"source": "tavily", "error": "No API key"}]

def search_brave(query, limit=5):
    if not BRAVE_KEY:
        return [{"source": "brave", "error": "No API key"}]
    try:
        req = urllib.request.Request(
            f"https://api.search.brave.com/res/v1/web/search?q={urllib.parse.quote(query)}&count={limit}",
            headers={"Accept": "application/json", "X-Subscription-Token": BRAVE_KEY}
        )
        resp = json.loads(urllib.request.urlopen(req, timeout=15).read())
        return [{"source": "brave", "title": r.get("title",""), "url": r.get("url",""), "snippet": r.get("description","")[:300]} for r in resp.get("web",{}).get("results",[])]
    except Exception as e:
        return [{"source": "brave", "error": str(e)}]

def search_serper(query, limit=5):
    if not SERPER_KEY:
        return [{"source": "serper", "error": "No API key"}]
    try:
        data = json.dumps({"q": query, "num": limit}).encode()
        req = urllib.request.Request("https://google.serper.dev/search", data=data, headers={"X-API-KEY": SERPER_KEY, "Content-Type": "application/json"}, method="POST")
        resp = json.loads(urllib.request.urlopen(req, timeout=15).read())
        return [{"source": "serper", "title": r.get("title",""), "url": r.get("link",""), "snippet": r.get("snippet","")[:300]} for r in resp.get("organic",[])]
    except Exception as e:
        return [{"source": "serper", "error": str(e)}]

def search_bocha(query, limit=5):
    if not BOCHA_SCRIPT.exists() or not BOCHA_KEY:
        return [{"source": "bocha", "error": "Script or API key not found"}]
    try:
        result = subprocess.run(["bash", str(BOCHA_SCRIPT), query, "-n", str(limit)], capture_output=True, text=True, timeout=30)
        entries = re.findall(r'标题: (.+?)\n链接: (.+?)\n来源: (.+?)\n摘要: (.+?)(?=\n---|\Z)', result.stdout, re.DOTALL)
        return [{"source": "bocha", "title": t.strip(), "url": u.strip(), "snippet": s.strip()[:300]} for t,u,_,s in entries]
    except Exception as e:
        return [{"source": "bocha", "error": str(e)}]

def _fc_one(key, key_num, query, limit):
    try:
        data = json.dumps({"query": query, "maxResults": limit}).encode()
        req = urllib.request.Request("https://api.firecrawl.dev/v0/search", data=data, headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"}, method="POST")
        resp = json.loads(urllib.request.urlopen(req, timeout=30).read())
        items = []
        for r in resp.get("data", []):
            meta = r.get("metadata", {}) or {}
            title = (meta.get("og:title") or meta.get("title") or r.get("title") or "")[:150]
            content = r.get("content", r.get("markdown", ""))
            url_m = re.search(r'\]\(([^)]+)\)', content)
            url = url_m.group(1) if url_m else ""
            snippet = re.sub(r'\[.*?\]\([^)]*\)\s*', '', content)[:300]
            snippet = re.sub(r'\s+', ' ', snippet).strip()
            items.append({"source": "firecrawl", "title": str(title), "url": url, "snippet": snippet[:300]})
        return items
    except urllib.error.HTTPError as e:
        if e.code in (429, 403, 402):
            raise
        return [{"source": "firecrawl", "error": f"HTTP {e.code}"}]
    except Exception as e:
        return [{"source": "firecrawl", "error": str(e)}]

def search_firecrawl(query, limit=5):
    for i, key in enumerate(FIRECRAWL_KEYS):
        try:
            result = _fc_one(key, i+1, query, limit)
            if result and not result[0].get("error") and result[0].get("url"):
                return result
        except urllib.error.HTTPError:
            continue
    return [{"source": "firecrawl", "error": "All keys exhausted"}] if FIRECRAWL_KEYS else [{"source": "firecrawl", "error": "No API key"}]

def search_qichacha(query, limit=5):
    return search_tavily(f"site:qichacha.com OR site:aiqicha.baidu.com OR site:tianyancha.com {query}", limit)


# ── 百度搜索（爬虫，无官方API）──
BAIDU_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"

def search_baidu(query, limit=5):
    """百度搜索 — 基于 requests + BeautifulSoup 爬取 baidu.com/s?wd= 页面"""
    if not _HAS_SCRAPER:
        return [{"source": "baidu", "error": "Missing requests/bs4"}]
    try:
        url = f"https://www.baidu.com/s?wd={urllib.parse.quote(query)}&rn={limit}"
        resp = requests.get(url, headers={"User-Agent": BAIDU_UA}, timeout=10)
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []
        for div in soup.select(".result") or soup.select(".c-container") or soup.select("div[class*='result']"):
            a = div.find("a")
            if not a or not a.get("href"):
                continue
            title = a.get_text(strip=True)
            href = a.get("href", "")
            # Skip ads and "大家还在搜"
            if "baidu.com" in href and "link?" not in href:
                continue
            abstract = ""
            span = div.find("span", class_="content-right_")
            if not span:
                span = div.find("div", class_="c-abstract")
            if span:
                abstract = span.get_text(strip=True)[:300]
            if title:
                results.append({"source": "baidu", "title": title[:150], "url": href.strip(), "snippet": abstract})
        return results[:limit] if results else [{"source": "baidu", "error": "No results parsed (可能被反爬)"}]
    except Exception as e:
        return [{"source": "baidu", "error": str(e)[:80]}]


# ── 搜狗微信搜索（爬虫）──
def search_sogou_wechat(query, limit=5):
    """搜狗微信文章搜索 — 通过 weixin.sogou.com 爬取微信公众号文章"""
    if not _HAS_SCRAPER:
        return [{"source": "sogou_wechat", "error": "Missing requests/bs4"}]
    try:
        url = f"https://weixin.sogou.com/weixin?type=2&query={urllib.parse.quote(query)}"
        resp = requests.get(url, headers={
            "User-Agent": BAIDU_UA,
            "Referer": "https://weixin.sogou.com/",
        }, timeout=10)
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []
        for li in soup.select(".news-list2 li") or soup.select(".news-box li") or soup.select(".wx-rb_item"):
            # 标题和链接
            h3 = li.find("h3") or li.find("a", attrs={"uigs": re.compile(r"article_title")})
            if not h3:
                continue
            a = h3.find("a") if h3.name == "h3" else h3
            if not a or not a.get("href"):
                continue
            title = a.get_text(strip=True)
            href = a.get("href", "")
            if href.startswith("/"):
                href = "https://weixin.sogou.com" + href
            # 摘要
            abstract = ""
            p = li.find("p", class_="txt-info") or li.find("div", class_="txt-info") or li.find("p")
            if p:
                abstract = p.get_text(strip=True)[:300]
            # 来源公众号
            source_span = li.find("span", class_="account") or li.find("a", attrs={"uigs": re.compile(r"account_name")})
            account = source_span.get_text(strip=True) if source_span else ""
            title_with_source = f"[{account}] {title}" if account else title
            if title:
                results.append({"source": "sogou_wechat", "title": title_with_source[:150], "url": href.strip(), "snippet": abstract})
        return results[:limit] if results else [{"source": "sogou_wechat", "error": "No results (可能被反爬/IP受限)"}]
    except Exception as e:
        return [{"source": "sogou_wechat", "error": str(e)[:80]}]


# ── 中文政策搜索（--zh 模式）──

# 中国城市分级：搜索策略差异化
#   T1（一线）: 杭州/成都/南京等省会 → 全引擎可
#   T2（二线）: 温州/绍兴/嘉兴 → Bocha + site:gov.cn
#   T3（三线以下）: 丽水/衢州/舟山 → Bocha-only + 3变体并行
CITY_TIERS = {
    # T1 — 省会/副省级/强经济城市（全引擎 OK）
    "北京": 1, "上海": 1, "广州": 1, "深圳": 1, "杭州": 1, "南京": 1, "成都": 1,
    "武汉": 1, "重庆": 1, "天津": 1, "苏州": 1, "宁波": 1, "青岛": 1, "厦门": 1,
    "大连": 1, "西安": 1, "长沙": 1, "郑州": 1, "济南": 1, "合肥": 1, "福州": 1,
    "昆明": 1, "沈阳": 1, "哈尔滨": 1, "贵阳": 1, "海口": 1,
    # T2 — 普通地级市
    "佛山": 2, "东莞": 2, "无锡": 2, "常州": 2, "南通": 2, "徐州": 2, "绍兴": 2,
    "嘉兴": 2, "珠海": 2, "中山": 2, "惠州": 2, "泉州": 2, "温州": 2, "金华": 2,
    "烟台": 2, "唐山": 2, "洛阳": 2, "襄阳": 2, "宜昌": 2, "芜湖": 2, "柳州": 2,
    "桂林": 2, "遵义": 2, "九江": 2, "赣州": 2, "绵阳": 2, "岳阳": 2, "邯郸": 2,
    # T3 — 适用--zh模式的其他城市
}

# ── 中文政策穷尽搜索（v3.0 — 完整覆盖）──

# 中国政策文件命名模式库 —— 穷举所有可能组合
POLICY_TYPE_WORDS = [
    "实施方案", "实施细则", "试行办法", "暂行办法",
    "工作方案", "实施意见", "管理办法", "操作规程",
    "指导意见", "通知", "公告", "公示",
]

LTCI_TERMS = [
    "长期护理保险", "长护险", "长期照护保险",
    "政策性长期护理保险", "失能护理保障",
    "护理保险", "照护保险",
]

CONTENT_FOCUS = [
    "筹资", "缴费", "费率", "待遇",
    "支付", "报销", "定点机构", "服务机构",
    "评估", "失能评估", "服务项目",
    "经办", "申报", "2024", "2025", "2026",
]

AGGREGATOR_SITES = [
    "site:m12333.cn",
    "site:ylqxzb.com",
    "site:pkulaw.com",
    "site:66law.cn",
]

# 各省市医保局域名模式
GOV_URL_PATTERNS = [
    "http://ybj.{city}.gov.cn",
    "http://{city}.gov.cn/ylbzj",
    "http://{city}.gov.cn/zwgk",
    "http://{city}.gov.cn/xxgk",
    "http://{city}.gov.cn/zhengce",
]


def _exhaustive_zh_variants(query):
    """为中文政策查询生成穷尽式变体列表（15-30个变体）

    中国政策文件命名极其标准化，穷举所有可能的命名组合，
    确保即使搜索引擎索引不完整，也能命中。
    """
    parts = query.split()
    city = parts[0] if parts else ""
    keyword = " ".join(parts[1:]) if len(parts) > 1 else ""

    variants = [query]  # 原词

    # 1. 术语变体（长护险 ↔ 长期护理保险 ↔ ...）
    if keyword:
        # 检测原查询包含哪个 LTCI 术语
        existing_term = next((t for t in LTCI_TERMS if t in query), None)
        if existing_term:
            # 替换为其他术语
            for term in LTCI_TERMS:
                if term != existing_term:
                    variants.append(query.replace(existing_term, term))
        else:
            # 没有 LTCI 术语，添加通用术语
            for term in LTCI_TERMS[:3]:
                variants.append(f"{city} {term}")

    # 2. 政策类型变体（最多8个最有代表性的组合）
    if city:
        # 用第一个 LTCI 术语遍历政策类型
        term = LTCI_TERMS[0]
        for ptype in POLICY_TYPE_WORDS[:8]:  # 仅用前8个最常用政策类型
            variants.append(f"{city} {term} {ptype}")
        # 再加 2 个用"长护险"的简写形式
        for ptype in ["实施方案", "实施细则", "筹资标准"]:
            variants.append(f"{city} 长护险 {ptype}")

    # 3. 内容焦点变体
    if city:
        for term in LTCI_TERMS[:1]:
            for focus in CONTENT_FOCUS:
                variants.append(f"{city} {term} {focus}")

    # 4. 聚合平台搜索变体
    if city:
        for site in AGGREGATOR_SITES:
            for term in LTCI_TERMS[:1]:
                variants.append(f"{site} {city} {term}")

    # 5. 政府官网限域搜索
    if city:
        vars_to_add = [
            f"site:{city}.gov.cn 长期护理保险",
            f"site:gov.cn {city} 长护险",
            f"{city} 医保局 长护险 政策",
            f"{city} 第六险",
            f"{city} 失能 护理 保险",
        ]
        variants.extend(vars_to_add)

    # 去重 + 限长（最多30个，保留前15个最优先的）
    seen = set()
    unique = []
    for v in variants:
        if v not in seen:
            seen.add(v)
            unique.append(v)
    return unique[:30]


def _try_gov_url(city):
    """尝试直接访问城市医保局网站，返回工作中URL列表及内容摘要"""
    from urllib.request import urlopen, Request
    results = []
    for pattern in GOV_URL_PATTERNS:
        url = pattern.format(city=city)
        try:
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
            resp = urlopen(req, timeout=5)
            html = resp.read().decode("utf-8", errors="ignore")[:500]
            # 检查页面是否包含长护险关键词
            if any(k in html for k in ["长护险", "长期护理", "护理保险", "失能"]):
                results.append({"source": "gov_direct", "title": f"{city} 医保局页面（直连）", "url": url, "snippet": html[:200]})
        except:
            pass
    return results


def search_zh(query, limit=8):
    """中文政策穷尽搜索 v3.0 — bocha + 百度 + 搜狗微信 + 聚合平台 + 直连探测

    架构：
    ├── Bocha 变体批量搜索（15-30个变体并行）→ 覆盖所有命名组合
    ├── 百度搜索单次调用                     → 补充百度生态结果
    ├── 搜狗微信搜索                         → 微信公众号文章
    ├── 聚合平台搜索（m12333/ylqxzb/pkulaw）→ 搜索引擎不可达的内容
    └── 政府网站直连探测 → 搜索引擎完全不索引的内容
    """
    parts = query.split()
    city = parts[0] if parts else ""

    # 生成穷尽变体
    all_variants = _exhaustive_zh_variants(query)

    all_results = []
    seen_urls = set()

    def _add(results):
        for r in results:
            url = r.get("url", "")
            if url and url not in seen_urls and not r.get("error"):
                seen_urls.add(url)
                all_results.append(r)

    # ── 第一轮：优先变体（前8个最高质量变体）──
    priority_variants = all_variants[:10]
    for v in priority_variants:
        _add(search_bocha(v, limit))

    # ── 第二轮：剩余变体（第9-30个）──
    if len(all_results) < limit * 2:
        secondary_variants = all_variants[10:25]
        for v in secondary_variants:
            _add(search_bocha(v, limit))

    # ── 第三轮：百度 + 搜狗微信（补充中文生态）──
    _add(search_baidu(query, limit))
    _add(search_sogou_wechat(query, limit))

    # ── 第四轮：聚合平台 Deep Dive ──
    if len(all_results) < limit * 2:
        # 用 Bocha 搜聚合平台的 site: 限定
        for site in AGGREGATOR_SITES:
            _add(search_bocha(f"{site} {city} 长护险 政策", limit))

    # ── 第四轮：政府网站直连探测（非搜索引擎通道）──
    if city and len(all_results) < limit * 3:
        _add(_try_gov_url(city))

    # 最终去重排序
    seen = set()
    final = []
    for r in all_results:
        u = r.get("url", "")
        if u and u not in seen:
            seen.add(u)
            final.append(r)

    return final[:limit * 4]

def deduplicate(all_results):
    seen, deduped = set(), []
    for r in all_results:
        url = r.get("url", "")
        if url and url not in seen:
            seen.add(url)
            deduped.append(r)
    return deduped

def search_all(query, engines="tavily,brave,firecrawl,bocha", limit=5):
    engine_map = {
        "tavily": search_tavily, "brave": search_brave, "serper": search_serper,
        "bocha": search_bocha, "firecrawl": search_firecrawl,
        "qichacha": search_qichacha,
        "baidu": search_baidu, "sogou_wechat": search_sogou_wechat,
        "zh": search_zh,
    }
    selected = [e.strip() for e in engines.split(",") if e.strip() in engine_map]
    all_results = []
    with ThreadPoolExecutor(max_workers=len(selected)) as executor:
        futures = {executor.submit(engine_map[e], query, limit): e for e in selected}
        for future in as_completed(futures):
            try:
                all_results.extend(future.result())
            except:
                pass
    return deduplicate(all_results)

def engine_status():
    return {
        "tavily": len(TAVILY_KEYS), "brave": 1 if BRAVE_KEY else 0,
        "serper": 1 if SERPER_KEY else 0, "bocha": 1 if BOCHA_KEY else 0,
        "firecrawl": len(FIRECRAWL_KEYS),
        "baidu": 1 if _HAS_SCRAPER else 0, "sogou_wechat": 1 if _HAS_SCRAPER else 0,
    }

if __name__ == "__main__":
    import urllib.parse
    args = sys.argv[1:]
    if not args or "--help" in args or "-h" in args:
        print("用法: python3 multi_search.py <查询词> [选项]")
        print("  --json                 JSON输出（供cron agent解析）")
        print("  --status               检查引擎可用性")
        print("  --engines              指定引擎列表（默认: tavily,brave,firecrawl,bocha）")
        print("                         可选: qichacha / 任意组合")
        print("  --zh                   中文政策模式（bocha + baidu + 搜狗微信，适合长护险/公众号/政府文件）")
        print("  --limit N              每引擎返回条数（默认5）")
        print("")
        print("模式速查:")
        print("  默认（平衡）:    tavily+brave+firecrawl+bocha       ~3-10秒  通用场景")
        print("  --zh（中文）:    bocha + baidu + 搜狗微信     ~5-12秒  长护险/公众号/政府文件")
        print("  --engines=...（深挖）: 可加 qichacha  ~8-30秒  深挖")
        print("")
        print("⚠️ 已知问题: Tavily/Brave 将'长期护理保险'误解析为英文'engine'")
        print("   中文政策搜索请用 --zh 模式，不受此问题影响。")
        sys.exit(0)
    if "--status" in args:
        st = engine_status()
        print(f"Tavily: {st['tavily']} key(s) {'✅' if st['tavily'] else '❌'}")
        print(f"Brave: {'✅' if st['brave'] else '❌'}")
        print(f"Serper: {'✅' if st['serper'] else '❌'}")
        print(f"Bocha: {'✅' if st['bocha'] else '❌'}")
        print(f"Firecrawl: {st['firecrawl']} key(s) {'✅' if st['firecrawl'] else '❌'}")
        print(f"百度搜索: {'✅' if st['baidu'] else '❌'}")
        print(f"搜狗微信: {'✅' if st['sogou_wechat'] else '❌'}")
        sys.exit(0)
    # 解析参数：支持 --flag 放在查询词前后
    query = None
    engines = 'tavily,brave,firecrawl,bocha'
    limit = 5
    json_mode = False
    zh_mode = False
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--engines" and i + 1 < len(args):
            engines = args[i + 1]
            i += 2
        elif a == "--zh":
            zh_mode = True
            engines = "zh"
            i += 1
        elif a == "--limit" and i + 1 < len(args):
            limit = int(args[i + 1])
            i += 2
        elif a == "--json":
            json_mode = True
            i += 1
        elif a.startswith("--"):
            i += 1  # skip unknown flags
        else:
            query = a  # first non-flag arg is the query
            i += 1
    if not query:
        print("❌ 请提供搜索关键词")
        print("用法: python3 multi_search.py <查询词> [选项]")
        sys.exit(1)
    results = search_all(query, engines, limit)
    if json_mode:
        print(json.dumps({"query": query, "timestamp": time.strftime("%Y-%m-%d %H:%M"), "total": len(results), "engines": engine_status(), "engine_set": engines, "mode": "full" if "qichacha" in engines else "default", "results": results}, ensure_ascii=False, indent=2))
    else:
        mode_label = "🔥深度" if "qichacha" in engines else ("🇨🇳中文" if zh_mode else "⚖️平衡")
        print(f"\n🔍 多引擎搜索 [{mode_label}]: {query}")
        print(f"   引擎: {engines} | 结果: {len(results)}条\n")
        icons = {"tavily": "🌐", "brave": "🦁", "serper": "📰", "bocha": "🔍", "firecrawl": "🔥", "qichacha": "🏢", "baidu": "🔵", "sogou_wechat": "💬", "zh": "🇨🇳"}
        for i, r in enumerate(results, 1):
            s = r.get("source", "?")
            e = r.get("error", "")
            if e: print(f"  [{s}] ⚠️ {e}")
            else: print(f"  {icons.get(s,'📄')} [{s}] {r.get('title','')}\n     {r.get('url','')}\n     {r.get('snippet','')[:150]}\n")
