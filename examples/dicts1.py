# Een dict
person = {
    "name" : "Hay",
    "year" : 1983
}

name = person["name"]
year = person["year"]
print "%s is geboren in %s" % (name, year)

# Meerdere dicts in een lijst
persons = [
    {
        "name" : "Hay",
        "year" : 1983
    },
    {
        "name" : "Lotte",
        "year" : 1981
    }
]

# Personen met naam en jaar uitprinten
for person in persons:
    name = person["name"]
    birthyear = person["birthyear"]
    print "%s is geboren in %s" % (name, birthyear)

# De persons list met dicts had je ook net zo goed zo kunnen schrijven
persons = []
persons.push(person) # Let op: person bestaat nog steeds! (zie bovenaan)

person2 = {}
person2["name"] = "Lotte"
person2["year"] = 1981

persons.push(person2)

# En je kan het zelfs zo doen ipv eerst een nieuwe dict aanmaken
persons.push({
    "name" : "Lotte",
    "year" : 1981
})