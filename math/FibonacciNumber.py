def fibNum(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    print(a)


fibNum(7)