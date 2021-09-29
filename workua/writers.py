import csv
import sqlite3
import json


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


class JSONWriter:
    def __init__(self):
        self._file = open('./results.json', 'w')

    def write(self, item: dict):
        json.dump(item, self._file, ensure_ascii=False, indent=4)
        self._file.write(',')


class DbWriter:

    def __init__(self):
        self.con = sqlite3.connect('./workua.db')
        self.cur = self.con.cursor()

    def write(self, item):

        sql_query_to_create_table = '''CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER NOT NULL PRIMARY KEY,
            href VARCHAR(60),
            jobs_id INTEGER,
            title VARCHAR(200),
            salary VARCHAR(50),
            address VARCHAR(50),
            description VARCHAR(5000)
            );'''
        self.cur.execute(sql_query_to_create_table)

        sql_write_query = f'''INSERT INTO jobs VALUES (
        null,
        '{item['href']}',
        '{item['id']}',
        '{item['title']}',
        '{item['salary']}',
        '{item['work_address']}',
        '{item['description'][0]}'
        )'''
        try:
            self.cur.execute(sql_write_query)
        except Exception as exc:
            error = exc
            breakpoint()
        self.con.commit()


        # self.cur.execute(
        #     f'''INSERT INTO jobs (
        #     'href',
        #     'id',
        #     'title',
        #     'salary',
        #     'address',
        #     'description',)
        #     VALUES (
        #     '{item['href']}',
        #     '{item['id']}',
        #     '{item['title']}',
        #     '{item['salary']}',
        #     '{item['work_address']}',
        #     '{item['description']}',)'''
        # )


        # self.cur.executemany(
        #     f'''INSERT INTO jobs (?,?,?,?,?,?)''', item.values()
        #     values ('{item[row]})'''
        # )
        #     'insert into {db_name} (t1, i1) values (?, ?)'.format(self._table), (row['t1'], row['i1'])
        # self.con.commit()


