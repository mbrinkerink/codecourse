import csv

csvfile_in = open("names.csv")
csvfile_out = open("weirdnames.csv", "w")
csvreader = csv.DictReader(csvfile_in)
csvwriter = csv.writer(csvfile_out)

def silly_name(name):
    n = name.lower()
    return "tsje" in n or "noe" in n or "oeli" in n

csvwriter.writerow(["name", "number", "gender"])

for row in csvreader:
    if silly_name(row["name"]):
        newrow = [ row["name"], row["number"], row["gender"] ]
        csvwriter.writerow(newrow)