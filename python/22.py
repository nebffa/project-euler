import csv

# read in text file
with open("names.txt", 'rb') as f:
    line = csv.reader(f).next()
   
line.sort()

namesSum = 0
for i in range(0, len(line)):
    # split each name into a list of its letters
    name = list(line[i])
    # set sum of characters in the name to 0
    nameSum = 0
    
    for j in range(0, len(name)):
        nameSum += ord(name[j]) - 64
        
    namesSum += (nameSum * (i + 1))
        
print namesSum
