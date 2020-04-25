s = 'madam'
flag = True
j = -1
size = len(s)
for i in range(size):
    if s[i] != s[j]:
        flag = False
        break
    else:
        j -= 1

if flag:
    print('Palindrome')
else:
    print('Not palindrome')
