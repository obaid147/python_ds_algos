def method1(binary):
    decimal = 0
    index = 0
    while binary:
        rem = binary % 10
        decimal += rem * 2**index
        binary //= 10
        index += 1
    print(decimal)


# Recursive:
def method2(index, s, binary):
    if binary == 0:
        return s
    else:
        rem = binary % 10
        s += rem * 2**index
        index += 1
        return method2(index, s, binary // 10)


number = int(input("Enter a binary Number: "))
s, index = 0, 0
decimal = method2(index, s, number)
print(decimal)
