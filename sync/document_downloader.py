import requests
from urllib.parse import urlparse, unquote
from dateutil.parser import parse as parsedate
from pathlib import Path
from sync import core

def filename_from_url(url: str) -> str:
    path = urlparse(url).path
    return unquote(Path(path).name)

def last_modified_date(headers) -> str:
    # https://stackoverflow.com/a/70641487/6830113
    import collections
    collections.Callable = collections.abc.Callable
    last_modified = headers["last-modified"]
    url_date = parsedate(last_modified)
    return url_date.strftime("%Y-%m-%d")

def download(project: any, url: str):
    # TODO: Get the latest document on disk
    response = requests.get(url)
    filepath = core.dir_for_project(project) / last_modified_date(response.headers) / filename_from_url(url)
    core.create_dir_if_not_exists(filepath.parent)
    print(f"Downloaded {url} to {filepath}")
    # TODO: Don't create day dir if no changes happened
    # if changed_date > last_date, write new file
    with open(filepath, 'wb') as f:
        f.write(response.content)
