#!/usr/bin/env python3
"""Migrate legacy Cappuccino website source tree into a complete Hugo site skeleton."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

BLOG_RE = re.compile(r"^(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.+?)(?:\.html)?\.markdown$")
MD_SUFFIX_RE = re.compile(r"(?:\.html)?\.markdown$")
IMG_REF_RE = re.compile(r"""(?:src=["']|\]\()(?P<url>(?:/?img/|cpo-uploads/)[^"')\s]+)""")
RAW_HTML_TAG_RE = re.compile(r"<(?:div|span|table|iframe|script|style|object|embed)\b", re.IGNORECASE)

DEFAULT_HUGO_TOML = """baseURL = "https://cappuccino.dev/"
language.Locale = "en-us"
title = "Cappuccino"

[params]
description = "Objective-J, Foundation, and AppKit for the web."

[menu]
    [[menu.main]]
        name = "Learn"
        url = "/learn/"
        weight = 10
    [[menu.main]]
        name = "Blog"
        url = "/blog/"
        weight = 20
    [[menu.main]]
        name = "Support"
        url = "/support/"
        weight = 30
    [[menu.main]]
        name = "Contribute"
        url = "/contribute/"
        weight = 40
"""

BASEOF_HTML = """<!DOCTYPE html>
<html lang="{{ Site.Language.Locale | default "en" }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ if .IsHome }}{{ site.Title }}{{ else }}{{ .Title }} — {{ site.Title }}{{ end }}</title>
    <link rel="stylesheet" href="/css/site.css">
</head>
<body>
    <header>
        <a href="/">{{ site.Title }}</a>
        <nav aria-label="Primary">
            <ul>
                {{- range site.Menus.main }}
                    <li><a href="{{ .URL }}">{{ .Name }}</a></li>
                {{- end }}
            </ul>
        </nav>
    </header>

    <main>
        {{ block "main" . }}{{ end }}
    </main>

    <footer>
        <p>{{ site.Title }}</p>
    </footer>
</body>
</html>
"""

HOME_HTML = """{{ define "main" }}
    <article>
        <h1>{{ .Title | default site.Title }}</h1>
        {{ .Content }}
    </article>
{{ end }}
"""

SINGLE_HTML = """{{ define "main" }}
    <article>
        <header>
            <h1>{{ .Title }}</h1>
            {{- with .Date }}
                <time datetime="{{ .Format "2006-01-02" }}">{{ .Format "January 2, 2006" }}</time>
            {{- end }}
        </header>
        {{ .Content }}
    </article>
{{ end }}
"""

LIST_HTML = """{{ define "main" }}
    <section>
        <header>
            <h1>{{ .Title }}</h1>
            {{ .Content }}
        </header>
        <ul>
            {{- range .Pages }}
                <li>
                    <a href="{{ .RelPermalink }}">{{ .Title }}</a>
                    {{- with .Date }}
                        <time datetime="{{ .Format "2006-01-02" }}">{{ .Format "2006-01-02" }}</time>
                    {{- end }}
                </li>
            {{- end }}
        </ul>
    </section>
{{ end }}
"""

BASELINE_CSS = """/* Bottom-up baseline stylesheet; refine layout and surface tokens incrementally. */
"""


def split_front_matter(text: str) -> tuple[str | None, str]:
        """Return (yaml_block_without_fences, body) if YAML front matter is present."""
        if not text.startswith("---\n") and not text.startswith("---\r\n"):
                return None, text
    
        lines = text.splitlines(keepends=True)
        for idx in range(1, len(lines)):
                if lines[idx].strip() == "---":
                        fm = "".join(lines[1:idx]).rstrip("\r\n")
                        body = "".join(lines[idx + 1 :])
                        return fm, body
        return None, text


def has_key(fm: str | None, key: str) -> bool:
        if not fm:
                return False
        return re.search(rf"^{re.escape(key)}\s*:", fm, flags=re.MULTILINE) is not None


def yaml_quote(value: str) -> str:
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'


def build_front_matter(
        existing_fm: str | None,
        date_str: str | None,
        aliases: list[str],
) -> str:
        """Normalize front matter into a clean YAML block."""
        parts: list[str] = []
        if existing_fm and existing_fm.strip():
                parts.append(existing_fm.strip())
            
        if date_str and not has_key(existing_fm, "date"):
                parts.append(f"date: {date_str}")
            
        if aliases and not has_key(existing_fm, "aliases"):
                formatted = ", ".join(yaml_quote(a) for a in aliases)
                parts.append(f"aliases: [{formatted}]")
            
        if not parts:
                return ""
        return "---\n" + "\n".join(parts) + "\n---\n\n"


def copy_file(src: Path, dst: Path, dry_run: bool) -> None:
        if dry_run:
                return
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    
    
def write_text(dst: Path, content: str, dry_run: bool, overwrite: bool = True) -> bool:
        if not overwrite and dst.exists():
                return False
        if dry_run:
                return True
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(content, encoding="utf-8")
        return True


def scaffold_hugo_site(dst_root: Path, dry_run: bool, force_scaffold: bool) -> int:
        """Create root hugo.toml, _index.md home entry point, layouts, and base CSS."""
        scaffold_files: list[tuple[Path, str]] = [
                (dst_root / "hugo.toml", DEFAULT_HUGO_TOML),
                (dst_root / "content" / "_index.md", "---\ntitle: \"Cappuccino\"\n---\n"),
                (dst_root / "layouts" / "_default" / "baseof.html", BASEOF_HTML),
                (dst_root / "layouts" / "index.html", HOME_HTML),
                (dst_root / "layouts" / "_default" / "single.html", SINGLE_HTML),
                (dst_root / "layouts" / "_default" / "list.html", LIST_HTML),
                (dst_root / "static" / "css" / "site.css", BASELINE_CSS),
        ]
        created = 0
        for path, content in scaffold_files:
                if write_text(path, content, dry_run=dry_run, overwrite=force_scaffold):
                        created += 1
        return created


def migrate(
        src_root: Path,
        dst_root: Path,
        bundle_blog: bool,
        dry_run: bool,
        force_scaffold: bool,
) -> int:
        source_dir = src_root / "source"
        if not source_dir.is_dir():
                print(f"error: missing source directory: {source_dir}", file=sys.stderr)
                return 1
    
        notes: list[str] = []
        migrated_md = 0
        copied_assets = 0
    
        scaffold_count = scaffold_hugo_site(dst_root, dry_run=dry_run, force_scaffold=force_scaffold)
    
        # 1. Data files
        data_dir = src_root / "data"
        if data_dir.is_dir():
                for item in sorted(data_dir.rglob("*")):
                        if item.is_file():
                                copy_file(item, dst_root / "data" / item.relative_to(data_dir), dry_run)
                                copied_assets += 1
                            
        # 2. Static assets (img, downloads, learn/files)
        asset_mappings = [
                (source_dir / "img", dst_root / "static" / "img"),
                (source_dir / "downloads", dst_root / "static" / "downloads"),
                (source_dir / "learn" / "files", dst_root / "static" / "learn" / "files"),
        ]
        for a_src, a_dst in asset_mappings:
                if not a_src.is_dir():
                        continue
                for item in sorted(a_src.rglob("*")):
                        if item.is_file():
                                copy_file(item, a_dst / item.relative_to(a_src), dry_run)
                                copied_assets += 1
                            
        # 3. Markdown content (blog + sections/pages)
        for md_path in sorted(source_dir.rglob("*.markdown*")):
                if not md_path.is_file():
                        continue
            
                rel = md_path.relative_to(source_dir)
            
                if rel.parts and rel.parts[0] in {"img", "downloads"}:
                        continue
                if len(rel.parts) >= 2 and rel.parts[:2] == ("learn", "files"):
                        continue
            
                if md_path.suffix == ".erb":
                        notes.append(f"[ERB] {rel} -> requires manual template/content review")
                        continue
            
                m_blog = BLOG_RE.match(md_path.name) if rel.parts and rel.parts[0] == "blog" else None
                aliases: list[str] = []
                date_str: str | None = None
            
                if m_blog:
                        date_str = m_blog.group("date")
                        slug = m_blog.group("slug")
                        aliases.append(f"/blog/{date_str.replace('-', '/')}/{slug}.html")
                        out_rel = Path("blog") / slug / "index.md" if bundle_blog else Path("blog") / f"{date_str}-{slug}.md"
                else:
                        norm_name = MD_SUFFIX_RE.sub(".md", md_path.name)
                        parent_parts = rel.parent.parts
                        if norm_name == "index.md" and parent_parts != (".",):
                                out_rel = Path(*parent_parts) / "_index.md"
                        else:
                                out_rel = Path(*parent_parts, norm_name) if parent_parts != (".",) else Path(norm_name)
                            
                raw = md_path.read_text(encoding="utf-8", errors="replace")
                fm, body = split_front_matter(raw)
                new_fm = build_front_matter(fm, date_str, aliases)
                write_text(dst_root / "content" / out_rel, new_fm + body, dry_run=dry_run, overwrite=True)
                migrated_md += 1
            
                if RAW_HTML_TAG_RE.search(body):
                        notes.append(f"[HTML] {rel} -> contains raw HTML tags; audit for semantic/CSS cleanup")
                    
                img_matches = sorted({m.group("url") for m in IMG_REF_RE.finditer(body)})
                if img_matches:
                        preview = ", ".join(img_matches[:4])
                        extra = f" (+{len(img_matches) - 4} more)" if len(img_matches) > 4 else ""
                        notes.append(f"[IMG] {rel} -> {preview}{extra}")
                    
        print(f"Hugo scaffold files written: {scaffold_count}")
        print(f"Markdown files migrated: {migrated_md}")
        print(f"Data & static files copied: {copied_assets}")
        print(f"Follow-up audit items: {len(notes)}")
        for note in notes:
                print(f"  {note}")
            
        return 0


def main() -> int:
        parser = argparse.ArgumentParser(description="Migrate legacy site into a ready Hugo skeleton.")
        parser.add_argument("source_repo", type=Path, help="Path to cloned legacy repo root")
        parser.add_argument("target_hugo", type=Path, help="Path to Hugo destination directory")
        parser.add_argument(
                "--bundle-blog",
                action="store_true",
                help="Emit blog posts as page bundles (content/blog/<slug>/index.md)",
        )
        parser.add_argument(
                "--force-scaffold",
                action="store_true",
                help="Overwrite existing hugo.toml, layouts, and starter files in target_hugo",
        )
        parser.add_argument(
                "--dry-run",
                action="store_true",
                help="Scan and report without writing files",
        )
        args = parser.parse_args()
        return migrate(
                args.source_repo.resolve(),
                args.target_hugo.resolve(),
                args.bundle_blog,
                args.dry_run,
                args.force_scaffold,
        )
        

if __name__ == "__main__":
        raise SystemExit(main())
    
