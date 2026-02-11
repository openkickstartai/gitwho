"""Tests."""
import json
from gitwho.json_output import format_json

def test_basic():
    d = {"files":{"a.py":{"Alice":100}}, "authors":{"Alice":{"files":1,"lines":100,"sole_owner":1}},
        "total_files":1, "total_lines":100}
    r = json.loads(format_json(d))
    assert r["summary"]["total_files"] == 1
    assert r["authors"][0]["pct"] == 100.0

def test_empty():
    d = {"files":{}, "authors":{}, "total_files":0, "total_lines":0}
    r = json.loads(format_json(d))
    assert r["authors"] == []
