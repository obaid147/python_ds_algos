# Time Complexity -> O(2n)--> O(n)
def method1(arr, number, temp):
    while temp > 0:
        rem = temp % 2
        temp //= 2
        arr.append(rem)
    print('Binary value of', number, 'is')
    for i in reversed(arr):
        print(i, end='')


# Time Complexity -> O(2n) --> O(n)
def method2(arr, temp):
    if temp == 0:
        return [i for i in reversed(arr)]
    else:
        rem = temp % 2
        temp //= 2
        arr.append(rem)
        return method2(arr, temp)


if __name__ == '__main__':
    number = int(input("Enter a Positive Decimal Number: "))
    temp = number
    arr = []
    # method1(arr, number, temp)
    method2(arr, number)
    for i in reversed(arr):
        print(i, end='')