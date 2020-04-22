def computeGCD(n1, n2):
    while n2:
        n1 = n2
        n2 = n1 % n2

    return n1


print("GCD = ", computeGCD(6, 2))