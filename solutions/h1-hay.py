correct = 0
incorrect = 0

print "Welkom bij de briljante superquiz"
print "Laten we beginnen met je naam"
name = raw_input("Wat is je naam?")

print "Fantastisch " + name

# Vraag 1
q = raw_input("Vraag 1! Noem een willekeurig jaar waarin Swiebertje op TV was?")
if int(q) > 1954 and int(q) < 1975:
    print "Helemaal goed!"
    correct = correct + 1
else:
    print "Totaal fout!"
    incorrect = incorrect + 1

# Vraag 2
q = raw_input("Wie speelde Swiebertje? Noem de voornaam, of de achternaam.")
if q == "joop" or q == "doderer":
    print "Supertof!"
    correct = correct + 1
else:
    print "Aaargh! Nee, dat is niet goed!"
    incorrect = incorrect + 1

print "Je had er goed " + str(correct)
print "Je had er fout " + str(incorrect)

if correct > incorrect:
    print "Ja! Hoera! Meer goed dan fout!"
elif correct == incorrect:
    print "Even veel goed als fout!"
else:
    print "Alles fout! Sukkel!"