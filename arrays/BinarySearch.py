def binary_search(arr, num):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == num:
            return "Found"
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return "Not Found"


arr = [1, 6, -2, 5, 4, 40, 3]
num = int(input("Enter a number: "))  # 3
arr.sort()
# [-2, 1, 3, 4, 5, 6, 40]
print(binary_search(arr, num))
