#!/usr/bin/env bash

# Bash safe mode
set -euo pipefail

# For each file in source/blog/ that has a .markdown or .md extension, run it through the frontmatter fixer and
# replace the original file with the fixed version. This script is intended to be run from the root of the repository.

for file in source/blog/*.markdown source/blog/*.md; do
    ./tools/fix_frontmatter.py <"$file" >"$file.tmp"
    # if nothing but whitespace changed, continue
    if diff -q "$file" "$file.tmp" > /dev/null; then
        rm "$file.tmp"
        continue
    fi

    # Print the difference
    echo "Fixing $file"
    # diff -u "$file" "$file.tmp"
    mv "$file.tmp" "$file"
done
