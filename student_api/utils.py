import os
import time
from github import Github, GithubException

def push_to_github(repo_path, repo_name):
    """
    Push the generated app to GitHub.
    Handles existing repos and returns repo URL, commit SHA, and GitHub Pages URL.
    """
    g = Github(os.getenv("GITHUB_TOKEN"))
    user = g.get_user()

    # Make repo name unique to avoid conflicts
    repo_name_unique = f"{repo_name.replace(' ', '-')}_{int(time.time())}"

    try:
        # Try to create the repo
        repo = user.create_repo(repo_name_unique, private=False)
        print(f"Created new repo: {repo_name_unique}")
    except GithubException as e:
        if e.status == 422:  # repo already exists
            repo = user.get_repo(repo_name_unique)
            print(f"Repo already exists, using existing repo: {repo_name_unique}")
        else:
            raise e

    # TODO: Add actual git push logic here
    # For now, we return a dummy commit SHA
    commit_sha = "dummy_commit_sha"

    pages_url = f"https://{user.login}.github.io/{repo_name_unique}/"

    return repo.html_url, commit_sha, pages_url
