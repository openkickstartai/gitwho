"""Tests for analyzer."""
import os, tempfile, subprocess
from gitwho.analyzer import analyze_repo, _list_tracked

def _mk_repo(tmp):
    subprocess.run(["git","init",tmp], capture_output=True)
    subprocess.run(["git","-C",tmp,"config","user.email","t@t.com"], capture_output=True)
    subprocess.run(["git","-C",tmp,"config","user.name","Tester"], capture_output=True)
    open(os.path.join(tmp,"a.py"),"w").write("print(1)\nprint(2)\n")
    subprocess.run(["git","-C",tmp,"add","."], capture_output=True)
    subprocess.run(["git","-C",tmp,"commit","-m","init"], capture_output=True)

def test_list_tracked():
    with tempfile.TemporaryDirectory() as t:
        _mk_repo(t)
        assert "a.py" in _list_tracked(t)

def test_analyze():
    with tempfile.TemporaryDirectory() as t:
        _mk_repo(t)
        d = analyze_repo(t)
        assert d["total_files"] == 1
        assert "Tester" in d["authors"]

def test_not_repo():
    with tempfile.TemporaryDirectory() as t:
        try: analyze_repo(t); assert False
        except ValueError: pass
