leeftijd1 = raw_input("Wat is jouw leeftijd persoon 1?")
leeftijd2 = raw_input("Wat is jouw leeftijd persoon 2?")
naam1 = raw_input("Wat is jouw naam persoon 1?")
naam2 = raw_input("Wat is jouw naam persoon 2?")
barrie = "Barrie"
print "Persoon 1 is ouder:"
print int(leeftijd1) > int(leeftijd2)
print "Persoon 2 is ouder:"
print int(leeftijd2) > int(leeftijd1)
print "Er is een Barrie:"
print barrie == naam1 or barrie == naam2