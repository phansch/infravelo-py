from sync import document_downloader
from sync import core
from api_fetcher import core as api_fetcher
from scraper import core as scraper
from datetime import date
import json

def project_to_json(project: dict):
    filepath = core.dir_for_project(project) / date.today().strftime("%Y-%m-%d") / "project.json"
    core.create_dir_if_not_exists(filepath.parent)
    with open(filepath, "w") as outfile:
        json.dump(project, outfile)

def run():
    today = date.today() # format: 2024-12-21
    all_projects = api_fetcher.all_projects();
    print(f"Downloaded {len(all_projects)} projects from the Infravelo API")

    # Select projects that are not finished yet, to avoid needless scraping
    projects_to_scrape = list(filter(core.is_project_to_scrape, all_projects))
    print(f"About to scrape {len(projects_to_scrape)} projects.")

    core.create_project_dirs(projects_to_scrape)

    for project in projects_to_scrape:
        print(f"Scraping {project["link"]}")
        project_to_json(project)
        # TODO: Skip project if already checked today
        # TODO: Download json
        document_urls = scraper.get_document_urls_from_page(project['link'])
        for url in document_urls:
            document_downloader.download(project, url)
