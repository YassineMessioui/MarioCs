from traitement_csv import import_csv_layout
import csv


def read_high_score(level):
    data = import_csv_layout("./score.csv")
    return int(data[level + 1][1])


def change_score(level, score):
    data = import_csv_layout("./score.csv")
    if score > int(data[level + 1][1]):
        data[level + 1][1] = str(score)
        with open("score.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
