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
    sections = {'header':'', 'content':''}
    soup = BeautifulSoup(html, "html.parser")

    job_header = soup.find('div', attrs={"data-tn-component":"jobHeader"})
    job_content = soup.find('span', attrs={"id":"job_summary"})

    if job_content and len(job_content) > 1:
            sections['header'] = job_header
            sections['content'] = job_content

    return sections
