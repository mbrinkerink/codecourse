name1 = raw_input("Hoe heet je?")
name2 = raw_input("Hoe heet de ander?")
fruit = raw_input("Noem eens een vrucht")

if name1[0].isupper():
    print "Aangenaam " + name1
else:
    print "Hoi " + name1

if "te" in name1:
    print "Jij bent vast Lotte of Maarten"

print "%s is een %s" % (name1, fruit.upper())

if name2[0].isupper():
    print "Aangenaam " + name2
else:
    print "Hoi " + name2

if "te" in name2:
    print "Jij bent vast Lotte of Maarten"

print "%s is een %s" % (name2, fruit.upper())