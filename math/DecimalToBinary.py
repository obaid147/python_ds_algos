# iterative....
def method1(s, decimal):
    while decimal > 0:
        rem = decimal % 2
        s = str(rem) + s
        decimal //= 2
        print(int(rem), end='')


# Recursive:
def method2(s, num):
    if num == 0:
        return s
    else:
        rem = num % 2
        s = str(rem) + s
        return method2(s, num // 2)


if __name__ == '__main__':
    decimal = int(input("Enter a Positive Decimal Number: "))
    # method1("", decimal)
    binary = method2("", decimal)
    print("binary: ", binary)
