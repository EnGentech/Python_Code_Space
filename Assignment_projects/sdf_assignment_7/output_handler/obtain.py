import csv

with open('delete.csv', "r") as file:
    reader = csv.reader(file)
    for x in reader:
        print(x)
