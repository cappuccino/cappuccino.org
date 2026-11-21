#!/usr/bin/env python3
//  audit-frontmatter.py
//  
//
//  Created by David Richardson on 2026-11-21.
//


python3 -c '
import pathlib, re
for p in sorted(pathlib.Path("content").rglob("*.md")):
    lines = p.read_text(errors="replace").splitlines()
    if lines and lines[0].strip() == "---":
        seen = {}
        for i, line in enumerate(lines[1:], 2):
            if line.strip() == "---":
                break
            m = re.match(r"^([A-Za-z0-9_-]+)\s*:", line)
            if m:
                k = m.group(1)
                if k in seen:
                    print(f"{p}:{i}: duplicate key \"{k}\" (first at line {seen[k]})")
                seen.setdefault(k, i)
'
