import csv
import logging
from os import stat


class DataBase:
    def __init__(self, db_filename='app/assets/db_dev.csv', *args, **kwargs):
        self._db_file = open(db_filename, 'a+', newline='')
        self.__FIELDNAMES = ['user cards',
                             'computer cards', 'user win', 'computer win']
        self._csv_writer = csv.DictWriter(
            self._db_file, fieldnames=self.__FIELDNAMES)
        self._csv_reader = csv.DictReader(
            self._db_file, fieldnames=self.__FIELDNAMES)

        if not stat(db_filename).st_size:
            logging.debug('No data found. Creating new...')
            self._csv_writer.writeheader()

    def save_data(self, data):
        self._csv_writer.writerow(data)

    def load_data(self):
        self._db_file.seek(0)
        db_data = list(self._csv_reader)
        return db_data

    def save_backup(self):
        pass

    def load_backup(self):
        pass

    def close_databse(self):
        self._db_file.close()


if __name__ == '__main__':
    from functools import reduce
    db = DataBase()
    totals = 0
    data = db.load_data()[1:5]
    for d in data:
        totals += (d['user win'])
    print(totals)
