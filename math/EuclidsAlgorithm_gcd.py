def method1(bigNum, smallNum):
    while smallNum:
        bigNum = smallNum
        smallNum = bigNum % smallNum
    print('GCD =', bigNum)


method1(6, 2)