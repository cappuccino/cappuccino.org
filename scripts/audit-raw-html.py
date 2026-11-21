#!/usr/bin/env python3
"""Audit Markdown content files for candidate raw HTML tags outside code spans."""

from __future__ import annotations

import pathlib
import re
import sys

HTML_TAGS: frozenset[str] = frozenset({
    "a", "abbr", "address", "area", "article", "aside", "audio",
    "b", "base", "bdi", "bdo", "blockquote", "body", "br", "button",
    "canvas", "caption", "cite", "code", "col", "colgroup",
    "data", "datalist", "dd", "del", "details", "dfn", "dialog", "div", "dl", "dt",
    "em", "embed",
    "fieldset", "figcaption", "figure", "footer", "form",
    "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html",
    "i", "iframe", "img", "input", "ins",
    "kbd",
    "label", "legend", "li", "link",
    "main", "map", "mark", "menu", "meta", "meter",
    "nav", "noscript",
    "object", "ol", "optgroup", "option", "output",
    "p", "param", "picture", "pre", "progress",
    "q",
    "rp", "rt", "ruby",
    "s", "samp", "script", "section", "select", "small", "source", "span",
    "strong", "style", "sub", "summary", "sup",
    "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead",
    "time", "title", "tr", "track",
    "u", "ul",
    "var", "video",
    "wbr",
})

FENCED_CODE_RE = re.compile(r"(?m)^(`{3,}|~{3,})[^\n]*\n.*?^\1[ \t]*$", re.DOTALL)
INLINE_CODE_RE = re.compile(r"(`+)([^\n]*?)\1")
TAG_RE = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9-]*)(?=\s|/?>)[^>]*>")


def strip_frontmatter(text: str) -> str:
    """Return content body after leading YAML or TOML frontmatter if present."""
    if text.startswith("---\n") or text.startswith("---\r\n"):
        parts = re.split(r"\r?\n---[ \t]*(?:\r?\n|$)", text, maxsplit=2)
        if len(parts) == 3:
            return parts[2]
    if text.startswith("+++\n") or text.startswith("+++\r\n"):
        parts = re.split(r"\r?\n\+\+\+[ \t]*(?:\r?\n|$)", text, maxsplit=2)
        if len(parts) == 3:
            return parts[2]
    return text


def scan_file(path: pathlib.Path) -> list[str]:
    """Return sorted distinct HTML tag tokens found in a Markdown file."""
    body = strip_frontmatter(path.read_text(encoding="utf-8"))
    without_fences = FENCED_CODE_RE.sub("", body)
    without_code = INLINE_CODE_RE.sub("", without_fences)

    found: set[str] = set()
    for match in TAG_RE.finditer(without_code):
        slash, raw_name = match.group(1), match.group(2).lower()
        if raw_name in HTML_TAGS:
            found.add(f"/{raw_name}" if slash else raw_name)
    return sorted(found)


def main(argv: list[str]) -> int:
    root = pathlib.Path(argv[1]) if len(argv) > 1 else pathlib.Path("content")
    if not root.is_dir():
        print(f"error: directory not found: {root}", file=sys.stderr)
        return 2

    matches = 0
    for path in sorted(root.rglob("*.md")):
        tags = scan_file(path)
        if tags:
            matches += 1
            print(f"{path}: {', '.join(tags)}")

    return 1 if matches else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
