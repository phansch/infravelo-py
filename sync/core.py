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
        dir_for_project(project).mkdir(parents=True,exist_ok=True)

def run():
    runner.run()
