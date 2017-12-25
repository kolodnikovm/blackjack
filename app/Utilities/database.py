""" Модуль базы данных """
import csv
from .supfuncs import remove_empty_lines

class DataBase:
    """ Класс предоставляет инструменты для работы с базой данных,
    представленной в виде файла, путь которого передается в конструктор класса. """

    def __init__(self, db):
        self.db_file = open(db, 'r+', newline='')


    def save_data(self, data):
        """ Сохраняет параметр data в файл self.db_file """
        csv.writer(self.db_file).writerow(data)
        remove_empty_lines(self.db_file)
        # self.db_file.flush()
        # os.fsync(self.db_file)

    def read_total_score(self):
        """ Считывает кол-во выйгрышных матчей компьютера и пользователя.
        Возращает суммарное кол-во побед в виде списка [<побед юзера>, <побед компа>] """
        total_score = [0, 0]
        for row in csv.reader(self.db_file):
            total_score[0] += int(row[2])
            total_score[1] += int(row[3])
        return total_score
