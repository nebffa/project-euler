latticeSize = 20

import math
totalWays = math.factorial(2 * latticeSize) / (math.factorial(latticeSize) ** 2)

print "total ways = %d" % totalWays