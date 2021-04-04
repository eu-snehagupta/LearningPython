import os
import csv
from csv import reader

def read_data():
    data = []
    with open ("data.csv", "r") as f:
        csv_reader = reader(f)
        header = next(csv_reader)
        if header != None:
            for rows in csv_reader:
                data.append(rows[0].replace(";",","))
        print(data)
    with open ("data1.csv", "w") as f:
        for eachitem in data:
            f.write(eachitem + "\n")


read_data()