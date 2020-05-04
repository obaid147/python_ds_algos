def charOfString():
    for i in range(len(str1)):
        for j in range(1, len(str1)):
            if str1[i] != str1[j]:
                return 'NO'
    return 'Yes'


str1 = 'oom'
print(charOfString())