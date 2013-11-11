ways = 0


aList = range(200, -1, -200)
for a in aList:
    
    bList = range(200 - a, -1, -100)
    for b in bList:
        cList = range(200 - a - b, -1, -50)
        for c in cList:
            dList = range(200 - a - b - c, -1, -20)
            for d in dList:
                eList = range(200 - a - b - c - d, -1, -10)
                for e in eList:
                    fList = range(200 - a - b - c - d - e, -1, -5)
                    for f in fList:
                        gList = range(200 - a - b - c - d - e - f, -1, -2)
                        for g in gList:
                            hList = range(200 - a - b - c - d - e - f - g, -1, -1)
                            for h in hList:
                                print hList
                                if a + b + c + d + e + f + g + h == 200:
                                    
                                    ways += 1
                                    
print ways
