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
    return request.data

def scrape_html(html):
    soup = BeautifulSoup(html, "html.parser")

    # job_content = soup.find(id="job-content")
    # job_header = soup.find(id="job-header
    job_summary = soup.find(id="job_summary")
    for p in job_summary.find_all('p'):
        print(p)
        print("--------------------")
    return job_summary
