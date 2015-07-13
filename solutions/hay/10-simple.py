import csv

csvfile = open("names.csv")
csvreader = csv.DictReader(csvfile)

def silly_name(name):
    n = name.lower()
    return "tsje" in n or "noe" in n or "oeli" in n

for row in csvreader:
    if silly_name(row["name"]):
        print row["name"]