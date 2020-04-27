# TC --> O(n) aux-space O(1)
def method1(array):
    flag = True
    i = 0
    j = len(arr) - 1
    while i < j:
        if array[i] != array[j]:
            flag = False
            break
        else:
            i = i + 1
            j = j - 1
            flag = True
    if flag:
        print(array, 'is Palindrome')
    else:
        print(array, 'is  not Palindrome')


def reverse(a):
    j = a
    rev = 0
    while j > 0:
        rem = j % 10
        rev = rev * 10 + rem
        j //= 10
    return rev


# Tc O(n)
def method2(array1):
    for i in range(len(array1)):
        if array1[i] != reverse(array1[i]):
            return False
        else:
            continue
    return True


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 2, 1]
    # method1(arr)
    array1 = [111, 222, 333, 444, 555]
    print(method2(array1))
