print "Welkom bij de grrrrote Swiebertje-quiz!"
name = raw_input("Hoe heet je?")
print "Welkom " + name + "!"
question1 = raw_input("Noem een willekeurig jaar waarin Swiebertje op tv was")
answer1 = range(1955, 1976)
correct = "goed!"
score = 0
if (question1 == answer1):
  print correct
  score = score + 1
else:
  print "helaas,dit antwoord is niet juist."
question2 = raw_input("Wie speelde Swiebertje?")
answer2 = "Joop"
answer3 = "Doderer"
if str(question2) == answer2:
  print correct
  score = score + 1
if str(question2) == answer3:
  print correct
  score = score + 1
else:
  print "helaas, dit antwoord is niet juist!"
if int(score) == 2:
  print "gefeliciteerd", name ," je hebt gewonnen met een score van ", score, "en gaat door voor de wasmachine!"
if int(score) < 2:
  print "Helaas", name ," je hebt verloren met een score van", score,": loosah!"
	  