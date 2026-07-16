#!/usr/bin/env python3
"""从 167 份 .md 报告批量抽取结构化数据 → data/facts.json"""
import json, re, sys
from pathlib import Path
from collections import defaultdict

KB = Path("/Users/kennethye/workspace/kate-kb")
REPORTS_DIR = KB / "reports"
FACTS_FILE = KB / "data/facts.json"

# === 国家关键词映射 ===
COUNTRY_KEYWORDS = {
    "JP": ["日本", "japan", "介護", "介护", "nichii", "sompo", "benesse", "tsukui"],
    "DE": ["德国", "germany", "deutsch", "pflege", "johanniter", "korian", "deutsche fachpflege"],
    "HK": ["香港", "hong kong", "hk", "evercare", "bamboos", "qualitycare", "ydcare", "eden home"],
    "SG": ["新加坡", "singapore", "sg", "speedoc", "nuhs", "sgh", "singhealth", "moht", "mic@home"],
    "UK": ["英国", "uk", "united kingdom", "nhs", "cera", "birdie", "doccla", "huma", "whzan", "clinitouch", "lottie", "elder", "feebris", "luscii", "inhealthcare", "isansys", "docobo"],
    "US": ["美国", "us", "united states", "medicare", "medicaid", "dispatchhealth", "contessa", "amedisys", "bayada", "cadence", "biofourmis", "current health", "centerwell", "honor", "home instead", "signify", "amwell", "sollis", "atrium", "cleveland", "mayo clinic", "kaiser", "mass general", "mount sinai", "johns hopkins", "uchicago"],
    "CN": ["中国", "china", "cn", "长护险", "天与", "福寿康", "普康", "璞缘", "小橙", "易得康"],
    "AU": ["澳大利亚", "australia", "au", "amplar", "bolton clarke", "hammondcare", "kincare", "silver chain", "bupa home care", "calvary", "regis", "trilogy", "australian unity", "home instead au"],
    "TW": ["台湾", "taiwan", "tw"],
    "FR": ["法国", "france", "fr", "sante cie", "had"],
    "KR": ["韩国", "korea", "kr", "silwhon"],
    "NL": ["荷兰", "netherlands", "nl", "buurtzorg"],
    "SE": ["瑞典", "sweden", "se", "attendo"],
    "CA": ["加拿大", "canada", "ca", "alayacare", "ontario"],
    "IL": ["以色列", "israel", "il", "blev shalem", "yad sarah", "isavta"],
    "BR": ["巴西", "brazil", "br", "home doctor"],
}

def detect_countries(text_lower):
    scores = defaultdict(int)
    for code, keywords in COUNTRY_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                scores[code] += 1
    return [c for c, s in sorted(scores.items(), key=lambda x: -x[1])] if scores else ["GLOBAL"]

