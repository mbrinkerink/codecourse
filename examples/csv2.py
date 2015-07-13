import csv

csvfile = open("twitter.csv")
reader = csv.reader(csvfile)

for row in reader:
    print row