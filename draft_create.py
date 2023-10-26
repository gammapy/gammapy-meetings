import sys

from github import Github
import os


def get_github_repo():
    try:
        token = os.environ["SECRET_GITHUB_TOKEN"]
    except KeyError:
        token = "Token not available!"
    print("beginning")
    gh = Github(token)
    # gh = Github()
    repo_gammapy = gh.get_repo("gammapy/gammapy")
    print(repo_gammapy.get_pulls().get_page(1))
    print("end")


if __name__ == "__main__":
    get_github_repo(sys.argv[1])
    # get_github_repo()
