from bs4 import BeautifulSoup
import requests

def get_html(url):
    request = None
    request = requests.get(url)
    if request.ok:
        return request.text
    else:
        print(request.status_code)

def scrape_html(html):
    sections = {}
    soup = BeautifulSoup(html, "html.parser")

    job_header = soup.find(id="jobHeader")
    job_summary = soup.find('span', attrs={"id":"job_summary"})

    print(job_header)

    if job_summary and len(job_summary) > 1:
            sections['header'] = job_header
            sections['summary'] = job_summary
    else:
        return None
    #job_content = soup.find(id="job-content") -- not sure if I want this

    return sections
