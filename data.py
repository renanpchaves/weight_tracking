import csv

date_strings = []
weight = []

with open('data.csv') as r:
    reader = csv.reader(r)
    for row in reader:
        date_strings.append(row[0])
        weight.append(float(row[1]))