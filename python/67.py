from time import time

t = time()
def addBase(triangle):
    lengthBase = len(triangle)
    
    for i in range(0, lengthBase - 1):
        if triangle[lengthBase - 1][i] >= triangle[lengthBase - 1][i + 1]:
            triangle[lengthBase - 2][i] += triangle[lengthBase - 1][i]
        else:
            triangle[lengthBase - 2][i] += triangle[lengthBase - 1][i + 1]
    
    return triangle
    
def reduceTriangle(triangle):
    lengthBase = len(triangle)

    # remove bottom row
    del triangle[lengthBase - 1]
    # remove last column
    map(lambda x: x.pop(lengthBase - 1), triangle)
        
    return triangle

triangle = [map(int, row.split()) for row in open('triangle67.txt')]
for i in triangle:
    while len(i) < 100:
        i.append(0)

lengthTriangle = len(triangle)
for i in range(1, lengthTriangle):
    # move up a level
    triangle = addBase(triangle)
    # now remove the previous level
    triangle = reduceTriangle(triangle)
    
print triangle[0][0]
print time() - t