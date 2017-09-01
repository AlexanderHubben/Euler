a = 0
b = 1
sum = 0
while a < 4000000 and b < 4000000:
    a += b
    if a % 2 == 0:
        sum += a
    b += a
    if b % 2 == 0:
        sum += b
print(sum)
