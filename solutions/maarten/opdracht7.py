filmlijst = [
	{
		"titel" : "Film1",
		"jaar" : 2001
	},
	{
		"titel" : "Film2",
		"jaar" : 2002
	}
]

film_titel = raw_input("Noem een filmtitel:")
film_jaar = raw_input("In welk jaar verscheen deze film?")
film_jaar = int(film_jaar)
filmlijst.append(
	{
		"titel" : film_titel, 
		"jaar" : film_jaar
	}
)

for film in filmlijst:
	print film["titel"].upper()	
	print film["jaar"]
# Er was een beter manier om dit te doen, maar dit weet ik niet meer.
	print 2015-film["jaar"]