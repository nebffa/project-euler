import csv
import time

t = time.time()

def lines_intersect(point1, point2, adjusted_midpoint):
    line1 = (point1, point2)
    line2 = ((0.0, 0.0), adjusted_midpoint)
    EPS = 1e-02

    x1 = line1[0][0]
    y1 = line1[0][1]
    x2 = line1[1][0]
    y2 = line1[1][1]

    x3 = line2[0][0]
    y3 = line2[0][1]
    x4 = line2[1][0]
    y4 = line2[1][1]

    denom  = (y4-y3) * (x2-x1) - (x4-x3) * (y2-y1)
    numera = (x4-x3) * (y1-y3) - (y4-y3) * (x1-x3)
    numerb = (x2-x1) * (y1-y3) - (y2-y1) * (x1-x3)


    # Are the line coincident? 
    if abs(numera) < EPS and abs(numerb) < EPS and abs(denom) < EPS:
        return True

    # Are the line parallel 
    if abs(denom) < EPS:
        return False

    # Is the intersection along the the segments
    mua = numera / denom
    mub = numerb / denom
    # AM - use equality here so that "on the end" is not an
    # intersection; use strict inequality if "touching at end" is an
    # intersection */
    if mua < 0 or mua > 1 or mub < 0 or mub > 1:
        return False

    return True



file = open('triangles.txt', 'r')
triangles = []
for triangle in csv.reader(file):
    points = [int(coordinate) for coordinate in triangle]
    triangles.append(((points[0], points[1]), (points[2], points[3]), (points[4], points[5])))

count = 0
for triangle in triangles:
    contains_origin = True
    centroid = (1.0 * sum([point[0] for point in triangle]) / 3, 1.0 * sum([point[1] for point in triangle]) / 3)

    for i in range(0, 3):
        point1 = triangle[i]
        point2 = triangle[(i + 1) % 3]

        # see if the line between point1-point2 and the origin-(just beyond the midpoint of point1-point2) intersect
        # if all such lines intersect, then the triangle contains the origin

        # the midpoint of the edge
        midpoint = (0.5 * (point1[0] + point2[0]), 0.5 * (point1[1] + point2[1]))

        # we need to find the gradient between the midpoint and the centroid of the triangle, in order to find a point just outside the triangle
        if (midpoint[0] - centroid[0]) == 0:
            gradient = "NaN"
        else:
            gradient = (midpoint[1] - centroid[1]) / (midpoint[0] - centroid[0])

        # create a point just outside of the triangle
        if gradient == "NaN":
            if (midpoint[1] - centroid[1]) > 0:
                adjusted_midpoint = (midpoint[0], midpoint[1] + 1)
            else:
                adjusted_midpoint = (midpoint[0], midpoint[1] - 1)  
        elif (midpoint[0] - centroid[0]) > 0:
            adjusted_midpoint = (midpoint[0] + 0.1, midpoint[1] + 0.1 * gradient)
        elif (midpoint[0] - centroid[0]) < 0:
            adjusted_midpoint = (midpoint[0] - 0.1, midpoint[1] - 0.1 * gradient)
        

        # if the midpoint-origin line does not intersect with any edge of the triangle, then the triangle does not contain the origin
        if not lines_intersect(point1, point2, adjusted_midpoint):
            contains_origin = False

    if contains_origin:
        count += 1

print count
print time.time() - t
