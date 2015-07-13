with open("people.txt") as people:
    for person in people:
        print person

with open("people.txt") as people:
    allpeople = people.readlines()
    print allpeople

