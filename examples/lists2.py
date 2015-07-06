birthdays = [
    ["Hay", 1983],
    ["Lotte", 1981],
    ["Jesse", 1985]
]

print birthdays[0]
print birthdays[0][1]

for bday in birthdays:
    print "%s is jarig in %s" % (bday[0], bday[1])

