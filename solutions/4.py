fruit = raw_input("Noem eens een vrucht?")

print "De eerste letter is een " + fruit[0]

if fruit[0] == "a" or fruit[0] == "e":
    print "Eerste letter is een a of e"

print "Zonder eerste karakter " + fruit[1:]

fruit_b = "b" + fruit[1:]
print "Met een 'b': " + fruit_b

print "Tweede tot vierde letter " + fruit[1:2]

print "En nu alle letters!"

for char in fruit:
    print char