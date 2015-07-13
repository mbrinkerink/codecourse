def functie(bestand):
	open_bestand = open(bestand)
	print 'Printing "%s"' % (bestand)
# enumerate() geeft altijd 2 variabelen terug!!!
	for index, naam in enumerate(open_bestand):
		print index, naam.strip()
		
functie("people.txt")
functie("people2.txt")