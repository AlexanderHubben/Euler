num = 600851475143
factor = 2
while num > 1:
    if num % factor == 0:
        num /= factor
    else:
        factor++
print(factor)
