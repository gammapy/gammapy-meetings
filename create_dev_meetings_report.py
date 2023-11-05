import os
from datetime import datetime, timedelta
import pytz

current_directory = '.' #os.getcwd()

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

# ***************** reading token from a file ************************
# token_file_path = "/home/hstapel/PycharmProjects/projekt_gammapy/token/token.txt"
# # check if file is present
# if os.path.isfile(token_file_path):
#     with open(token_file_path) as file:
#         token = file.read().replace('\n', '')
# # token = os.environ('repo-token?') # for CI

# ***************** connecting to the repository of gammapy with token or without ***************
from github import Github
token = os.environ["SUPER_SECRET"]
gh = Github(token)
repo_gammapy = gh.get_repo("gammapy/gammapy")

# ***************** getting pulls**********************
gammapy_pulls_all_open = repo_gammapy.get_pulls('open')
gammapy_pulls_all_closed = repo_gammapy.get_pulls('closed')
gammapy_issues = repo_gammapy.get_issues()
pulls_page1 = gammapy_pulls_all_open.get_page(0)

# *************** one week long **********************
days = 8
d = datetime.today() - timedelta(days=days)


def list_items(text, items):
    for i in items:
        if i.created_at.replace(tzinfo=pytz.utc) > d.replace(tzinfo=pytz.utc):
            text = text + f'* [#{i.number}]({i.html_url}) {i.title} - {i.user.name}\n'
    return text


pulls_text = list_items(f'\n### PRs opened last week (less than {days} days ago): \n', gammapy_pulls_all_open)
merged_text = list_items(f'\n### PRs merged last week (less than {days} days ago): \n', gammapy_pulls_all_closed)
issues_text = list_items(f'\n### issues opened last week (less than {days} days ago): \n', gammapy_issues.get_page(0))

report = title + report_heading + pulls_text + merged_text + issues_text + report_footer

if not isExist:
    os.makedirs(today_report)
today_report_md = os.path.join(today_report, "README.md")

with open(today_report_md, "w") as f:
    f.write(report)

if __name__ == "__main__":
    print('all is good')
