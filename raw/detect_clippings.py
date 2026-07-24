#!/usr/bin/env python3
"""Detect incoming Obsidian Clipper files in the wiki vault root."""
import os, json, re, time

VAULT = os.path.expanduser("~/workspace/kate-home-healthcare")
KNOWN_FILE = os.path.join(VAULT, "raw", ".known_clipper_files.json")

# Files that are intentionally in the vault root (not clippings)
CORE_FILES = {
    "Home.md", "SCHEMA.md", "index.md", "log.md", "Updates.md",
    "config.yaml", ".gitkeep",
}

def get_md_roots():
    """Return set of .md filenames currently in vault root."""
    return {
        f for f in os.listdir(VAULT)
        if f.endswith(".md") and os.path.isfile(os.path.join(VAULT, f))
    }

def has_clipper_frontmatter(path):
    """Check if file has frontmatter indicating it's a Clipper capture."""
    try:
        with open(path) as f:
            head = f.read(2000)
    except Exception:
        return False
    if not head.startswith("---"):
        return False
    # Clipper files typically have source_url, source, or clipping_id
    markers = ["source_url:", "source:", "clipping_id:", "source_updated:"]
    for m in markers:
        if m in head:
            return True
    # Also catch files with auto-generated Obsidian Clipper title patterns
    return False

def load_known():
    if os.path.exists(KNOWN_FILE):
        with open(KNOWN_FILE) as f:
            return set(json.load(f))
    return set()

def save_known(files):
    os.makedirs(os.path.dirname(KNOWN_FILE), exist_ok=True)
    with open(KNOWN_FILE, 'w') as f:
        json.dump(sorted(files), f)

def main():
    known = load_known()
    current = get_md_roots()
    
    # New files = in current but not in known AND not in CORE_FILES
    new_files = (current - known) - CORE_FILES
    
    clippings = []
    for fname in sorted(new_files):
        fpath = os.path.join(VAULT, fname)
        if has_clipper_frontmatter(fpath):
            stat = os.stat(fpath)
            clippings.append({
                "filename": fname,
                "path": fpath,
                "size": stat.st_size,
                "mtime": stat.st_mtime,
            })
    
    # Save current state for next run
    save_known(current)
    
    # Output JSON for cron consumption
    print(json.dumps({"clippings": clippings, "total": len(clippings)}, indent=2))

if __name__ == "__main__":
    main()
