def method1(number, convertTo):
    x = 1
    inp = number
    while inp > 0:
        rem = inp % 10
        if rem == 0:
            number = number + x * convertTo
        x *= 10
        inp //= 10
    print(number)


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
    t = int(input("Enter number of test cases: "))
    while t > 0:
        number = int(input("Enter a number with zeros: "))
        convertToNumber = int(input("Enter number to replace 0 with:"))
        method1(number, convertToNumber)
        t -= 1
        #todo update method2 accordding tomethod1
        # method2(number, convertToNumber)
