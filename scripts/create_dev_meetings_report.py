# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
This script will run once a week (on Friday at 6 am? dev_meeting_reports.yml defines the time
with cron syntax) to create a Gammapy Developer Meeting Report containing pull requests which have been
opened or merged, as well as issues which have been opened since the previous meeting
"""

import os
from datetime import datetime, timedelta
import pytz
from github import Github

current_directory = '.'

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

# ***************** connecting to the repository of gammapy with token ***************

token = os.environ["SUPER_SECRET"]
gh = Github(token, per_page=200)
repo_gammapy = gh.get_repo("gammapy/gammapy")

# ***************** getting pulls**********************
gammapy_pulls_all_open = repo_gammapy.get_pulls('open').get_page(0)
gammapy_pulls_all_closed = repo_gammapy.get_pulls('closed').get_page(0)
gammapy_issues = repo_gammapy.get_issues(state='open').get_page(0)
#pulls_page1 = gammapy_pulls_all_open.get_page(0)
# *************** one week long **********************
days = 8
d = datetime.today() - timedelta(days=days)


def list_items(text, items, closed=False):
    for i in items:
        time = i.closed_at if closed else i.created_at
        if time.replace(tzinfo=pytz.utc) > d.replace(tzinfo=pytz.utc):
            text = text + f'* [#{i.number}]({i.html_url}) {i.title} - {i.user.name}\n'
    return text

def list_created_issues(text, issues):
    for i in issues:
        if i.pull_request is None:
            if i.created_at.replace(tzinfo=pytz.utc) > d.replace(tzinfo=pytz.utc):
                text = text + f'* [#{i.number}]({i.html_url}) {i.title} - {i.user.name}\n'
    return text

pulls_text = list_items(f'\n### PRs opened last week (less than {days} days ago): \n', gammapy_pulls_all_open)
merged_text = list_items(f'\n### PRs merged last week (less than {days} days ago): \n', gammapy_pulls_all_closed, True)
issues_text = list_created_issues(f'\n### issues opened last week (less than {days} days ago): \n', gammapy_issues)

report = title + report_heading + pulls_text + merged_text + issues_text + report_footer

if not isExist:
    os.makedirs(today_report)
today_report_md = os.path.join(today_report, "README.md")

with open(today_report_md, "w") as f:
    f.write(report)

if __name__ == "__main__":
    print('all is good')
