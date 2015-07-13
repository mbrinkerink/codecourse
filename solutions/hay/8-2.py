people = open("people.txt")
twitter = open("twitter.txt")
twitterdates = open("twitterdates.txt", "w")

allpeople = people.readlines()
alltwitter = twitter.readlines()
counter = 0

for person in allpeople:
    date = alltwitter[counter].strip()
    person = person.strip()
    twitterdate = "%s zit op Twitter sinds %s\n" % (person, date)
    twitterdates.write(twitterdate)

people.close()
twitter.close()
twitterdates.close()