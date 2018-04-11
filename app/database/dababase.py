import csv
import logging
import pickle
from os import stat


class DataBase:
    def __init__(self, fieldnames, db_filename='app/assets/db_dev.csv', bckp_filename='app/assets/data', *args, **kwargs):
        self._db_filename = db_filename
        self._bckp_filename = bckp_filename
        self._db_file = open(db_filename, 'a+', newline='')
        self._FIELDNAMES = fieldnames
        self._csv_writer = csv.DictWriter(
            self._db_file, fieldnames=self._FIELDNAMES)
        self._csv_reader = csv.DictReader(
            self._db_file, fieldnames=self._FIELDNAMES)

        if not stat(db_filename).st_size:
            logging.debug('No data found. Creating new...')
            self._csv_writer.writeheader()

    def save_data(self, data, backup=False, save_to=None):
        if save_to:
            with open(save_to, 'a+', newline='', encoding='utf-8') as fh:
                writer = csv.writer(fh)
                writer.writerow(data)
        if backup:
            with open(self._bckp_filename, 'wb') as bckp:
                pickle.dump(data, bckp)
        else:
            self._csv_writer.writerow(data)

    def load_data(self, restore=False):
        if restore:
            with open(self._bckp_filename, 'rb') as bckp:
                return pickle.load(bckp)
        else:
            self._db_file.seek(0)
            db_data = list(self._csv_reader)
            return db_data

    def reset_file(self, file=None):
        if file is None:
            file = self._bckp_filename
        open(file, 'w').close()

    def close_database(self):
        self._db_file.close()
