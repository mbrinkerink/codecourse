
name = raw_input("Welkom bij de Swiebertje quiz! Hoe heet je?")
print "Van harte welkom, " + name + "!"

vraag1 = raw_input("Bij deze de eerste vraag: noem een willekeurig jaar waarin Swiebertje op tv was")
print int(vraag1)

if int(vraag1) >=1955 and int(vraag1) <=1975:
    print "Correct"
    score = score + 1
else:
    print "Fout"

vraag2 = raw_input("We gaan door: Wie speeltje Swiebertje?")
print vraag2

if vraag2 == "Joop" and "Doderer":
    print "Correct"
    score = score + 1
else:
    print "Fout"

print "Je hebt",str(score)+"/2 vragen goed."
if score == 0:
    print "Het ging om Swiebertje he, niet om Zeg 'ns Aaa. Beetje opletten he!"
if score == 1:
    print "50% is nog steeds een onvoldoende, opnieuw!"
if score == 2:
    print "Wauw! Je bent een ware fan, petje af, winnaar!"