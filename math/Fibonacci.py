def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibSeries(til):
    for i in range(til + 1):
        print(i, "th : ", fib(i))


till = int(input("Enter till: "))
print(fibSeries(till))