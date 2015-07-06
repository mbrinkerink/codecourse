birthdays = [
    ["Hay", 1983],
    ["Lotte", 1981],
    ["Jesse", 1985]
]

print birthdays[0] # ["Hay", 1983]
print birthdays[0][1] # 1983

for bday in birthdays:
    name = bday[0]
    year = bday[1]
    print "%s is jarig in %s" % (name, year)

