namen = []
namen.append(raw_input("Geef een naam:"))
namen.append(raw_input("Geef nog een naam:"))
namen.append(raw_input("En geef nog een naam:"))
vrucht = raw_input("Noem een vrucht:")
vrucht = vrucht.upper()

for naam in namen:
	if naam[0].isupper():
		print "Aangenaam %s" % (naam)
	else:
		print "Hoi %s" % (naam)
# Begin hier weer met een for-loop zodat de drie fases niet door elkaar lopen.
for naam in namen:
	if ("te" in naam):
		print "Er zit 'te' in %s" %(naam)
for naam in namen:
	print "%s is een %s" % (naam, vrucht)