# O(n)
def powerOfNumber(base, exp):
    if exp == 0:
        return 1
    else:
        return base * powerOfNumber(base, exp - 1)


#
def powerOfNumRec(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        r = powerOfNumRec(base, exp/2)
        return r * r
    else:
        return base * powerOfNumRec(base, exp-1)


base = 2
exp = int(input("Enter a number: "))

# print(powerOfNumber(base, exp))
print(powerOfNumRec(base, exp))