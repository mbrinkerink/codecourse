import json

jsondata = open("rijksmuseum.json").read()
data = json.loads(jsondata)
paintings = []

for row in data["rows"]:
    value = row["value"]

    painting = {
        "title" : value["title"],
        "date" : value.get("date", None),
        "creator" : value["creator"],
    }

    paintings.append( painting )

paintingsfile = open("paintings.json", "w")
paintingsjson = json.dumps(paintings)
paintingsfile.write(paintingsjson)