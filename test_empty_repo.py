import pytest
import tempfile, os, subprocess

def test_empty_repo_no_crash():
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(['git', 'init'], cwd=tmp, capture_output=True)
        result = analyze_repo(tmp)
        assert result['total_commits'] == 0
        assert result['authors'] == {}

def test_single_commit_repo():
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(['git', 'init'], cwd=tmp, capture_output=True)
        subprocess.run(['git', 'config', 'user.email', 'test@test.com'], cwd=tmp, capture_output=True)
        subprocess.run(['git', 'config', 'user.name', 'Test'], cwd=tmp, capture_output=True)
        open(os.path.join(tmp, 'README.md'), 'w').write('# Test')
        subprocess.run(['git', 'add', '.'], cwd=tmp, capture_output=True)
        subprocess.run(['git', 'commit', '-m', 'init'], cwd=tmp, capture_output=True)
        result = analyze_repo(tmp)
        assert result['total_commits'] == 1
