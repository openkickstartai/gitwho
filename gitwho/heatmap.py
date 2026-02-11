"""HTML heatmap generator."""
import json
from typing import Dict

HTML_TEMPLATE = '''<!DOCTYPE html>
<html><head><title>gitwho ownership</title>
<style>
body {{ font-family: monospace; margin: 20px; background: #1a1a2e; color: #eee; }}
.file {{ display: inline-block; margin: 2px; padding: 8px; border-radius: 4px; cursor: pointer; }}
.file:hover {{ opacity: 0.8; }}
h1 {{ color: #e94560; }}
.legend {{ margin: 20px 0; }}
.legend span {{ display: inline-block; padding: 4px 12px; margin: 2px; border-radius: 3px; }}
</style></head>
<body><h1>Code Ownership Heatmap</h1>
<div class="legend">{legend}</div>
<div>{files}</div>
<p>{summary}</p></body></html>'''

COLORS = ['#e94560','#0f3460','#16213e','#533483','#2b9348','#e07c24','#3a86ff','#8338ec']

def generate_heatmap(data: Dict, output: str = 'ownership.html'):
    authors = list(data['authors'].keys())
    color_map = {a: COLORS[i % len(COLORS)] for i, a in enumerate(authors)}
    legend = ''.join(f'<span style="background:{color_map[a]}">{a}</span>' for a in authors)
    files_html = []
    for fname, contribs in sorted(data['files'].items()):
        primary = max(contribs, key=contribs.get)
        size = sum(contribs.values())
        w = max(60, min(200, size * 2))
        tip = ', '.join(f'{a}: {n}' for a, n in contribs.items())
        files_html.append(f'<div class="file" style="background:{color_map[primary]};width:{w}px" title="{fname}: {tip}">{fname.split("/")[-1]}</div>')
    summary = f"{data['total_files']} files, {data['total_lines']} lines, {len(authors)} authors"
    html = HTML_TEMPLATE.format(legend=legend, files=''.join(files_html), summary=summary)
    with open(output, 'w') as f:
        f.write(html)
    return output
