from enum import Enum
from pathlib import Path
import os
from sync import runner

# Various util methods for filesystem and request things

class ProjectState(Enum):
    DONE = "Abgeschlossen"
    UNDER_CONSTRUCTION = "in Bau"
    IN_PLANNING = "in Planung"
    ENVISAGED = "Vorgesehen"

def without_done_projects(project):
    return project['status'] != ProjectState.DONE.value

def project_slug_from_url(project_url):
    return project_url.split('/')[-2]

def root_dir() -> Path:
    return Path(__file__).parent.parent

def dir_for_project(project) -> Path:
    return root_dir() / "data" / project_slug_from_url(project["link"])

def create_project_dirs(projects):
    for project in projects:
        create_dir_if_not_exists(dir_for_project(project))

def create_dir_if_not_exists(path: Path):
    path.mkdir(parents=True,exist_ok=True)

def run():
    runner.run()
