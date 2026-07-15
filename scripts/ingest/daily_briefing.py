#!/usr/bin/env python3
"""每日简报生成器——更新 pages/home.md 的「今日3件事」板块。"""
import json, subprocess, sys, re
from pathlib import Path
from datetime import datetime, timedelta

KB = Path("/Users/kennethye/workspace/kate-kb")
HOME = KB / "Home.md"
MULTI_SEARCH = "/Users/kennethye/workspace/kate_quant/multi_search.py"

def get_latest_rss():
    """尝试从 RSS 监控获取最新动态"""
    # 简化版：直接搜索最近3天的居家医疗新闻
    queries = [
        "hospital at home home health care policy change 2026 site:homehealthcarenews.com",
        "long term care insurance reform 2026 Japan Pflegeversicherung",
        "virtual ward NHS hospital home latest 2026"
    ]
    items = []
    for q in queries:
        try:
            r = subprocess.run(
                ["PYTHONPATH=", "/usr/bin/python3", MULTI_SEARCH, "--fast", "--json", q],
                capture_output=True, text=True, timeout=30,
                env={**__import__('os').environ, 'PYTHONPATH': ''}
            )
            data = json.loads(r.stdout)
            for item in data.get("results", [])[:3]:
                items.append({
                    "title": item.get("title", "")[:80],
                    "url": item.get("url", ""),
                    "source": item.get("source", "web")
                })
        except Exception:
            continue
    return items[:3]

def generate():
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    
    # 尝试获取 RSS 动态（失败则用占位符）
    items = get_latest_rss()
    
    if items:
        lines = []
        for i, item in enumerate(items):
            lines.append(f"### {i+1}. [{item['title']}]({item['url']})")
            lines.append(f"*来源: {item['source']} · {today}*")
            lines.append("")
    else:
        lines = [
            "### 1. ~~（RSS 监控暂无新数据，等待下次扫描）~~",
            "",
            "### 2. ~~（跨国共振检测未触发）~~",
            "",
            "### 3. ~~（无新报告入库）~~",
            ""
        ]
    
    # 读取 home.md，替换 DAILY_BRIEFING 区块
    content = HOME.read_text()
    pattern = r"(<!-- DAILY_BRIEFING_START -->)(.*?)(<!-- DAILY_BRIEFING_END -->)"
    replacement = f"<!-- DAILY_BRIEFING_START -->\n\n{''.join(chr(10) + l for l in lines)}\n<!-- DAILY_BRIEFING_END -->"
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # 同时更新 STATS 区块的最后更新日期
    new_content = re.sub(
        r"📅 最后更新 \| .*",
        f"📅 最后更新 | {today}",
        new_content
    )
    
    HOME.write_text(new_content)
    print(f"✅ home.md 已更新 ({today})")

if __name__ == "__main__":
    generate()
