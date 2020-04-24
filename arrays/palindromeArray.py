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


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 2, 1]
    method1(arr)
