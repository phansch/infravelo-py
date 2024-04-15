from sync import core as sync

def test_filter():
    p1 = [{ 'status': 'Abgeschlossen' }, { 'status': 'in Bau'}]
    result = list(filter(sync.without_done_projects, p1))
    assert result == [{ 'status': 'in Bau'}]
