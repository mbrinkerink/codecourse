def shownames(filename, remark):
    f = open(filename)

    for item in f: # Verwijder newline
        item = item.strip()
        print "%s is %s!" % (item, remark)

if __name__ == "__main__":
    shownames("people.txt", "echt super")
    print "---" * 10
    shownames("people2.txt", "werkelijk briljant")