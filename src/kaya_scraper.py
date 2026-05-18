import requests
import json
from datetime import datetime, timedelta
import json

SENT_FILE = "sent_projects.json"


def load_sent_projects():
    try:
        with open(SENT_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    except:
        return set()


def save_sent_projects(sent_projects):
    with open(SENT_FILE, "w", encoding="utf-8") as f:
        json.dump(list(sent_projects), f)


def kaya_scraper(skill_id):
    API_URL = f"https://ir.api.kaya.ir/api/v2/projects/projects?limit=20&offset=0&skills={skill_id}"
    sent_projects = load_sent_projects()
    projects = requests.get(API_URL).json()["projects"]

    results = []
    now = datetime.now()

    for project in projects:
        project_id = project["project_id"]
        project_time = datetime.fromtimestamp(project["submit_date"] / 1000)

        if now - project_time <= timedelta(minutes=10) and project_id not in sent_projects:
            title = project["title"]
            description = project["description"]
            date = project_time.strftime("%Y-%m-%d %H:%M")
            jobs = ", ".join(job["name"] for job in project["jobs"])

            text = f"""
Project ID : {project_id}
Title      : {title}
Date       : {date}
Budget     : {project['budget_minimum']} - {project['budget_maximum']} {project['currency_code']}
Country    : {project['owner_country']}

Skills     : {jobs}

Description:
{description}

Link:
{project['freelancer_url']}
"""
            results.append(text)
            sent_projects.add(project_id)

    save_sent_projects(sent_projects)

    return results
