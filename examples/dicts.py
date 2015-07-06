person = {
    "name" : "Hay",
    "birthyear" : 1983
}

print "%s is geboren in %s" % (person["name"], person["birthyear"])

persons = [
    {
        "name" : "Hay",
        "birthyear" : 1983
    },
    {
        "name" : "Lotte",
        "birthyear" : 1981
    }
]

for person in persons:
    name = person["name"]
    birthyear = person["birthyear"]
    print "%s is geboren in %s" % (name, birthyear)

