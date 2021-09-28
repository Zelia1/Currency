import requests
from filter import filter_word
import re
from bs4 import BeautifulSoup
from writers import TxtWriter, CSVWriter, DbWriter, JSONWriter

ROOT = 'https://www.work.ua'

full_url = ROOT + '/ru/jobs/'

result = []
page = 1

writers_list = [
    TxtWriter(),
    CSVWriter(),
    JSONWriter(),
    DbWriter(),
]

while True:

    print(f'Page: {page}')

    # TODO
    if page == 2:
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

    root_job = ''
    for job_details in jobs:
        data = {}
        href = job_details.find('a')['href']
        url_job = ROOT + href
        response_job = requests.get(url_job)
        soup_job = BeautifulSoup(response_job.content, 'html.parser')

        for el in soup_job.find_all('div', 'card wordwrap'):
            data['href'] = url_job
            data['id'] = ''.join(char for char in href if char.isdigit())
            data['title'] = el.find('h1').text
            # work_address = el.find('p', {'class': 'text-indent add-top-sm'}).text.strip().split()[0]
            # valid_address = filter_word(work_address)
            try:
                data['salary'] = ''.join(el.find('b', 'text-black').text.split())
            except:
                data['salary'] = None
            try:
                data['work_address'] = filter_word(el.find('p', {'class': 'text-indent add-top-sm'}).text.strip().split()[0])
            except:
                data['work_address'] = None

            # x = el.select('p')[6].text.strip()
            try:
                data['description'] = [i.text.strip() for i in el.select('div#job-description')]
            except:
                data['description'] = None
        for writer in writers_list:
            try:

                writer.write(data)
            except:
                continue

    page += 1
######################################################################################################################

        # breakpoint()
        # root_job = ROOT + href
        # id_ = ''.join(char for char in href if char.isdigit()) + '/'
        # href_by_company = href[:9] + 'by-company/' + id_
        # print(href)
    #
    # response_job = requests.get(root_job)
    # soup_job = BeautifulSoup(response_job.text, 'html.parser')
    # job_container = soup_job.find_all("div", {"class": "card wordwrap"})
    # data = {}
    # p_tag = ''
    # for data_job in job_container:
    #     data['name_job'] = data_job.find("h1", {"id": "h1-name"}).text
    #     try:
    #         data['salary'] = ''.join(data_job.find("b", {"class": "text-black"}).text.split())
    #     except:
    #         data['salary'] = None
    #     try:
    #         data['title'] = data_job.find("a")["title"]
    #     except:
    #         data['title'] = None
    #     try:
    #         data['work_address'] = data_job.find('p', {'class': 'text-indent add-top-sm'}).text.strip()
    #     except:
    #         data['work_address'] = None

       # details_job = data_job.find_all("div", {"id": "job-description"})
       # list_tags = ['p', 'ul', 'li', ]
    #     for tag in list_tags:
    #         for row in details_job:
    #             if tag == 'p':
    #                 p_tag = row.find(tag).text[:-1]
    #                 data[p_tag] = []
    #                 for _ in row:
    #                     breakpoint()
    #                     data[p_tag].append(_.text[:-1])

############################################################################################################3

    #     for tag in list_tags:
    #         for details in details_job:
    #             if tag == 'p':
    #                 for _ in details.find_all(tag):
    #                     p_tag = details.find(tag).text[:-1]
    #                     data[_.text[:-1]] = []
    #             # if tag == 'ul':
    #             #     ul_tag = details.find(tag).text
    #             #     data[p_tag] = [details.find(tag).text]
    #             #     breakpoint()
    #             if tag == 'li':
    #                 for _ in details.find_all(tag):
    #                     data[p_tag].append(_.text[:-1])
    #                     breakpoint()
    #     print(data)

        # id_ = ''.join(char for char in href if char.isdigit())
        # title = job.find('a').text
        # salary = ''.join(job.find('b').text.split())
        # job_info = {
        #     'href': href,
        #     'id': id_,
        #     'title': title,
        #     'salary': salary
        # }
        #
        # for writer in writers_list:
        #     writer.write(job_info)
