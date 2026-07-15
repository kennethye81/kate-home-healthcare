#!/usr/bin/env python3
"""批量 Markdown → HTML 转换器。
用法: python3 batch_convert.py [--all]
"""
import subprocess, sys, os, json, time
from pathlib import Path

KB_ROOT = Path("/Users/kennethye/workspace/kate-kb")
REPORTS_DIR = KB_ROOT / "reports"
HTML_DIR = KB_ROOT / "html"
RENDER_SCRIPT = "/Users/kennethye/.hermes/profiles/kate-strategist/skills/sensenova/sn-md-to-html-report/scripts/render_report.py"

def convert_one(md_path: Path) -> dict:
    """转换单个 .md → .html"""
    html_path = HTML_DIR / md_path.with_suffix(".html").name
    cmd = [
        sys.executable, RENDER_SCRIPT,
        str(md_path), str(html_path),
        "--embed-images", "--with-js", "--title-style", "comfortable"
    ]
    start = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    elapsed = time.time() - start
    return {
        "file": md_path.name,
        "output": str(html_path),
        "elapsed": round(elapsed, 1),
        "success": r.returncode == 0 and html_path.exists(),
        "error": r.stderr[:200] if r.returncode != 0 else None
    }

def main():
    md_files = sorted(REPORTS_DIR.glob("*.md"))
    if not md_files:
        print("❌ 没有找到 .md 报告文件")
        return
    
    print(f"📄 {len(md_files)} 份报告待转换\n")
    
    results = []
    for i, md in enumerate(md_files):
        print(f"[{i+1}/{len(md_files)}] {md.name[:60]}...", end=" ", flush=True)
        r = convert_one(md)
        results.append(r)
        status = "✅" if r["success"] else f"❌ {r['error'][:50]}"
        print(f"{status} ({r['elapsed']}s)")
    
    # 汇总
    ok = sum(1 for r in results if r["success"])
    fail = len(results) - ok
    print(f"\n{'='*50}")
    print(f"✅ {ok} 成功 | ❌ {fail} 失败 | 总计 {len(results)}")
    
    # 记录到 index
    index_path = REPORTS_DIR / "index.json"
    existing = {}
    if index_path.exists():
        existing = json.loads(index_path.read_text())
    
    for r in results:
        name = r["file"]
        if name in existing:
            existing[name]["html"] = r["output"]
            existing[name]["converted_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    
    index_path.write_text(json.dumps(existing, ensure_ascii=False, indent=2))
    print(f"📋 index.json 已更新")

if __name__ == "__main__":
    main()
