#!/usr/bin/env python3
"""
scaffold.py
Scaffold agent folders in docs/lv1 and/or docs/lv2 (defaults to both).
Creates: assets/, index.md, lab-guide.md
Also updates mkdocs.yml navigation and docs/lv1/index.md or docs/lv2/index.md.
"""
import argparse
import sys
import re
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - informative runtime behavior
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


def title_from_name(agent_name: str) -> str:
    return agent_name.replace("-", " ").title()


def update_mkdocs_nav(project_root: Path, level: str, agent_name: str, display_name: str, force: bool) -> None:
    mkdocs_path = project_root / "mkdocs.yml"
    data = yaml.safe_load(mkdocs_path.read_text(encoding="utf-8")) or {}
    nav = data.get("nav", [])

    section_label = "Agent Builder" if level == "lv1" else "Copilot Studio"
    subpath = f"{level}/{agent_name}/index.md"

    # Find or create section
    section = None
    for item in nav:
        if isinstance(item, dict) and section_label in item:
            section = item[section_label]
            break
    if section is None:
        section = []
        nav.append({section_label: section})

    # Check if entry exists
    for entry in section:
        if isinstance(entry, dict) and display_name in entry:
            existing_path = entry[display_name]
            if existing_path == subpath:
                print(f"mkdocs.yml: entry for '{display_name}' already present under '{section_label}'")
                data["nav"] = nav
                mkdocs_path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
                return
            if force:
                entry[display_name] = subpath
                print(f"mkdocs.yml: updated '{display_name}' path to {subpath}")
                data["nav"] = nav
                mkdocs_path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
                return
            else:
                print(f"mkdocs.yml: entry for '{display_name}' exists with different path. Use --force to overwrite.")
                return

    # Append new entry
    section.append({display_name: subpath})
    data["nav"] = nav
    mkdocs_path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    print(f"mkdocs.yml: added '{display_name}' under '{section_label}'")


def update_level_index(project_root: Path, level: str, agent_name: str, display_name: str) -> None:
    index_path = project_root / "docs" / level / "index.md"
    if not index_path.exists():
        print(f"WARNING: {index_path} does not exist, skipping index update.")
        return

    version_tag = "v1" if level == "lv1" else "v2"
    bullet = f"- **[{display_name} · {version_tag}]({agent_name}/index.md)**"

    content = index_path.read_text(encoding="utf-8")
    # Avoid duplicate lines
    if re.search(rf"\*\[{re.escape(display_name)}\s·\s{version_tag}\]", content):
        print(f"{index_path.name}: entry for '{display_name} · {version_tag}' already exists, skipping.")
        return

    # Append bullet at the end with a newline
    if not content.endswith("\n"):
        content += "\n"
    content += f"{bullet}\n"
    index_path.write_text(content, encoding="utf-8")
    print(f"Updated {index_path.relative_to(project_root)}: added {display_name} · {version_tag}")


# New: central, easy-to-edit default index template
def default_index_template() -> str:
    """
    Built-in minimal index.md template used for newly created agents.
    Edit this function to change the default template in the future.
    Placeholders: {{AGENT_NAME}}, {{DISPLAY_NAME}}, {{VERSION_TAG}}
    """
    return (
        "# {{DISPLAY_NAME}} · {{VERSION_TAG}}\n\n"
        "## Overview\n"
        "Placeholder overview for the {{DISPLAY_NAME}}.\n\n"
        "## What this version demonstrates\n"
        "- Search on SharePoint knowledge\n"
        "- Job post generation via instructions\n\n"
        "## Built with\n"
        "- Copilot Studio Lite (Agent Builder)\n\n"
        "## Get started\n"
        "→ **[Open the lab guide](lab-guide.md)**\n\n"
        "## Next\n"
        "→ **[{{DISPLAY_NAME}} · next version](../../lv2/{{AGENT_NAME}}/index.md)**\n"
    )


def apply_index_template(project_root: Path, base: Path, level: str, agent_name: str, display_name: str) -> None:
    tpl = default_index_template()
    version_tag = "v1" if level == "lv1" else "v2"
    content = tpl.replace("{{AGENT_NAME}}", agent_name).replace("{{DISPLAY_NAME}}", display_name).replace("{{VERSION_TAG}}", version_tag)
    index_path = base / "index.md"
    index_path.write_text(content, encoding="utf-8")
    print(f"Populated template into {index_path.relative_to(project_root)}")


def scaffold_agent(agent_name: str, levels: list[str], force: bool) -> None:
    """Create agent structure for specified levels."""
    # Get project root (parent of tools/ directory)
    project_root = Path(__file__).resolve().parent.parent
    display_name = title_from_name(agent_name)

    for level in levels:
        base = project_root / "docs" / level / agent_name

        # Create assets directory
        (base / "assets").mkdir(parents=True, exist_ok=True)

        # index.md: populate with built-in template
        index_path = base / "index.md"
        if index_path.exists():
            if force:
                apply_index_template(project_root, base, level, agent_name, display_name)
                print(f"Overwritten: {index_path.relative_to(project_root)}")
            else:
                print(f"Skipping existing file: {index_path.relative_to(project_root)}")
        else:
            base.mkdir(parents=True, exist_ok=True)
            apply_index_template(project_root, base, level, agent_name, display_name)
            print(f"Created: {index_path.relative_to(project_root)}")

        # lab-guide.md (skip or overwrite depending on force)
        lab_path = base / "lab-guide.md"
        if lab_path.exists():
            if force:
                lab_path.write_text("", encoding="utf-8")
                print(f"Overwritten: {lab_path.relative_to(project_root)}")
            else:
                print(f"Skipping existing file: {lab_path.relative_to(project_root)}")
        else:
            lab_path.write_text("", encoding="utf-8")
            print(f"Created: {lab_path.relative_to(project_root)}")

        # Update mkdocs.yml nav for this level
        update_mkdocs_nav(project_root, level, agent_name, display_name, force)

        # Update the level index page (e.g., docs/lv1/index.md)
        update_level_index(project_root, level, agent_name, display_name)


def main():
    parser = argparse.ArgumentParser(description="Scaffold agent in docs/lv1 and/or docs/lv2")
    parser.add_argument("name", help="Agent folder name (e.g., hr-assistant)")
    parser.add_argument("--lv1", action="store_true", help="Create only in lv1")
    parser.add_argument("--lv2", action="store_true", help="Create only in lv2")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    # Determine which levels to create
    levels = []
    if args.lv1:
        levels.append("lv1")
    if args.lv2:
        levels.append("lv2")
    if not levels:
        levels = ["lv1", "lv2"]

    scaffold_agent(args.name, levels, args.force)


if __name__ == "__main__":
    main()