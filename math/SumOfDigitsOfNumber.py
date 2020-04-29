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
    if n == 0:
        return sum
    else:
        return method2(n//10, sum + (n % 10))


if __name__ == '__main__':
    t = int(input("Enter number of test cases: "))
    while t > 0:
        number = int(input("Enter number to calculate sum:"))
        result = method2(number, 0)
        print("sum of digits is: ", result)
        t -= 1