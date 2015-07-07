naam1 = raw_input("Geef een naam:")
naam2 = raw_input("Geeft nog een naam:")
vrucht = raw_input("Noem een vrucht:")
# Eigenlijk is == True hier overbodig. Default is True, enkel False maak je expliciet.
if naam1[0].isupper() == True:
	print "Aangenaam %s" % (naam1)
elif naam1[0].isupper() == False:
	print "Hoi %s" % (naam1)
# Werkt alleen tussen haakjes of zonder == True expliciet te maken.
if ("te" in naam1) == True:
	print "Er zit 'te' in je naam"
if naam2[0].isupper() == True:
	print "Aangenaam %s" % (naam2)
elif naam2[0].isupper() == False:
	print "Hoi %s" % (naam2)
if ("te" in naam2) == True:
	print "Er zit 'te' in je naam"
vrucht_groot = vrucht.upper()
print "%s is een %s" % (naam1, vrucht_groot)
print "%s is een %s" % (naam2, vrucht_groot)