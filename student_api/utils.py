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

    # Make repo name unique
    repo_name_unique = f"{repo_name.replace(' ', '-')}_{int(time.time())}"

    try:
        # Try to create the repo
        repo = user.create_repo(repo_name_unique, private=False)
        print(f"Created new repo: {repo_name_unique}")
    except GithubException as e:
        if e.status == 422:
            # Repo already exists, get existing one
            repo = user.get_repo(repo_name_unique)
            print(f"Repo already exists, using existing repo: {repo_name_unique}")
        else:
            # Other GitHub errors
            raise e

    # TODO: Add your actual commit/push logic
    commit_sha = "dummy_commit_sha"

    pages_url = f"https://{user.login}.github.io/{repo_name_unique}/"

    return repo.html_url, commit_sha, pages_url
