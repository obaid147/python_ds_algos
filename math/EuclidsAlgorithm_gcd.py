# Euclid's Algorithm Loop
def method1(n1, n2):
    while n2:
        '''This way it's not working'''
        # n1 = n2
        # n2 = n1 % n2
        '''it works this way though that i dont know how'''
        n1, n2 = n2, n1 % n2

    return n1


# Euclid's Algorithm Recursion
def method2(n1, n2):
    if not n2:
        return n1
    else:
        return method2(n2, n1 % n2)


print(method1(48, 18))