hello = "Hallo  "
world = "Wereld"
helloworld = "%s, %s!"

print hello.lower()
print world.upper()
print hello[0].isupper()
print hello[-1].isupper()
print hello.strip()

print "allo" in hello
print helloworld % (hello, world)