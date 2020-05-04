def m1(arr, key):
    count = 0
    for i in range(len(arr)):
        if key <= arr[i]:
            count += 1
    return count


def m2(arr, key):
    low = 0
    high = len(arr)
    count = 0
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return high - mid

        if arr[mid] <= key:
            high = mid - 1
        else:
            count = mid + 1
            low = mid + 1
    return count


# array = [1, 2, 2, 2, 3, 4]  # ip 3, op 5
array = [1, 2, 3, 4, 5, 6, 7]  # ip 2 op 6

n = int(input("Enter a number: "))
# print(m1(array, n))
print(m2(array, n))