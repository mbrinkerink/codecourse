import csv

csvfile = open("twitter.csv")
reader = csv.DictReader(csvfile)

for row in reader:
    for key, val in row.iteritems():
        print "%s: %s" % (key, val)

    print "---"