#!/usr/bin/env python3
"""从 facts.json 生成 pages/compare/ 下的 6 个跨国对比页"""
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

KB = Path("/Users/kennethye/workspace/kate-kb")
FACTS_FILE = KB / "data/facts.json"
COMPARE_DIR = KB / "pages/compare"

COUNTRY_ORDER = ["JP", "DE", "SG", "UK", "US", "HK", "CN", "TW", "AU", "KR", "FR", "NL", "SE", "CA", "IL", "BR"]
COUNTRY_NAMES = {
    "JP":"🇯🇵 日本","DE":"🇩🇪 德国","SG":"🇸🇬 新加坡","UK":"🇬🇧 英国","US":"🇺🇸 美国",
    "HK":"🇭🇰 香港","CN":"🇨🇳 中国","TW":"🇹🇼 台湾","AU":"🇦🇺 澳大利亚","KR":"🇰🇷 韩国",
    "FR":"🇫🇷 法国","NL":"🇳🇱 荷兰","SE":"🇸🇪 瑞典","CA":"🇨🇦 加拿大","IL":"🇮🇱 以色列","BR":"🇧🇷 巴西"
}

PAGES = {
    "payment.md": {
        "title": "支付体系跨国对比",
        "metrics": ["payment_amount", "premium_rate", "oop_ratio"],
        "desc": "17 国居家医疗支付标准、保险费率、自付比例对比"
    },
    "timeline.md": {
        "title": "政策时间线跨国对比",
        "metrics": ["founded"],
        "desc": "17 国长护险/HaH 立法与改革时间线"
    },
    "companies.md": {
        "title": "头部公司跨国对比",
        "metrics": ["revenue", "employees", "funding", "valuation"],
        "desc": "54 家居家医疗公司收入、融资、估值、员工规模对比"
    },
    "market.md": {
        "title": "市场规模跨国对比",
        "metrics": ["market_size", "coverage_count", "growth_rate"],
        "desc": "17 国居家医疗市场规模、覆盖人数、增长率对比"
    },
}

def load_facts():
    if not FACTS_FILE.exists():
        return []
    return json.loads(FACTS_FILE.read_text()).get("facts", [])

def build_comparison_page(facts, metrics, title, desc):
    today = datetime.now().strftime("%Y-%m-%d")
    total = len(facts)
    
    lines = [
        "---",
        "auto_generated: true",
        f"generated_at: {today}",
        f"total_facts: {total}",
        "---",
        "",
        f"# {title}",
        "",
        f"> {desc}",
        f"> 数据源: {total} 条结构化事实 · 自动生成于 {today}",
        "",
        "---",
        ""
    ]
    
    for metric in metrics:
        items = [f for f in facts if f.get("metric") == metric]
        if not items:
            continue
        
        # 按国家分组
        by_country = defaultdict(list)
        for item in items:
            by_country[item["country"]].append(item)
        
        metric_names = {
            "payment_amount": "💳 支付金额",
            "premium_rate": "📊 保险费率",
            "oop_ratio": "💰 自付比例",
            "founded": "📅 成立/立法年份",
            "revenue": "📈 公司收入",
            "employees": "👥 员工数",
            "funding": "💵 融资额",
            "valuation": "🏷️ 估值",
            "market_size": "📐 市场规模",
            "coverage_count": "👤 覆盖人数",
            "growth_rate": "🚀 增长率",
        }
        
        lines.append(f"## {metric_names.get(metric, metric)}")
        lines.append("")
        lines.append(f"| 国家 | 数据 | 来源报告 |")
        lines.append("|------|------|------|")
        
        for code in COUNTRY_ORDER:
            vals = by_country.get(code, [])
            if vals:
                for v in vals[:3]:  # 每个国家最多 3 条
                    report_name = v.get("report", "")[:50]
                    lines.append(f"| {COUNTRY_NAMES.get(code, code)} | {v['value'][:60]} | {report_name} |")
        
        lines.append("")
    
    lines.append("---")
    lines.append(f"> 🤖 自动生成于 {today}")
    return "\n".join(lines)

def main():
    facts = load_facts()
    COMPARE_DIR.mkdir(parents=True, exist_ok=True)
    
    for filename, config in PAGES.items():
        content = build_comparison_page(facts, config["metrics"], config["title"], config["desc"])
        (COMPARE_DIR / filename).write_text(content)
        print(f"✅ {filename}: {content.count(chr(10))} 行")

if __name__ == "__main__":
    main()
