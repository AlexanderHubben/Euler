tot=0
for x in range(0,1001):
    if x % 3 == 0 or x % 5 == 0:
        tot+=x
print(tot)
