from bs4 import BeautifulSoup
import urllib3

def get_html(url):
    request = None
    try:
        http = urllib3.PoolManager()
        request = http.request("GET", url, timeout = 4.0, retries = 2)
    except urllib3.exceptions.NewConnectionError:
        print('Connection failed.')
        return None
    return request

def scrape(url):
    pass
