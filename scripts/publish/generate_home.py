#!/usr/bin/env python3
"""从 facts.json 生成 Home.md — 17 国 × 10 指标跨国对比矩阵"""
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

KB = Path("/Users/kennethye/workspace/kate-kb")
FACTS_FILE = KB / "data/facts.json"
INSIGHTS_FILE = KB / "data/insights.json"
HOME = KB / "Home.md"

def load_facts():
    if not FACTS_FILE.exists():
        return []
    return json.loads(FACTS_FILE.read_text()).get("facts", [])

def build_comparison_table(facts, metric, title, unit_hint=""):
    """构建 17 国 × 指标对比表"""
    # 按国家聚合
    country_data = defaultdict(list)
    for f in facts:
        if f.get("metric") == metric:
            country_data[f.get("country", "GLOBAL")].append(f["value"])
    
    COUNTRY_ORDER = ["JP", "DE", "SG", "UK", "US", "HK", "CN", "TW", "AU", "KR", "FR", "NL", "SE", "CA", "IL", "BR"]
    COUNTRY_NAMES = {"JP":"🇯🇵 日本","DE":"🇩🇪 德国","SG":"🇸🇬 新加坡","UK":"🇬🇧 英国","US":"🇺🇸 美国","HK":"🇭🇰 香港","CN":"🇨🇳 中国","TW":"🇹🇼 台湾","AU":"🇦🇺 澳大利亚","KR":"🇰🇷 韩国","FR":"🇫🇷 法国","NL":"🇳🇱 荷兰","SE":"🇸🇪 瑞典","CA":"🇨🇦 加拿大","IL":"🇮🇱 以色列","BR":"🇧🇷 巴西"}
    
    lines = [f"### {title}"]
    lines.append(f"| 国家 | {title} | 来源 |")
    lines.append("|------|------|------|")
    
    for code in COUNTRY_ORDER:
        values = country_data.get(code, [])
        if values:
            v = values[0][:60]
            lines.append(f"| {COUNTRY_NAMES.get(code, code)} | {v} | — |")
    
    return "\n".join(lines)

def generate():
    facts = load_facts()
    today = datetime.now().strftime("%Y-%m-%d")
    total = len(facts)
    
    # 指标分布
    metrics = defaultdict(list)
    for f in facts:
        metrics[f["metric"]].append(f)
    
    top_metrics = sorted(metrics.items(), key=lambda x: -len(x[1]))
    
    sections = []
    sections.append("---")
    sections.append("auto_generated: true")
    sections.append(f"generated_at: {today}")
    sections.append(f"total_facts: {total}")
    sections.append("---")
    sections.append("")
    sections.append("# 🌏 全球居家医疗知识图谱")
    sections.append("")
    sections.append(f"> 167 份深度报告 · 17 个国家 · {total} 条结构化数据 · 持续更新")
    sections.append("")
    sections.append("---")
    sections.append("")
    sections.append(f"## 📊 核心指标跨国对比")
    sections.append("")
    
    # 取排名前 8 的指标（每条至少 3 国数据）
    shown = 0
    for metric, items in top_metrics:
        countries = set(i["country"] for i in items)
        if len(countries) >= 3 and shown < 8:
            title_map = {
                "payment_amount": "💳 支付金额",
                "payment_detail": "💳 支付明细",
                "table_payment": "💳 支付数据",
                "payment_amount_currency": "💳 支付货币金额",
                "premium_rate": "📊 保险费率",
                "coverage_count": "👤 覆盖人数",
                "market_size": "📐 市场规模",
                "revenue": "📈 公司收入",
                "funding": "💵 融资额",
                "employees": "👥 员工数",
                "founded": "📅 成立年份",
                "growth_rate": "🚀 增长率",
                "locations": "🏢 网点数",
                "percentage": "📊 占比",
                "valuation": "🏷️ 估值",
                "oop_ratio": "💰 自付比例",
                "patient_count": "🏥 患者数",
                "readmission_rate": "🔄 再入院率",
                "satisfaction": "⭐ 满意度",
                "mortality_rate": "⚠️ 死亡率",
                "er_reduction": "🚑 急诊减少",
                "bed_count": "🛏️ 病床数",
                "bed_days": "📅 住院天数",
                "nurse_count": "👩‍⚕️ 护士数",
                "avg_salary": "💵 平均薪资",
                "aging_rate": "👴 老龄化率",
                "gdp_share": "📊 GDP占比",
                "budget": "💰 预算",
                "policy_year": "📜 政策年份",
                "hospitalization_rate": "🏥 住院率",
            }
            title = title_map.get(metric, metric)
            sections.append(build_comparison_table(items, metric, title))
            sections.append("")
            shown += 1
    
    sections.append("---")
    sections.append("")
    sections.append("## 🌏 按国家探索")
    sections.append("")
    sections.append("| Tier 1 | Tier 2 | Tier 3 |")
    sections.append("|------|------|------|")
    sections.append("| [🇭🇰 香港](pages/hong-kong/overview.md) | [🇸🇬 新加坡](pages/global/新加坡/00-概览.md) | [🇰🇷 韩国](pages/global/韩国/00-概览.md) |")
    sections.append("| [🇯🇵 日本](pages/global/日本/00-概览.md) | [🇬🇧 英国](pages/global/英国/00-概览.md) | [🇫🇷 法国](pages/global/法国/00-概览.md) |")
    sections.append("| [🇩🇪 德国](pages/global/德国/00-概览.md) | [🇺🇸 美国](pages/global/美国/00-概览.md) | [🇳🇱 荷兰](pages/global/荷兰/00-概览.md) |")
    sections.append("| | [🇨🇳 中国](pages/global/中国/00-概览.md) | [🇸🇪 瑞典](pages/global/瑞典/00-概览.md) |")
    sections.append("| | [🇹🇼 台湾](pages/global/台湾/00-概览.md) | [🇨🇦 加拿大](pages/global/加拿大/00-概览.md) |")
    sections.append("| | [🇦🇺 澳大利亚](pages/global/澳大利亚/00-概览.md) | [🇮🇱 以色列](pages/global/以色列/00-概览.md) |")
    sections.append("| | | [🇧🇷 巴西](pages/global/巴西/00-概览.md) |")
    sections.append("")
    sections.append("---")
    sections.append("")
    sections.append("## 📂 跨国对比矩阵")
    sections.append("")
    sections.append(f"- [支付体系对比 →](pages/compare/payment.md)")
    sections.append(f"- [政策时间线对比 →](pages/compare/timeline.md)")
    sections.append(f"- [头部公司对比 →](pages/compare/companies.md)")
    sections.append(f"- [市场规模对比 →](pages/compare/market.md)")
    sections.append("")
    sections.append("---")
    sections.append("")
    sections.append(f"> 🤖 自动生成于 {today} · 数据源: data/facts.json ({total} 条)")
    
    HOME.write_text("\n".join(sections) + "\n")
    print(f"✅ Home.md 已生成: {total} 条数据, {shown} 个指标对比表")

if __name__ == "__main__":
    generate()
