#!/usr/bin/env python3
"""生成 HTML 报告目录页——搜索、筛选、排序。"""
import json, sys
from pathlib import Path
from datetime import datetime

KB = Path("/Users/kennethye/workspace/kate-kb")
HTML_DIR = KB / "html"
OUTPUT = KB / "html/index.html"

def scan_reports():
    reports = []
    for f in sorted(HTML_DIR.glob("*.html"), reverse=True):
        if f.name == "index.html":
            continue
        stat = f.stat()
        name = f.stem
        # 尝试从文件名解析日期
        date_str = name[:10] if len(name) >= 10 and name[4] == "-" else "unknown"
        # 尝试从文件名解析国家
        countries = []
        for c in ["hk", "sg", "jp", "de", "uk", "us", "cn", "au", "fr", "kr", "br", "ca", "se", "nl", "il", "tw"]:
            if f"-{c}-" in name or f"-{c}." in name or name.endswith(f"-{c}"):
                countries.append(c.upper())
        
        reports.append({
            "name": name,
            "file": f.name,
            "date": date_str,
            "size_kb": round(stat.st_size / 1024, 1),
            "countries": countries or ["GLOBAL"],
            "url": f.name
        })
    return reports

def generate():
    reports = scan_reports()
    
    # 构建 countries 列表用于 filter
    all_countries = sorted(set(c for r in reports for c in r["countries"]))
    
    html = f"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kate 知识库 · 研究报告目录</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f8fafc; color: #1e293b; line-height: 1.6; }}
header {{ background: linear-gradient(135deg, #0f766e, #155e75, #1d4ed8); color: white; padding: 48px 24px 32px; text-align: center; }}
header h1 {{ font-size: clamp(28px, 5vw, 44px); margin-bottom: 8px; }}
header p {{ opacity: .85; font-size: 16px; }}
.controls {{ max-width: 1200px; margin: 0 auto; padding: 16px 20px; display: flex; gap: 10px; flex-wrap: wrap; }}
.controls input, .controls select {{ padding: 10px 14px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 14px; flex: 1; min-width: 150px; }}
.list {{ max-width: 1200px; margin: 0 auto; padding: 0 20px 40px; }}
.card {{ background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px 20px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; }}
.card:hover {{ border-color: #0f766e; box-shadow: 0 4px 12px rgba(15,118,110,.08); }}
.card .info {{ flex: 1; min-width: 200px; }}
.card .name {{ font-weight: 600; color: #0f172a; }}
.card .meta {{ font-size: 13px; color: #64748b; margin-top: 4px; }}
.card .tag {{ display: inline-block; background: #dbeafe; color: #1d4ed8; padding: 2px 8px; border-radius: 4px; font-size: 12px; margin-right: 4px; }}
.card a {{ color: #0f766e; text-decoration: none; font-weight: 500; white-space: nowrap; }}
.card a:hover {{ text-decoration: underline; }}
.stats {{ max-width: 1200px; margin: 0 auto; padding: 8px 20px 0; color: #64748b; font-size: 14px; }}
.hidden {{ display: none; }}
</style>
</head>
<body>
<header>
<h1>📱 Kate 知识库 · 研究报告</h1>
<p>{len(reports)} 份报告 · {len(all_countries)} 个国家/地区 · 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
</header>
<div class="controls">
<input type="text" id="search" placeholder="🔍 搜索报告名称..." oninput="filter()">
<select id="country" onchange="filter()">
<option value="">🌏 所有国家</option>
{"".join(f'<option value="{c}">{c}</option>' for c in all_countries)}
</select>
<select id="sort" onchange="filter()">
<option value="date">📅 按日期（最新）</option>
<option value="name">📋 按名称</option>
<option value="size">📦 按大小</option>
</select>
</div>
<div class="stats" id="stats">{len(reports)} 份报告</div>
<div class="list" id="list">
</div>
<script>
const reports = {json.dumps(reports, ensure_ascii=False)};
const list = document.getElementById('list');
const stats = document.getElementById('stats');
const search = document.getElementById('search');
const country = document.getElementById('country');
const sort = document.getElementById('sort');

function render(filtered) {{
    list.innerHTML = filtered.map(r => `
<div class="card">
<div class="info">
<div class="name">${{r.name}}</div>
<div class="meta">${{r.date}} · ${{r.size_kb}}KB · ${{r.countries.map(c => `<span class="tag">${{c}}</span>`).join(' ')}}</div>
</div>
<a href="${{r.url}}" target="_blank">查看报告 →</a>
</div>`).join('');
    stats.textContent = `${{filtered.length}} 份报告`;
}}

function filter() {{
    let filtered = [...reports];
    const q = search.value.toLowerCase();
    const c = country.value;
    const s = sort.value;

    if (q) filtered = filtered.filter(r => r.name.toLowerCase().includes(q));
    if (c) filtered = filtered.filter(r => r.countries.includes(c));

    if (s === 'name') filtered.sort((a,b) => a.name.localeCompare(b.name));
    else if (s === 'size') filtered.sort((a,b) => b.size_kb - a.size_kb);
    else filtered.sort((a,b) => b.date.localeCompare(a.date));

    render(filtered);
}}

render(reports);
</script>
</body>
</html>"""
    OUTPUT.write_text(html)
    print(f"✅ index.html 已生成: {len(reports)} 份报告, {len(all_countries)} 个国家")

if __name__ == "__main__":
    generate()
