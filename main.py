#TODO: spit out to 403 errors, add project

import csv
import re
from datetime import datetime
from eva_store import store

TODAYS_DATE = datetime.today().strftime('%d/%m/%Y')
RECORDS = []


class Record:
    def __init__(self, project, number, occurences, variant, instances = None) -> None:
        self.project = project
        self.number = number
        self.occurences = occurences
        self.variant = variant.upper()
        self.instances = instances if instances else []

    def __str__(self):
        return f"Record - Project: {self.project} Number: {self.number}, Occurences: {self.occurences}, Variant: {self.variant}, Instances: {self.instances}"

with open("./input/403.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:

        variant = (row[0].split("@")[1]).split(".")[0]
        number = re.search(r"\b(\d+)\b", row[0]).group(1)
        project = ""

        for site in store.ALL_SITES:
            if site.variant_id == variant.upper():
                project = site.project_name

        RECORDS.append(Record(project, number, row[1], variant, row[2:]))


for r in RECORDS:
    r.instances = list(filter(lambda x: x != '', r.instances))
    print(r.instances)

with open("./output/403_formatted.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    for r in RECORDS:


        row = ["", r.project, r.variant, r.number, r.occurences, TODAYS_DATE, r.instances, "", "Not-Started"]




        csv_writer.writerow(row)
