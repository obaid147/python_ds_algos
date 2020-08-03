s1 = '216266789923456887234799302763999'
s2 = '487123789234546713710763896289349'
l1 = []

# integers = [1, 2, 3]
# strings = [str(integer) for integer in integers]
# a_string = "". join(strings)
# an_integer = int(a_string)
# print(an_integer)
#
for i in reversed(range(len(s1))):
    s3 = int(s1[i]) + int(s2[i])
    temp = s3
    print(temp)