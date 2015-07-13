with open("people.txt") as f:
    people = f.readlines()

with open("twitter.txt") as f:
    twitter = f.readlines()

with open("twitterdates.txt", "w") as f:
    for index, person in enumerate(people):
        date = twitter[index].strip()
        person = person.strip()
        f.write("%s zit sinds %s op Twitter\n" % (person, date))