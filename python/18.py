triangle = [
[75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[95, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[17, 47, 82, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[18, 35, 87, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[20, 4, 82, 47, 65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[19, 1, 23, 75, 3, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[88, 2, 77, 73, 7, 63, 67, 0, 0, 0, 0, 0, 0, 0, 0],
[99, 65, 4, 28, 6, 16, 70, 92, 0, 0, 0, 0, 0, 0, 0],
[41, 41, 26, 56, 83, 40, 80, 70, 33, 0, 0, 0, 0, 0, 0],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 0, 0, 0, 0, 0],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 0, 0, 0, 0],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 0, 0, 0],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 0, 0],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 0],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]


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


lengthTriangle = len(triangle)
for i in range(1, lengthTriangle):
    # move up a level
    triangle = addBase(triangle)
    # now remove the previous level
    triangle = reduceTriangle(triangle)
    
print triangle[0][0]