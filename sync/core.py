from api_fetcher import core as api_fetcher
from scraper import core as scraper
from enum import Enum
from pathlib import Path
import os
from urllib.parse import urlparse, unquote
import requests

class ProjectState(Enum):
    DONE = "Abgeschlossen"
    UNDER_CONSTRUCTION = "in Bau"
    IN_PLANNING = "in Planung"
    ENVISAGED = "Vorgesehen"

def without_done_projects(project):
    return project['status'] != ProjectState.DONE.value

def project_slug_from_url(project_url):
    return project_url.split('/')[-2]

def filename_from_url(url: str) -> str:
    path = urlparse(url).path
    return unquote(Path(path).name)

def root_dir() -> Path:
    return Path(__file__).parent.parent

def dir_for_project(project) -> Path:
    return root_dir() / "data" / project_slug_from_url(project["link"])

def create_project_dirs(projects):
    for project in projects:
        dir_for_project(project).mkdir(parents=True,exist_ok=True)

def run():
    all_projects = api_fetcher.all_projects();
    print(f"Downloaded {len(all_projects)} projects from the Infravelo API")

    # Select projects that are not finished yet, to avoid needless scraping
    projects_to_scrape = list(filter(without_done_projects, all_projects))
    print(f"About to scrape {len(projects_to_scrape)} projects.")

    create_project_dirs(projects_to_scrape)

    for project in projects_to_scrape:
        print(f"Scraping {project["link"]}")
        document_urls = scraper.get_document_urls_from_page(project['link'])
        for url in document_urls:
            path = dir_for_project / filename_from_url(url)
            print(f"Downloading {url} to {path}")
            response = requests.get(url)
            with open(path, 'wb') as f:
                f.write(response.content)
