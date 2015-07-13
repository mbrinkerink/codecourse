totaal = [
	{
		"naam" : "Armegeddon",
		"jaar" : 1990
	},
	{
		"naam" : "Ace Ventura",
		"jaar" : 1994
	}
]


list1 = {}
list1["naam"] = raw_input("welke film is jouw favoriet?  ")
list1["jaar"] = int(raw_input("in welk jaar verscheen deze film?  "))

totaal.append(list1)

for film in totaal:
	naam = film["naam"]
	jaar = film["jaar"]
	tijd = str(2015 - jaar)
	print "%s is uitgekomen in %s, dat is %s jaar geleden" % (naam.upper(), jaar, tijd)