# Fix: guard against empty commit history
def analyze_repo(path):
    commits = get_commits(path)
    if not commits:
        print("No commits found in repository")
        return {"authors": {}, "total_commits": 0, "files": {}}
    # ... rest of analysis
    return analyze_commits(commits)
