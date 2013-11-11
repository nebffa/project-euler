value = 1

array = [9]
arrayStop = 0
while len(array) != 7:
    array.append(array[-1] + (len(array) + 1) * 9 * 10 ** (len(array)))
    
numbers = [10, 100, 1000, 10000, 100000, 1000000]
for i in numbers:
    for j in range(0, len(array)):
        if i < array[j]:
            value *= int(str(((i - array[j - 1]) / (j + 1) + + 10 ** j))[(i - array[j - 1]) % (j + 1) - 1])
            break

print value
