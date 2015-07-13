def showfile(filename):
    print "Printing " + filename
    f = open(filename)

    counter = 0
    for line in f:
        line = line.strip()
        print "%s %s" % (counter, line)
        counter = counter +1

showfile("people.txt")
print "-----" * 10
showfile("people2.txt")