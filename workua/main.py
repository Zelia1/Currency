import requests
from bs4 import BeautifulSoup
from writers import TxtWriter, CSVWriter, DbWriter

ROOT = 'https://www.work.ua'

full_url = ROOT + '/ru/jobs/'

result = []
page = 0

writers_list = [
    TxtWriter(),
    CSVWriter(),
    DbWriter(),
]

while True:
    page += 1
    print(f'Page: {page}')

    # TODO
    if page == 5:
        break

    params = {
        'page': page,
    }

    response = requests.get(full_url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_list_container = soup.find("div", {"id": "pjax-job-list"})

    if job_list_container is None:
        break

    jobs = soup.find_all("div", {"class": "card card-hover card-visited wordwrap job-link js-hot-block"})

    for job in jobs:
        href = job.find('a')['href']
        id_ = ''.join(char for char in href if char.isdigit())
        title = job.find('a').text
        salary = ''.join(job.find('b').text.split())
        job_info = {
            'href': href,
            'id': id_,
            'title': title,
            'salary': salary
        }

        for writer in writers_list:
            writer.write(job_info)
