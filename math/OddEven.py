def method1(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


def method2(num):
    if num & 1 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == '__main__':
    number = int(input("Enter a number: "))
    # method1(number)
    method2(number)
