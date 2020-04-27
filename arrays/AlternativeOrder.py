# TC --> O(n)
def method1(arr):
    for i in range(1, len(arr)+1, 2):
        if i & 1:
            print(i, end=' ')


if __name__ == '__main__':
    array1 = [1, 2, 3, 4, 5]
    array2 = [1, 2, 3, 4]
    method1(array1)