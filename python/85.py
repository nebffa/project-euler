from time import time

t = time()

closest_distance = 10 ** 7
for n in range(1000):
    for m in range(1000):
        smaller_rectangles_count = n * (n + 1) * m * (m + 1) / 4
        
        if closest_distance > abs(smaller_rectangles_count - 2 * 10 ** 6):
            closest_distance = abs(smaller_rectangles_count - 2 * 10 ** 6)
            closest_big_rectangle_area = m * n
            

print closest_big_rectangle_area
print time() - t