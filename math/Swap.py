def method1():
    x = 1
    y = 2
    print("Before swap x = ", x, ' y =  ', y)
    x = x + y
    y = x - y
    x = x - y
    print("After  swap x = ", x, ' y =  ', y)


def method2():
    x = 1
    y = 2
    print("Before swap x = ", x, ' y =  ', y)
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print("After  swap x = ", x, ' y =  ', y)


# method1()
method2()
