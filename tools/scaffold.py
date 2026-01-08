#!/usr/bin/env python3
"""
scaffold.py
Scaffold agent folders in docs/lv1 and/or docs/lv2 (defaults to both).
Creates: assets/, index.md, lab-guide.md
"""
import argparse
import sys
from pathlib import Path

def scaffold_agent(agent_name: str, levels: list[str], force: bool) -> None:
    """Create agent structure for specified levels."""
    # Get project root (parent of tools/ directory)
    project_root = Path(__file__).resolve().parent.parent
    
    for level in levels:
        base = project_root / "docs" / level / agent_name
        
        # Create assets directory
        (base / "assets").mkdir(parents=True, exist_ok=True)
        
        # Create empty markdown files
        for filename in ["index.md", "lab-guide.md"]:
            filepath = base / filename
            if filepath.exists() and not force:
                print(f"ERROR: {filepath} already exists. Use --force to overwrite.", file=sys.stderr)
                sys.exit(1)
            filepath.write_text("", encoding="utf-8")
        
        print(f"Created: {base.relative_to(project_root)}")

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