import csv

# read in text file
with open("words.txt", 'rb') as f:
    line = csv.reader(f).next()
	
line.sort()

triangles = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276]
wordsSum = 0
for i in range(0, len(line)):
    # split each name into a list of its letters
    name = list(line[i])
    # set sum of characters in the name to 0
    wordSum = 0
    
    for j in range(0, len(name)):
        wordSum += ord(name[j]) - 64
		
    for j in range(0, len(triangles)):
		if wordSum == triangles[j]:
			wordsSum += 1
			break
			

			
print wordsSum
