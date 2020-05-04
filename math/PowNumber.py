def powerOfNumber(var, inp):
    if inp == 0:
        return 1
    if inp == 1:
        return var
    else:
        return powerOfNumber(var * base, inp - 1)


base = 2
variable = base
inputNum = int(input("Enter a number: "))
print(powerOfNumber(variable, inputNum))