names = ["Bert", "Ernie", "Pino"]

for name in names:
    print "Aangenaam, " + name

print names[1] # "Bert"
print names[-1] # "Pino"

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
    is_eighties = year in eighties
    print "%s in de jaren tachtig? %s" % (year, is_eighties)

# Een list kan meerdere type variabelen door elkaar hebben
things = [42, True, "Hallo"]