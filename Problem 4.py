maximum = 0
for x in range(100,1000):
    for y in range(100,1000):
        if x*y > maximum:
            string1=str(x*y)
            if(list(string1))==(list(reversed(string1))):
                maximum = int(string1)
print maximum
