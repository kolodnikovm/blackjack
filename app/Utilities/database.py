import os
import csv
# Заделать через os.path путь к файлу БД
class DataBase:
    """ Класс предоставляет инструменты для работы с базой данных
    представленным в виде файла, путь которого передается в конструктор класса. """

    def __init__(self, db):
        self.db_file = open(db, 'a+', newline='')
        self.writer = csv.writer(self.db_file)


    def save_data(self, data):
        """ Сохраняет параметр data в файл self.db """
        # TODO Flush() file
        self.writer.writerow(data)

    def read_total_score(self):
        self.reader = csv.reader(self.db_file)
        total_score = [0, 0]
        for row in self.reader:
            total_score[0] += int(row[2]); total_score[1] += int(row(3))
        return total_score
