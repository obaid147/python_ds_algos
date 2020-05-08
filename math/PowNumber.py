def powerOfNumber(base, result, exp):
    if exp == 0:
        return result
    else:
        return powerOfNumber(base, base * result, exp - 1)


base = 2
result = 1
exp = int(input("Enter a number: "))

print(powerOfNumber(base, result, exp))