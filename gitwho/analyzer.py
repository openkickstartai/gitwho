"""Core git analysis engine."""
import subprocess, os
from collections import defaultdict
from typing import Dict, List, Optional

def analyze_repo(path: str, max_depth: Optional[int] = None) -> Dict:
    if not os.path.isdir(os.path.join(path, ".git")):
        raise ValueError(f"{path} is not a git repository")
    files = _list_tracked(path)
    ownership = defaultdict(lambda: defaultdict(int))
    total_lines = defaultdict(int)
    for f in files:
        if max_depth and f.count("/") > max_depth: continue
        blame = _get_blame(path, f)
        for author, lines in blame.items():
            ownership[f][author] = lines
            total_lines[f] += lines
    authors = defaultdict(lambda: {"files":0,"lines":0,"sole_owner":0})
    for f, contribs in ownership.items():
        for author, lines in contribs.items():
            authors[author]["files"] += 1
            authors[author]["lines"] += lines
        if len(contribs) == 1:
            authors[list(contribs.keys())[0]]["sole_owner"] += 1
    return {"files": dict(ownership), "authors": dict(authors),
            "total_files": len(files), "total_lines": sum(total_lines.values())}

def _list_tracked(path):
    r = subprocess.run(["git","-C",path,"ls-files"], capture_output=True, text=True)
    return [f for f in r.stdout.strip().split("\n") if f]

def _get_blame(path, filepath):
    try:
        r = subprocess.run(["git","-C",path,"blame","--line-porcelain",filepath],
            capture_output=True, text=True, timeout=10)
        counts = defaultdict(int)
        for line in r.stdout.split("\n"):
            if line.startswith("author "): counts[line[7:].strip()] += 1
        return dict(counts)
    except: return {}
