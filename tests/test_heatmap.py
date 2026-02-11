"""Tests for heatmap."""
import os, tempfile
from gitwho.heatmap import generate_heatmap

def test_generate_html():
    data = {'files': {'a.py': {'Alice': 100, 'Bob': 20}, 'b.py': {'Bob': 50}},
        'authors': {'Alice': {'files':1,'lines':100,'sole_owner':0}, 'Bob': {'files':2,'lines':70,'sole_owner':1}},
        'total_files': 2, 'total_lines': 170}
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, 'test.html')
        generate_heatmap(data, out)
        content = open(out).read()
        assert 'Alice' in content
        assert 'Bob' in content
        assert 'a.py' in content
