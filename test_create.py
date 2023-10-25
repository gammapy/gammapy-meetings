import sys

from github import Github


def get_github_repo(token):
    gh = Github(token)
    repo_gammapy = gh.get_repo("gammapy/gammapy")
    print(repo_gammapy)


if __name__ == "__main__":
    get_github_repo(sys.argv[1])
