"""JSON output."""
import json

def format_json(data, indent=2):
    out = {"summary": {"total_files": data["total_files"], "total_lines": data["total_lines"],
        "authors": len(data["authors"])},
        "authors": [{"name": n, "files": s["files"], "lines": s["lines"],
            "sole_owner": s["sole_owner"],
            "pct": round(s["lines"]/max(data["total_lines"],1)*100,1)}
            for n,s in sorted(data["authors"].items(), key=lambda x:-x[1]["lines"])]}
    return json.dumps(out, indent=indent)
