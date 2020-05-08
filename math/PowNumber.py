# O(n)
def powerOfNumber(base, exp):
    if exp == 0:
        return 1
    else:
        return base * powerOfNumber(base, exp - 1)


# logarithmic
def powerOfNum(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        r = powerOfNum(base, exp/2)
        return r * r
    else:
        return base * powerOfNum(base, exp-1)


base = 2
exp = int(input("Enter a number: "))

print(powerOfNumber(base, exp))
# print(powerOfNum(base, exp))