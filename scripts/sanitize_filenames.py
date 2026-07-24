#!/usr/bin/env python3
"""Clean invalid characters from filenames in the Clippings directory.
Runs as cron watchdog — silent when nothing to fix."""

import os
import re
import sys

VAULT = "/Users/kennethye/workspace/kate-home-healthcare"
CLIPPINGS_DIR = os.path.join(VAULT, "Clippings")

# Characters banned on Windows NTFS + most cloud sync services
INVALID_CHARS = r'[?*:<>|"]'
# Replace with
REPLACEMENT = "—"  # em dash — safe, readable, won't conflict with hyphens in titles


def sanitize(name: str) -> str:
    """Replace invalid filename characters + strip trailing spaces/dots."""
    cleaned = re.sub(INVALID_CHARS, REPLACEMENT, name)
    # Strip from stem (handles "stem .md" -> "stem.md")
    stem, ext = os.path.splitext(cleaned)
    stem = stem.rstrip(". ")
    cleaned = stem + ext
    # Also strip from very end (handles "stem." -> "stem", "stem " -> "stem")
    cleaned = cleaned.rstrip(". ")
    return cleaned


def main():
    if not os.path.isdir(CLIPPINGS_DIR):
        print(f"[SKIP] Clippings dir not found: {CLIPPINGS_DIR}")
        sys.exit(0)

    fixed = 0
    for fname in os.listdir(CLIPPINGS_DIR):
        safe = sanitize(fname)
        if safe != fname:
            old_path = os.path.join(CLIPPINGS_DIR, fname)
            new_path = os.path.join(CLIPPINGS_DIR, safe)
            # Avoid overwriting existing file
            if os.path.exists(new_path):
                base, ext = os.path.splitext(safe)
                safe = f"{base}_renamed{ext}"
                new_path = os.path.join(CLIPPINGS_DIR, safe)
            os.rename(old_path, new_path)
            print(f"[FIXED] {fname!r} → {safe!r}")
            fixed += 1

    if fixed == 0:
        # SILENT — no output = no cron delivery
        pass
    else:
        print(f"[DONE] {fixed} file(s) renamed.")


if __name__ == "__main__":
    main()
