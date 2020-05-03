def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibSeries(til):
    for i in range(til + 1):
        print(i, "th : ", fibUsingCaching(i))


def fibUsingCaching(n):

    if cache[n] != 0:
        return cache[n]
    if n <= 1:
        cache[n] = n
        return cache[n]
    else:
        cache[n] = fibUsingCaching(n-1) + fibUsingCaching(n-2)
        return cache[n]

# TC: O(n)


def nthFiboIterative(n):
    a = 0
    b = 1
    c = 0
    while c < n:
        a, b = b, a+b
        c += 1
    return a


cache = [0] * 101
till = int(input("Enter till: "))
fibSeries(till)