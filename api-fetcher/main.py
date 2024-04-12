import requests

session = requests.Session()

def get_projects():
    url = "https://www.infravelo.de/api/v1/projects/"
    first_page = session.get(url).json()
    yield first_page
    next_page_url = first_page["next"]

    while next_page_url != None:
        next_page = session.get(next_page_url).json()
        next_page_url = next_page["next"]
        yield next_page

def run():
    all_projects = []
    for page in get_projects():
        all_projects += page["results"]

    all_projects
