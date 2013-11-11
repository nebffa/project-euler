import time
import sympy

t_time = time.time()

def normal(x, y):
    t = sympy.Symbol('t')
    slope = sympy.Rational(-x, y)
    
    return slope * t + y - x * slope
    
length = 50
n_triangles = length ** 2
f = sympy.Function('f')
for x in range(0, length + 1):
    for y in range(0, length + 1):
    
        if x == 0 and y == 0:
            continue
        elif x == 0 or y == 0:
            n_triangles += length
            continue
        
        f = normal(x, y)
        for x_coord in range(0, length + 1):
            if x == x_coord:
                continue
        
            t = sympy.Symbol('t')
            y_coord = f.evalf(subs = {t: x_coord})
            
            if -0.00001 <= int(y_coord) - y_coord <= 0.00001 and 0 <= int(y_coord) <= length:
                n_triangles += 1
                
            

print n_triangles
print time.time() - t_time