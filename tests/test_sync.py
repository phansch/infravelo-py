from sync import core
from pathlib import Path


def test_filter():
    p1 = [{"status": "Abgeschlossen"}, {"status": "in Bau"}]
    result = list(filter(core.without_done_projects, p1))
    assert result == [{"status": "in Bau"}]


def test_bike_rack_filter():
    p1 = [
        {
            "types": [
                {
                    "name": "",
                    "type": "Anlehnb\u00fcgel",
                    "metrics": [{"name": "Anzahl Stellpl\u00e4tze", "value": "16"}],
                }
            ]
        }
    ]
    result = list(filter(core.without_bike_racks, p1))
    assert result == []


def test_project_slug_from_url():
    url = "https://www.example.com/projekt/oderberger-strasse-8/"
    result = core.project_slug_from_url(url)
    assert result == "oderberger-strasse-8"


def test_root_dir():
    assert core.root_dir().name == "infravelo-py"
