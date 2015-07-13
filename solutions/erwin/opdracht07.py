currentyear = 2015
films = [
    {
        "title": "Twelve Monkeys",
        "released": 1995
        },
        {
        "title": "Gone with the Wind",
        "released": 1939
        },
]

film = {}
film["title"] = raw_input("Noem je lievelingsfilm: ")
film["released"] = raw_input("Noem het verschijningsjaar van die film: ")
films.push(film)

for film in films:
    title = film["title"].upper()
    print title
    released = film["released"]
    print released
    print "%s jaar geleden verschenen" % (abs(released-currentyear))