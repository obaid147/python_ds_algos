def m1(arr):
    count = 0
    for i in range(len(arr)-1):
        if arr[i] <= num:
            count += 1
    return count


def m2(arr, n, key):
    low = 0
    high = n - 1
    count = 0

    while low <= high:
        mid = int((high + low) / 2)

        if arr[mid] <= key:
            count = mid + 1
            low = mid + 1
        else:
            high = mid - 1
    return count


# array = [1, 2, 2, 2, 3, 4]  # ip 3, op 5
array = [1, 2, 3, 4, 5, 6, 7]  # ip 9 op 7

num = int(input("Enter a number: "))
print(m2(array, len(array), num))