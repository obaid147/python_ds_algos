num = str(input("Enter a number: "))


def method1():
    flag = False
    for i in range(len(num)):
        if num[i] == '1' or num[i] == '0':
            flag = True
        else:
            flag = False
            return flag
    return flag


print(method1())