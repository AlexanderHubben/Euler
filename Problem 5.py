factors = {}
total=1
for x in range(1,21):
    number = x
    current = 2
    amount=0
    while number > 1:
        if number % current == 0:
            number /= current
            amount += 1
        else:

            current += 1
            amount = 0

        if amount > 0:
            if current in factors:
                if amount > factors[current]:
                    factors[current] = amount
            else:
                factors[current] = amount
for i in list(factors.keys()):
    total *= pow(i,factors[i])
print total
