from sync import core as sync
from pathlib import Path

def test_filter():
    p1 = [{ 'status': 'Abgeschlossen' }, { 'status': 'in Bau'}]
    result = list(filter(sync.without_done_projects, p1))
    assert result == [{ 'status': 'in Bau'}]


def test_project_slug_from_url():
    url = "https://www.example.com/projekt/oderberger-strasse-8/"
    result = sync.project_slug_from_url(url)
    assert result == "oderberger-strasse-8"

def test_filename_from_url():
    url = "https://www.example.com./projekt/oderberger-strasse-8/"
    result = sync.filename_from_url(url)
    assert result == "oderberger-strasse-8"

    url = "https://www.example.com./projekt/oderberger-strasse-8/filename.pdf"
    result = sync.filename_from_url(url)
    assert result == "filename.pdf"

    url = "https://www.example.com/projekt/oderberger-strasse-8/filename.pdf?1234"
    result = sync.filename_from_url(url)
    assert result == "filename.pdf"

    url = "https://www.example.com/projekt/oderberger-strasse-8/filename.pdf?1234#abc"
    result = sync.filename_from_url(url)
    assert result == "filename.pdf"

def test_root_dir():
    assert sync.root_dir().name == "infravelo-py"
