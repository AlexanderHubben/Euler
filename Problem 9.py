import math
for a in range (1,1000):
    for b in range(a,1000):
        if (math.sqrt((a * a) + (b * b)) + a + b) == 1000:
            print(a*b*(1000-(a+b)))