# === 指标提取模式 ===
METRICS = [
    # 支付金额
    (r'(?:支付[金额标准]?|给[付付]|reimbursement|payment)[：:＝=]\s*[\$€¥]?\s*([\d,]+\.?\d*)\s*(万|亿|元|USD|EUR|JPY|GBP|HKD|SGD|/月|/次|/日|/年|/人)?', 'payment_amount'),
    (r'(?:缴费率|保险费率)[：:＝=]\s*([\d,.]+)\s*%?', 'premium_rate'),
    (r'(?:自付比例|OOP|out.of.pocket)[：:＝=]?\s*([\d,.]+)\s*%', 'oop_ratio'),
    # 覆盖人数
    (r'(?:覆盖|认定|参保|受益)[人数量]?[：:＝=]?\s*([\d,]+\.?\d*)\s*(万|亿|人|M|B)?', 'coverage_count'),
    # 市场规模
    (r'(?:市场规模|market.size|TAM)[：:＝=]?\s*[\$€¥]?\s*([\d,]+\.?\d*)\s*(万|亿|M|B|K)?', 'market_size'),
    # 公司收入
    (r'(?:收入|营收|revenue|ARR)[：:＝=]?\s*[\$€¥]?\s*([\d,]+\.?\d*)\s*(万|亿|M|B|K)?', 'revenue'),
    # 估值
    (r'(?:估值|valuation)[：:＝=]?\s*[\$€¥]?\s*([\d,]+\.?\d*)\s*(万|亿|M|B|K)?', 'valuation'),
    # 融资
    (r'(?:融资|funding|融资总额)[：:＝=]?\s*[\$€¥]?\s*([\d,]+\.?\d*)\s*(万|亿|M|B|K)?', 'funding'),
    # 员工数
    (r'(?:员工|雇员|employees|headcount)[数数量]?[：:＝=]?\s*([\d,]+\.?\d*)\s*(万|人|名)?', 'employees'),
    # 成立年份
    (r'(?:成立于?|创立于?|founded|established)[：:＝=]?\s*(\d{4})', 'founded'),
    # 百分比
    (r'(?:占比|比例|share|penetration|coverage.rate)[：:＝=]?\s*([\d,.]+)\s*%', 'percentage'),
    # 增长率
    (r'(?:增长|增速|growth|CAGR)[：:＝=]?\s*([\d,.]+)\s*%', 'growth_rate'),
    # 医院/网点数
    (r'(?:网点|医院|诊所|网点数|locations|sites|branches)[：:＝=]?\s*([\d,]+)\s*(个|家)?', 'locations'),
]

def extract_from_report(filepath):
    try:
        text = filepath.read_text(encoding='utf-8', errors='ignore')
    except:
        return []
    text_lower = text.lower()
    countries = detect_countries(text_lower)
    
    facts = []
    for pattern, metric_type in METRICS:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            raw_value = m.group(0).strip()
            # 清理
            raw_value = re.sub(r'[\*\_`]', '', raw_value)
            line_num = text[:m.start()].count('\n') + 1
            
            facts.append({
                "country": countries[0],  # 主导国家
                "alt_countries": countries[1:],  # 次要国家
                "metric": metric_type,
                "value": raw_value,
                "report": filepath.name,
                "line": line_num
            })
    return facts

def main():
    md_files = sorted(REPORTS_DIR.glob("*.md"))
    if not md_files:
        print("❌ 无报告")
        return
    
    all_facts = []
    stats = defaultdict(int)
    
    for i, f in enumerate(md_files):
        facts = extract_from_report(f)
        all_facts.extend(facts)
        for fact in facts:
            stats[fact['metric']] += 1
        if (i + 1) % 20 == 0:
            print(f"  进度: {i+1}/{len(md_files)} 份, {len(all_facts)} 条...")
    
    # 去重（同一报告+同一指标+同一值）
    seen = set()
    unique = []
    for f in all_facts:
        key = (f['report'], f['metric'], f['value'][:50])
        if key not in seen:
            seen.add(key)
            unique.append(f)
    
    # 写入
    out = {
        "_description": "Kate 知识库结构化事实数据库",
        "_version": "4.1.0",
        "_updated": Path(__file__).stat().st_mtime,
        "_total_facts": len(unique),
        "_total_reports": len(md_files),
        "facts": unique
    }
    
    FACTS_FILE.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    
    print(f"\n{'='*50}")
    print(f"✅ 完成: {len(md_files)} 份报告 → {len(unique)} 条数据 (去重后)")
    print(f"\n指标分布:")
    for metric, count in sorted(stats.items(), key=lambda x: -x[1]):
        print(f"  {metric}: {count}")
    
    # 国家分布
    country_dist = defaultdict(int)
    for f in unique:
        country_dist[f['country']] += 1
    print(f"\n国家分布:")
    for c, n in sorted(country_dist.items(), key=lambda x: -x[1]):
        print(f"  {c}: {n}")

if __name__ == "__main__":
    main()
