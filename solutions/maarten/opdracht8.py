people = open("people.txt")
people_list = people.readlines()
twitter = open("twitter.txt")
twitter_list = twitter.readlines()
combi = open("combi.txt", "w")

for index in range(len(people_list)):
	person = people_list[index].strip()
	date = twitter_list[index].strip()
	person_and_date =  "%s zit sinds %s op Twitter.\n" % (person, date)
	combi.write(person_and_date)
	
people.close()
twitter.close()
combi.close()