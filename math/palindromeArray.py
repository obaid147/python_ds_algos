array = [1, 2, 3, 3, 2, 1]
i = 0
j = len(array) - 1
flag = False
while i < j:
    if array[i] == array[j]:
        i = i + 1
        j = j - 1
        flag = True
    else:
        flag = False
        break
if flag:
    print(array, 'is Palindrome')
else:
    print(array, 'is  not Palindrome')