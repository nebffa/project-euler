# question statement is too big to put here
# here's a link: http://projecteuler.net/problem=101

import sympy
import time

t = time.time()

n = sympy.Symbol('n')
c0, c1, c2, c3, c4, c5, c6, c7, c8, c9 = sympy.symbols(['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9'])
equations = {
    0: c0,
    1: c0 + c1*n,
    2: c0 + c1*n + c2*n**2,
    3: c0 + c1*n + c2*n**2 + c3*n**3,
    4: c0 + c1*n + c2*n**2 + c3*n**3 + c4*n**4,
    5: c0 + c1*n + c2*n**2 + c3*n**3 + c4*n**4 + c5*n**5,
    6: c0 + c1*n + c2*n**2 + c3*n**3 + c4*n**4 + c5*n**5 + c6*n**6,
    7: c0 + c1*n + c2*n**2 + c3*n**3 + c4*n**4 + c5*n**5 + c6*n**6 + c7*n**7,
    8: c0 + c1*n + c2*n**2 + c3*n**3 + c4*n**4 + c5*n**5 + c6*n**6 + c7*n**7 + c8*n**8,
    9: c0 + c1*n + c2*n**2 + c3*n**3 + c4*n**4 + c5*n**5 + c6*n**6 + c7*n**7 + c8*n**8 + c9*n**9
}


u = 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10


sequences = [[1]]
for sequence_length in range(2, 10 + 1):
    sequences.append(sequences[-1] + [u.subs({n: sequence_length})])

total = 0
for i in range(0, 10):
    sequence = sequences[i]
    equation = equations[i]

    simultaneous_equations = [equation.subs({n:(j + 1)}) - sequence[j] for j in range(0, i + 1)]
    constants = sympy.solve(simultaneous_equations)

    equation = equation.subs(constants)
    
    total += equation.subs({n:(i+2)})


print total
print time.time() - t