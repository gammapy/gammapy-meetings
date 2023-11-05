import sys

from github import Github
import os
from datetime import datetime, timedelta
import pytz

#token = os.environ["SECRET_GITHUB_TOKEN"]
#def get_github_repo(token):
def get_github_repo():
    try:
        token = os.environ["SUPER_SECRET"]
    except KeyError:
        token = "Token not available!"
        print(token)
    print("beginning", len(token), token.upper())
    gh = Github(token)
    #gh = Github()
    repo_gammapy = gh.get_repo("gammapy/gammapy")
    print(repo_gammapy.get_pulls().get_page(1))
    print("end")

    current_directory = os.getcwd()

    today = str(datetime.today().strftime('%Y-%m-%d'))
    time_now = str(datetime.today().strftime('%d/%m/%Y, %H:%M:%S'))
    today_long = str(datetime.today().strftime('%A, %B %d, %Y'))

    today_report = os.path.join(current_directory, "dev-meetings", str(datetime.today().date().year), today)
    isExist = os.path.exists(today_report)

    title = f'# Gammapy Developer Meeting \n'
    report_heading = f' * {today_long}, at 2 pm (CET) \n ' \
                     '* Gammapy Developer Meeting on Zoom (direct link on Slack) \n' \
                     '# Agenda\n'

    report_footer = f'\n report created at {time_now}'
    print(f'isExist {isExist} title {title} report heading {report_heading} report footer {report_footer}')


if __name__ == "__main__":
    get_github_repo()
