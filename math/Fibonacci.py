def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fiboSeries(till):
    for i in range(till + 1):
        print(i , "th : ", fib(i))

till = int(input("Enter till: "))

print(fiboSeries(till))