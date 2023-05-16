import csv
import re

RECORDS = []
class Record:
    def __init__(self, number, occurences, variant, instances = None) -> None:
        self.number = number
        self.occurences = occurences
        self.variant = variant.upper()
        self.instances = instances if instances else []

    def __str__(self):
        return f"Record - Number: {self.number}, Occurences: {self.occurences}, Variant: {self.variant}, Instances: {self.instances}"

with open("./input/403.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:

        variant = row[0].split("@")[1].split(".")[0]
        number = re.search(r"\b(\d+)\b", row[0]).group(1)
        RECORDS.append(Record(number, row[1], variant, row[2:]))

for r in RECORDS:
    print(r)
