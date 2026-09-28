#!/usr/bin/env python3
"""
graph_builder.py — AST Parsing and Structural Dependency Graph Engine

Mined from PyGraphify / AST Code Review Graphs.
Scans Python and JavaScript/TypeScript files in target directories,
parses syntactic trees (AST), extracts imports, definitions, and call dependencies,
and outputs deterministic graph structures in JSON or Markdown.

Usage:
    python3 graph_builder.py --dir /path/to/repo --output graph.json
    python3 graph_builder.py --file /path/to/file.py --format md
"""

import ast
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Set


class PythonASTVisitor(ast.NodeVisitor):
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.imports: List[str] = []
        self.classes: Dict[str, Dict[str, Any]] = {}
        self.functions: List[str] = []
        self.calls: Set[str] = set()

    def visit_Import(self, node: ast.Import):
        for alias in node.names:
            self.imports.append(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        module = node.module or ""
        for alias in node.names:
            full_import = f"{module}.{alias.name}" if module else alias.name
            self.imports.append(full_import)
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef):
        bases = []
        for base in node.bases:
            if isinstance(base, ast.Name):
                bases.append(base.id)
            elif isinstance(base, ast.Attribute):
                bases.append(f"{getattr(base.value, 'id', '')}.{base.attr}")
        self.classes[node.name] = {
            "bases": bases,
            "line": node.lineno,
            "methods": [n.name for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
        }
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.functions.append(node.name)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self.functions.append(node.name)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        if isinstance(node.func, ast.Name):
            self.calls.add(node.func.id)
        elif isinstance(node.func, ast.Attribute):
            self.calls.add(node.func.attr)
        self.generic_visit(node)


def parse_python_file(filepath: Path) -> Dict[str, Any]:
    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(content, filename=str(filepath))
        visitor = PythonASTVisitor(str(filepath))
        visitor.visit(tree)
        lines = content.splitlines()
        return {
            "path": str(filepath),
            "language": "python",
            "loc": len(lines),
            "imports": sorted(list(set(visitor.imports))),
            "classes": visitor.classes,
            "functions": sorted(visitor.functions),
            "calls": sorted(list(visitor.calls)),
            "status": "parsed"
        }
    except Exception as exc:
        return {
            "path": str(filepath),
            "language": "python",
            "error": str(exc),
            "status": "error"
        }


def parse_js_ts_file(filepath: Path) -> Dict[str, Any]:
    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
        lines = content.splitlines()
        
        # Regex heuristics for ESM / CommonJS imports
        import_patterns = [
            r'import\s+.*?from\s+[\'"](.*?)[\'"]',
            r'require\(\s*[\'"](.*?)[\'"]\s*\)',
            r'import\(\s*[\'"](.*?)[\'"]\s*\)'
        ]
        imports = []
        for pat in import_patterns:
            imports.extend(re.findall(pat, content))

        # Functions & Classes regex
        functions = re.findall(r'(?:function\s+([a-zA-Z0-9_$]+)|const\s+([a-zA-Z0-9_$]+)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>)', content)
        fn_names = [f[0] or f[1] for f in functions if (f[0] or f[1])]

        classes = re.findall(r'class\s+([a-zA-Z0-9_$]+)(?:\s+extends\s+([a-zA-Z0-9_$]+))?', content)
        class_dict = {c[0]: {"bases": [c[1]] if c[1] else []} for c in classes}

        return {
            "path": str(filepath),
            "language": "javascript/typescript",
            "loc": len(lines),
            "imports": sorted(list(set(imports))),
            "classes": class_dict,
            "functions": sorted(fn_names),
            "calls": [],
            "status": "parsed"
        }
    except Exception as exc:
        return {
            "path": str(filepath),
            "language": "javascript/typescript",
            "error": str(exc),
            "status": "error"
        }


def build_dependency_graph(root_dir: Path) -> Dict[str, Any]:
    graph: Dict[str, Any] = {
        "root": str(root_dir.resolve()),
        "nodes": {},
        "edges": [],
        "metrics": {
            "total_files": 0,
            "total_loc": 0,
            "languages": {}
        }
    }

    supported_extensions = {
        ".py": parse_python_file,
        ".js": parse_js_ts_file,
        ".jsx": parse_js_ts_file,
        ".ts": parse_js_ts_file,
        ".tsx": parse_js_ts_file,
    }

    for path in root_dir.rglob("*"):
        if any(part.startswith(".") or part in ("node_modules", "__pycache__", "venv", "dist", "build") for part in path.parts):
            continue
        if path.is_file() and path.suffix in supported_extensions:
            parser_fn = supported_extensions[path.suffix]
            parsed_data = parser_fn(path)
            rel_path = str(path.relative_to(root_dir))
            graph["nodes"][rel_path] = parsed_data
            
            graph["metrics"]["total_files"] += 1
            loc = parsed_data.get("loc", 0)
            graph["metrics"]["total_loc"] += loc
            lang = parsed_data.get("language", "unknown")
            graph["metrics"]["languages"][lang] = graph["metrics"]["languages"].get(lang, 0) + 1

            for imp in parsed_data.get("imports", []):
                graph["edges"].append({
                    "source": rel_path,
                    "target": imp,
                    "type": "import"
                })

    return graph


def format_markdown(graph: Dict[str, Any]) -> str:
    md = []
    md.append(f"# AST Dependency Graph Report")
    md.append(f"**Root Directory:** `{graph['root']}`  ")
    md.append(f"**Total Files:** {graph['metrics']['total_files']} | **Total LOC:** {graph['metrics']['total_loc']}\n")
    
    md.append("## Languages")
    for lang, count in graph['metrics']['languages'].items():
        md.append(f"- **{lang}**: {count} files")
    md.append("")

    md.append("## Modules & Topologies")
    md.append("| File Path | Language | LOC | Classes | Functions | Direct Imports |")
    md.append("| :--- | :--- | :--- | :--- | :--- | :--- |")
    for path, data in sorted(graph["nodes"].items()):
        if data.get("status") == "error":
            md.append(f"| `{path}` | Error | - | - | - | `{data.get('error')}` |")
            continue
        classes_str = ", ".join(data.get("classes", {}).keys()) or "-"
        funcs_count = len(data.get("functions", []))
        imports_count = len(data.get("imports", []))
        md.append(f"| `{path}` | {data.get('language')} | {data.get('loc')} | {classes_str} | {funcs_count} | {imports_count} |")

    return "\n".join(md)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="AST Code Review Graph Generator")
    parser.add_argument("--dir", type=str, default=".", help="Root directory to scan")
    parser.add_argument("--file", type=str, default=None, help="Single file to scan")
    parser.add_argument("--output", type=str, default=None, help="Output file path")
    parser.add_argument("--format", type=str, choices=["json", "md"], default="json", help="Output format")

    args = parser.parse_args()

    if args.file:
        target_path = Path(args.file)
        if not target_path.exists():
            sys.stderr.write(f"Error: File not found: {args.file}\n")
            sys.exit(1)
        suffix = target_path.suffix
        if suffix == ".py":
            result = parse_python_file(target_path)
        else:
            result = parse_js_ts_file(target_path)
        output_data = json.dumps(result, indent=2) if args.format == "json" else f"```json\n{json.dumps(result, indent=2)}\n```"
    else:
        root_dir = Path(args.dir)
        if not root_dir.is_dir():
            sys.stderr.write(f"Error: Directory not found: {args.dir}\n")
            sys.exit(1)
        graph = build_dependency_graph(root_dir)
        if args.format == "md":
            output_data = format_markdown(graph)
        else:
            output_data = json.dumps(graph, indent=2)

    if args.output:
        Path(args.output).write_text(output_data, encoding="utf-8")
        print(f"Graph written to {args.output}")
    else:
        print(output_data)

    sys.exit(0)


if __name__ == "__main__":
    main()
