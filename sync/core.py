from api_fetcher import core as api_fetcher
from scraper import core as scraper
from enum import Enum

class ProjectState(Enum):
    DONE = "Abgeschlossen"
    UNDER_CONSTRUCTION = "in Bau"
    IN_PLANNING = "in Planung"
    ENVISAGED = "Vorgesehen"

def without_done_projects(project):
    return project['status'] != ProjectState.DONE.value

def run():
    all_projects = api_fetcher.all_projects();
    print(f"Downloaded {len(all_projects)} projects from the Infravelo API")

    # Select projects that are not finished yet, to avoid needless scraping
    projects_to_scrape = list(filter(without_done_projects, all_projects))
    print(f"About to scrape {len(projects_to_scrape)} projects.")

    # TODO: slowly scrape the resulting pages
