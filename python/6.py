sumStack = 0

for i in range(1, 101):
    for j in range(i + 1, 101):
        sumStack += i * j

sumStack *= 2

print "sumStack = %d" % sumStack