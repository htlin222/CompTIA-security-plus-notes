#!/usr/bin/env python3
"""Add acronym aliases to concept note frontmatter."""

import re
import glob
import os

base = "/Users/htlin/CompTIA-security-plus-notes/content"
files = glob.glob(f"{base}/*/concepts/*.md")


def is_acronym(s):
    """Check if string looks like an acronym (mostly uppercase/digits, short)."""
    s = s.strip()
    parts = s.split("/")
    for part in parts:
        part = part.strip()
        if not part:
            return False
        upper_digit = sum(1 for c in part if c.isupper() or c.isdigit())
        lower = sum(1 for c in part if c.islower())
        if len(part) < 2:
            return False
        if upper_digit == 0:
            return False
        if len(part) > 8 and lower > upper_digit:
            return False
    return True


modified = 0
skipped_no_acronym = 0
skipped_no_paren = 0

for fpath in sorted(files):
    with open(fpath, "r") as f:
        content = f.read()

    if not content.startswith("---"):
        continue

    if "\naliases:" in content:
        continue

    title_match = re.search(r'^title:\s*"(.+?)"', content, re.MULTILINE)
    if not title_match:
        title_match = re.search(r"^title:\s*'(.+?)'", content, re.MULTILINE)
    if not title_match:
        continue

    title = title_match.group(1)

    paren_matches = re.findall(r"\(([^)]+)\)", title)
    if not paren_matches:
        skipped_no_paren += 1
        continue

    aliases = []

    for paren in paren_matches:
        paren_stripped = paren.strip()
        if is_acronym(paren_stripped):
            aliases.append(paren_stripped)

    # Check if title starts with acronym: "CSR (Certificate Signing Request)"
    prefix_match = re.match(r"^([A-Z][A-Za-z0-9/]+)\s*\(", title)
    if prefix_match:
        candidate = prefix_match.group(1)
        if is_acronym(candidate) and candidate not in aliases:
            aliases.append(candidate)

    if not aliases:
        skipped_no_acronym += 1
        continue

    # Deduplicate: add both as-is and uppercase version if different
    final_aliases = []
    for a in aliases:
        if a not in final_aliases:
            final_aliases.append(a)
        upper = a.upper()
        if upper != a and upper not in final_aliases:
            final_aliases.append(upper)

    # Build aliases yaml block
    aliases_block = "aliases:\n"
    for a in final_aliases:
        aliases_block += f"  - {a}\n"

    # Insert after tags block, before closing ---
    lines = content.split("\n")
    insert_idx = None
    in_frontmatter = False
    found_tags = False

    for i, line in enumerate(lines):
        if i == 0 and line.strip() == "---":
            in_frontmatter = True
            continue
        if in_frontmatter and line.strip() == "---":
            insert_idx = i
            break
        if line.startswith("tags:"):
            found_tags = True
        elif found_tags and line.startswith("  - "):
            pass
        elif found_tags and not line.startswith("  - "):
            insert_idx = i
            break

    if insert_idx is None:
        continue

    aliases_lines = aliases_block.rstrip("\n").split("\n")
    for j, al in enumerate(aliases_lines):
        lines.insert(insert_idx + j, al)

    new_content = "\n".join(lines)

    with open(fpath, "w") as f:
        f.write(new_content)

    modified += 1
    print(f"  {os.path.basename(fpath)}: {final_aliases}")

print(f"\nModified: {modified}")
print(f"Skipped (no parens): {skipped_no_paren}")
print(f"Skipped (no acronym in parens): {skipped_no_acronym}")
