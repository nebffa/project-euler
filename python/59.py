import itertools, time, csv

t = time.time()

with open("cipher1.txt", 'rb') as f:
    encrypted = csv.reader(f, delimiter = ',').next()
    
    
passwords = list(itertools.product('abcdefghijklmnopqrstuvwxyz', repeat = 3))

for password in passwords:
    n = 0
    decrypted = []
    
    for i in range(0, len(encrypted)):
        decrypted.append(int(encrypted[i]) ^ ord(password[i % 3]))
        
    the = 0
    for i in range(0, len(decrypted)):
        if chr(decrypted[i]) == 'T' or chr(decrypted[i]) == 't':
            if chr(decrypted[i + 1]) == 'h':
                if chr(decrypted[i + 2]) == 'e':
                    the += 1
                    
    if the >= 20:
        tmp = []
        sum_total = 0
        for i in decrypted:
            tmp.append(chr(i))
            sum_total += i
        print tmp
        print the
        print sum_total
        print password
        print time.time() - t
        raw_input()