import csv
LOCATION = "C:/Users/OliviaCurtis/Fourteen IP Communications/PolyAI & Fourteen IP EVA Development - General/403 Errors/errors_list.csv"

with open(LOCATION, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        