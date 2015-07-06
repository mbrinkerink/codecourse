print "Welkom bij de Swiebertje-quiz!"
gebruiker = raw_input("Gebruiker, wil je a.u.b. je naam typen?")

print "Welkom %s!" % (gebruiker)
print "Welkom " + gebruiker + "!"
print "Welkom " + gebruiker + ", je hebt " + fout + " fouten!"
print "Welkom %s, je hebt %d fouten" % (gebruiker, fout)

vraag1 = raw_input("Noem een willekeurig jaar waarin Swiebertje op tv was.")
vraag1 = int(vraag1)
if vraag1 > 1954 and vraag1 < 1976:
	score1 = 1
else:
	score1 = 0
vraag2 = raw_input("Wie speelde Swiebertje?")
if vraag2 == "Joop":
	score2 = 1
elif vraag2 == "Doderer":
	score2 = 1
else:
	score2 = 0
score_totaal = score1 + score2
fouten = 2 - score_totaal
print "Aantal goede antwoorden: %s" % (score_totaal)
print "Aantal foute antwoorden: %s" % (fouten)
if score_totaal == 2:
	print "Held! Allebei goed %s!" % (gebruiker)
elif score_totaal == 1:
	print "Volgende keer beter %s! Helaas maar 1 correct antwoord..." % (gebruiker)
else:
	print "Godverdehoeren, wat ben jij slecht %s! Geen enkel goed antwoord!" % (gebruiker)