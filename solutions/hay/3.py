name = raw_input("Wat is je naam? ")
times = raw_input("Hoe vaak? ")

if name == "Barrie":
    times = int(times)

    for time in range(0, times):
        print "Welkom!"
else:
    print "Helaas, je bent geen Barrie. Tot ziens"