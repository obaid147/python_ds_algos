def binary_search(arr, num):
    low = 0
    high = len(arr)-1

    for i in range(low, high):
        mid = low + (high - low) // 2 # low + high / 2
        if arr[mid] == num:
            return "Found"
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return "Not Found"


array = [1, 10, 5, 6, 7]
search = int(input("Enter a number to search: "))
array.sort()
print(binary_search(array, search))
