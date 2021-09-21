import csv
import sqlite3


class TxtWriter:
    def __init__(self):
        self.file = open('./results.txt', 'w')

    def write(self, item: dict):
        self.file.write(f"{item}\n")


class CSVWriter:
    def __init__(self):
        self._file = open('./results.csv', 'w')
        self.writer = csv.writer(self._file)
        self._headers = None

    def write(self, item: dict):

        if self._headers is None:
            self.writer.writerow(list(item.keys()))

        self.writer.writerow(list(item.values()))


class DbWriter:

    def __init__(self):
        self.con = sqlite3.connect('./workua.db')
        self.cur = self.con.cursor()

    def write(self, item: dict):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS jobs ("
            "id INTEGER NOT NULL PRIMARY KEY,"
            "href VARCHAR(50),"
            "jobs_id INTEGER,"
            "title VARCHAR(200),"
            "salary VARCHAR(50)"
            ");"
        )
        self.cur.execute(
            f"INSERT INTO jobs (href, jobs_id, title, salary)"
            f"values ('{item['href']}', '{item['id']}', '{item['title']}', '{item['salary']}')"
        )
        # 'insert into {db_name} (t1, i1) values (?, ?)'.format(self._table), (row['t1'], row['i1'])
        self.con.commit()

