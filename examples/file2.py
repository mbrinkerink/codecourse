people = open("people.txt")
awesomepeople = open("awesomepeople.txt", "w")

for person in people:
    person = person.strip() # Verwijder newline
    aweseomeperson = "%s is echt super!\n" % person
    awesomepeople.write(aweseomeperson)

people.close()
awesomepeople.close()