a = raw_input("Welkom bij de SWIEBERTJE QUIZ! Wat is je naam?  ")
print "welkom " + a + "  wat een mooie naam. High five voor je moeder en vader!" 
print "Zo nu gaan we lekker quizzen"
print "---------------THE QUIZZZZ--------------------------------"

goed = 0

vraag1 = raw_input("Vraag 1: wanneer was Swiebertje op tv?  ")
b = int(vraag1) 
if b in range(1955, 1975):
	goed = goed + 1
else: None
print "--------------------------------------------------------"	
vraag2 = raw_input("Vraag 2: Wie speelde Swiebertje?  ") 
c = str(vraag2)
if c == "joop" or c == "doderer" or c == "Joop" or c == "Doderer":
	goed = goed + 1
else: None
print "--------------------------------------------------------"
print "SCORE--SCORE--SCORE--SCORE--SCORE--SCORE--SCORE--SCORE"
print str(goed) + "...antwoorden goed"
print str(2 - goed) + "...antwoorden fout"
print "--------------------------------------------------------"
if goed == 2:
	print "Ajetoh! GEWONNEN! twee antwoorden goed"
else: None

if goed == 1:
	print "BIJNA! oeiiiii, maar eentje goed"
else: None

if goed == 0:
	print "VERLOREN! zuchttttt, ga maar lekker swieberen jij!"
else: None 