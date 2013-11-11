import time

t = time.time()

n, d = 7, 5
n_previous, d_previous = 3, 2
numb_times = 0
for i in range(1, 1000):
    if len(str(n)) > len(str(d)):
        numb_times += 1
    tmp_n, tmp_d = n, d
    n, n_previous = 2 * n + n_previous, tmp_n
    d, d_previous = 2 * d + d_previous, tmp_d
    
print numb_times
print time.time() - t