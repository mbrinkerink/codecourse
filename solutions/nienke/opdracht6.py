

input1 = str(raw_input("wat is je naam "))
input2 = str(raw_input("hoe heet je buurman/vrouw "))
input3 = str(raw_input("hoe heet je kat "))
input4 = str(raw_input("wat is je favoriete fruit "))

names = [input1, input2, input3, input4]

print " ------------------------"

if input1[0].isupper():
	print "Aangenaam " + input1
else: 
	print "Hoi " + input1

if input2[0].isupper():
	print "Aangenaam " + input2
else: 
	print "Hoi " + input2

if input3[0].isupper():
	print "Aangenaam " + input3
else: 
	print "Hoi " + input3

if input4[0].isupper():
	print "Aangenaam " + input4
else: 
	print "Hoi " + input4
	
print " ------------------------"

print "zit er een 'te' in de lijst?"
woord = "te"
print woord in input1
print woord in input2
print woord in input3
print woord in input4

print " ------------------------"
print "%s is een %s" % (input3, input4.upper())