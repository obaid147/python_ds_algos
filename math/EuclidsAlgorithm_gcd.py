def method1(n1, n2):
    while n2:
        n1 = n2
        n2 = n1 % n2

    return n1


print("GCD = ", method1(6, 2))