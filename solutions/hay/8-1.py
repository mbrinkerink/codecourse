people = open("people.txt")
twitter = open("twitter.txt")
twitterdates = open("twitterdates.txt", "w")
dates = []

for person in people:
    person = person.strip()
    dates.append(person)

counter = 0

for date in twitter:
    date = dates[counter] + " zit op Twitter sinds " + date
    twitterdates.write(date)
    counter = counter + 1

people.close()
twitter.close()
twitterdates.close()