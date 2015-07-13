people = open("people.txt")

for person in people:
    print person

allpeople = people.readlines()
print allpeople

people.close()