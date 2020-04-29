# iterative
def method1():
    n = 123
    sum = 0
    while n > 0:
        rem = n % 10
        n //= 10
        sum = sum + rem
    return sum


# recursive
def method2(n, sum):
    if n > 0:
        rem = n % 10
        return method2(n//10, sum+rem)
    else:
        return sum


if __name__ == '__main__':
    print(method1())
    print(method2(5231, 0))