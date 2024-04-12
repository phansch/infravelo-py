from bs4 import BeautifulSoup
import requests

INFRAVELO_DOMAIN = "https://infravelo.de"

def get_document_urls_from_page(page_url: str) -> list[str]:
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, "html.parser")
    download_items = soup.find_all("a", class_="download--item-download") # a download link
    urls = []
    for item in download_items:
        urls.append(INFRAVELO_DOMAIN + item["href"])
    print(urls)
    return urls


def test():
    get_document_urls_from_page("https://www.infravelo.de/projekt/otto-braun-strasse/")
