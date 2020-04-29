def method1(number):
    num = 1006
    x = 1
    inp = num
    while inp > 0:
        rem = inp % 10
        if rem == 0:
            num = num + x * number
        x *= 10
        inp //= 10
    print(num)


def method2(number):
    string = str(1006)
    newStr = ""
    for i in range(len(string)):
        if string[i] == '0':
            newStr = newStr + str(number)
        else:
            newStr = newStr + string[i]
    print(newStr)


if __name__ == '__main__':
    number = int(input("Enter a Number: "))
    # method1(number)
    method2(number)