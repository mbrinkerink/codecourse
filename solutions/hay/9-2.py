def showfile(filename):
    print "Printing " + filename

    with open(filename) as f:
        for index, line in enumerate(f):
            print "%s %s" % (index, line.strip())

showfile("people.txt")
print "-----" * 10
showfile("people2.txt")