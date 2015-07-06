# -*- coding: utf-8 -*-
# Introduceer de Swiebertje quiz
print "Hallo bij de Swiebertje-quiz!"
# Vraag de naam van de gebruiker en heet 'm van harte welkom
name=raw_input("Typ om te beginnen maar eens eerst jouw naam: ")
print "Welkom!"

# De eerste vraag is: noem een willekeurig jaar waarin Swiebertje op tv was (elk antwoord tussen 1955 en 1975 is goed)
year=raw_input("Noem een willekeurig jaar waarin Swiebertje op tv was. Jouw antwoord: ")
year = int(year)

if int(year) < 1975 and year > 1955:
    answer1 = "True"
else:
    answer1 = "False"

# De tweede vraag is: Wie speelde Swiebertje? Zowel de voornaam ("Joop") als de achternaam ("Doderer") is goed, maar niet de hele naam!
actor=raw_input("Wie speelde Swiebertje? Geef de voornaam of de achternaam. Jouw antwoord: ")

if (actor == "Joop") or (actor == "Doderer"):
    answer2 = "True"
else:
    answer2 = "False"

# Print vervolgens het aantal goede en foute antwoorden (die moet je dus bij het hele programma bijhouden!)
print answer1
print answer2

# Print dan of de gebruiker gewonnen, verloren, of evenveel goede als foute antwoorden had met een bijpassend compliment of verwensing.

if answer1 == "True" and answer2 == "True" :
        print "Proficiat, slimmerik! Zou je niet eens bij Beelden Geluid gaan werken?"
elif answer1 == "True" or answer2 == "True":
        print "Bijna helemaal goed gegaan, toch een hele vraag juist! Heb je wel even op Google gekeken?"
else:
        print "Terug naar school met jou!"

# Je kunt deze quiz maken met alleen de kennis die je deze les hebt opgedaan bij opdrachten #1, #2 en #3. Wat je zeker nodig zult hebben:
# Input van de gebruiker via raw_input
# Booleaanse vergelijkingen (and / or / groter dan / kleiner dan)
# if / else
# Converteren tussen string en integer en vice versa
# Concateneren van strings