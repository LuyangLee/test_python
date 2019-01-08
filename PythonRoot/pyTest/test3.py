import math
a = []
for x1 in range(1, int(math.sqrt(168)) + 1):
    if 168 % x1 == 0:
        x2 = 168 // x1
        if (x1 + x2) % 2 == 0 and (x2 - x1) % 2 == 0:
            n = (x1 + x2) / 2
            m = (x2 - x1) / 2
            a.append(math.pow(m,2) - 100)
print(a)
        
        