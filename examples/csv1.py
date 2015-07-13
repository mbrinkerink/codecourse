csvfile = open("twitter.csv")
keys = []

for index, line in enumerate(csvfile):
    fields = line.split(",")

    if index == 0:
        keys = fields
    else:
        for i, field in enumerate(fields):
            print "%s: %s" % (keys[i].strip(), field.strip())

    print "-----"