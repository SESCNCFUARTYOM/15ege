def d(n, m):
    return n%m == 0

for a in range(1, 500):
    for x in range(1, 500):
        if not((a % 45 == 0) and ((750 % x == 0) <= ((a % x != 0) <= (120 % x != 0)))):
            break
    else:
        print(a)
        break
    
