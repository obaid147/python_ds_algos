def powerOfNumber(cons, inp):
    # res = 2**num
    # print(res)
    print("2^{} is: {}".format(inp, cons**inp))


constant = 2
inputNum = int(input("Enter a number: "))
powerOfNumber(constant, inputNum)