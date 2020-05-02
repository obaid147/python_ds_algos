till = int(input("Enter till: "))
# TC: O(n)


def nthFibo(n):
    a = 0
    b = 1
    c = 0
    while c < n:
        a, b = b, a+b
        c += 1
    return a


def fiboSeries(till):
    for i in range(till + 1):
        print(i , "th : ", nthFibo(i))


fiboSeries(till)