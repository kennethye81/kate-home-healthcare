#!/usr/bin/env python3
"""数据新鲜度扫描——检查 facts.json 中的事实是否过期，更新 HTML 报告顶部警告。"""
import json
from pathlib import Path
from datetime import datetime, timedelta

KB = Path("/Users/kennethye/workspace/kate-kb")
FACTS = KB / "data/facts.json"
HTML_DIR = KB / "html"

STALE_DAYS = 30  # 超过30天未更新的数据点为「过时」

def check_freshness():
    if not FACTS.exists():
        return {"stale": 0, "total": 0}
    
    facts = json.loads(FACTS.read_text())
    fact_list = facts.get("facts", [])
    now = datetime.now()
    
    stale_count = 0
    for fact in fact_list:
        updated = fact.get("updated_at", fact.get("created_at", ""))
        if updated:
            try:
                dt = datetime.fromisoformat(updated)
                if (now - dt).days > STALE_DAYS:
                    stale_count += 1
            except:
                pass
    
    return {
        "stale": stale_count,
        "total": len(fact_list),
        "checked_at": now.isoformat()
    }

def inject_banners():
    result = check_freshness()
    
    if result["stale"] == 0:
        print(f"🟢 数据新鲜度: {result['total']} 条事实全部在 {STALE_DAYS} 天内")
        return
    
    ratio = result["stale"] / max(result["total"], 1)
    print(f"⚠️ 数据新鲜度: {result['stale']}/{result['total']} 条可能过时 ({ratio:.0%})")
    
    # 在每个 HTML 顶部注入警告（如果报告引用过时数据）
    # 简化版：只输出汇总报告
    report = {
        "checked_at": result["checked_at"],
        "total_facts": result["total"],
        "stale_facts": result["stale"],
        "freshness_ratio": f"{1 - ratio:.0%}"
    }
    
    report_path = KB / "html/freshness-report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"📋 新鲜度报告: {report_path}")

if __name__ == "__main__":
    inject_banners()
