from sync import document_downloader as document_downloader

def test_filename_from_url():
    url = "https://www.example.com./projekt/oderberger-strasse-8/"
    result = document_downloader.filename_from_url(url)
    assert result == "oderberger-strasse-8"

    url = "https://www.example.com./projekt/oderberger-strasse-8/filename.pdf"
    result = document_downloader.filename_from_url(url)
    assert result == "filename.pdf"

    url = "https://www.example.com/projekt/oderberger-strasse-8/filename.pdf?1234"
    result = document_downloader.filename_from_url(url)
    assert result == "filename.pdf"

    url = "https://www.example.com/projekt/oderberger-strasse-8/filename.pdf?1234#abc"
    result = document_downloader.filename_from_url(url)
    assert result == "filename.pdf"

def test_last_modified_date():
    headers = { "last-modified": "Tue, 30 Apr 2024 07:38:39 GMT" }
    result = document_downloader.last_modified_date(headers)
    assert result == '2024-04-30'
