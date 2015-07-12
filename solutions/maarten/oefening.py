getallen = range(1, 101)

for getal in getallen:
	if (getal % 3) == 0 and (getal % 5) == 0:
		print "%s BlipBlop" % (getal)
	elif (getal % 3) == 0:
		print "%s Blop" % (getal)
	elif (getal % 5) == 0:
		print "%s Blip" % (getal)
	else:
		print getal