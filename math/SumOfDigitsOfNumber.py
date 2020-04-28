# iterative
def method1():
    n = 123
    x = 0
    while n > 0:
        rem = n % 10
        n //= 10
        x = x + rem
    print(x)


# recursive
def method2(n, x):
    if n > 0:
        rem = n % 10
        return method2(n//10, x+rem)
    else:
        return x


if __name__ == '__main__':
    print(method2(123, 0))