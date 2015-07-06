names = ["Bert", "Ernie", "Pino"]

for name in names:
    print "Aangenaam, " + name

print names[1]
print names[-1]

hellos = []

for name in names:
    hellos.append("Hallo " + name)

for hello in hellos:
    print hello

years = [1983, 1980, 1993]

for year in years:
    print year

print 1983 in years

eighties = range(1980, 1989)

for year in years:
    print "%s in de jaren tachtig? %s" % (year, year in eighties)

things = [42, True, "Hallo"]