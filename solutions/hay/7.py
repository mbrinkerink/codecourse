movies = [
    {
        "title" : "Blade Runner",
        "year" : 1982
    },
    {
        "title" : "2001: A Space Odyssey",
        "year" : 1968
    }
]

title = raw_input("Noem eens een film?")
year = raw_input("In welk jaar verscheen die film?")

movie = {}
movie["title"] = title
movie["year"] = int(year)

movies.append(movie)

print "Hier zijn de films!"
print "------------------------------------"

for movie in movies:
    title = movie["title"]
    year = movie["year"]

    print "De film is " + title.upper()
    print "Verschenen in " + str(year)
    appeared = str(2015 - year)
    print "Dat is %s jaar geleden" % (appeared)
    print "------------------------------------"