vrucht = raw_input("Geef de naam van een vrucht:")
print vrucht[0]
if vrucht[0] == "a":
	print "Het is een 'a'"
elif vrucht[0] == "e":
	print "Het is een 'e'"
print vrucht[1:]
print "b" + vrucht[1:]
print vrucht[1:3]
for vrucht_achterelkaar in vrucht:
	print vrucht_achterelkaar