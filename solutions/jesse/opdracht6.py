name1 = raw_input("Hoe heet je?")
name2 = raw_input("Hoe heet de ander?")
name3 = raw_input("Hoe heet de laatste?")
fruit = raw_input("Noem een vrucht")

names = [str(name1), str(name2), str(name3)]

for item in names:
    print "%s is een %s" % (item, fruit.upper())

for item in names:
    if item[0].isupper():
        print "Aangenaam " + item
    if item[0].islower():
        print "Hoi " + item
    if "te" in item:
        print "Jij bent vast Lotte of Maarten"

for item in names:
    print "%s is een %s" % (item, fruit.upper())


