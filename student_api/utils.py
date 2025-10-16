from github import Github, GithubException

def push_to_github(repo_path, repo_name):
    g = Github(os.getenv("GITHUB_TOKEN"))
    user = g.get_user()

    # Check if repo exists
    try:
        repo = user.get_repo(repo_name)
        print(f"Repo {repo_name} already exists, using existing repo.")
    except GithubException:
        repo = user.create_repo(repo_name, private=False)

    # Continue with commit / push logic...
    commit_sha = "dummy_commit"  # your actual commit SHA logic
    pages_url = f"https://{user.login}.github.io/{repo_name}/"
    return repo.html_url, commit_sha, pages_url
