names = []
names.append(raw_input("Hoe heet je?"))
names.append(raw_input("Nog iemand?"))
names.append(raw_input("En nog iemand?"))

fruit = raw_input("Noem eens een vrucht")

for name in names:
    if name[0].isupper():
        print "Aangenaam " + name
    else:
        print "Hoi " + name

    if "te" in name:
        print "Jij bent vast Lotte of Maarten"

    print "%s is een %s" % (name, fruit.upper())