# Euclid's Algorithm Loop
def method1(n1, n2):
    while n2:
        rem = n1 % n2
        if rem == 0:
            break
        n1 = n2
        n2 = rem

    return n2


# Euclid's Algorithm Recursion
def method2(n1, n2):
    if not n2:
        return n1
    else:
        return method2(n2, n1 % n2)


print(method1(21, 13))