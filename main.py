import csv

records = []

class Record:
    def __init__(self, number, occurences, domain, instances = None) -> None:
        self.number = number
        self.occurences = occurences
        self.domain = domain
        self.instances = instances if instances else []

    def __str__(self):
        return f"Record - Number: {self.number}, Occurences: {self.occurences}, Domain: {self.domain}, Instances: {self.instances}"

with open("./input/403.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        domain = row[0].split("@")[1]


        records.append(Record(row[0], row[1], domain, row[2]))


for r in records:
    print(r)
