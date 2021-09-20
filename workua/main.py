import requests
from bs4 import BeautifulSoup

ROOT = 'https://www.work.ua'

full_url = ROOT + '/ru/jobs/'

params = {
    'page': 1,
}

response = requests.get(full_url, params=params)
soup = BeautifulSoup(response.text, 'html.parser')
job_list_container = soup.find("div", {"id": "pjax-job-list"})
jobs = soup.find_all("div", {"class": "card card-hover card-visited wordwrap job-link js-hot-block"})

result = []
for job in jobs:
    href = job.find('a')['href']
    id_ = ''.join(char for char in href if char.isdigit())
    title = job.find('a').text
    result.append({
        'href': href,
        'id': id_,
        'title': title,
    })

print(result)