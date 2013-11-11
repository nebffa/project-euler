def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

    
numbers = []
for a in range(2, 101):
    for b in range(2, 101):    
        numbers.append(a ** b)


numbers.sort()
numbers = f7(numbers)
    
print len(numbers)