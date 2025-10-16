from github import Github, GithubException
import os

g = Github(os.getenv("GITHUB_TOKEN"))
user = g.get_user()

try:
    repo = user.create_repo(repo_name, private=False)
except GithubException as e:
    if e.status == 422:
        repo = user.get_repo(repo_name)  # use existing repo
    else:
        raise e
