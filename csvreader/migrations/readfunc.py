import csv, os
from pathlib import Path


def set_file_dir(file_name):
    file_path = os.path.join(Path().absolute().parent.parent, 'files', file_name)
    return file_path


def csvsumm(file_to_count, column_to_sum):
    summed = 0
    with open(file_to_count, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",", quotechar='"')
        first_line = next(csvreader)
        for row in csvreader:
            try:
                summed += float(row[0].split(',')[column_to_sum][1:-1])
            except ValueError:
                pass
    return summed


my_file = set_file_dir('data.csv')
print(csvsumm(my_file, 9))










