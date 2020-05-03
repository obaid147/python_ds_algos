def binary_search(arr, num):
    low = 0
    high = len(arr)-1

    for i in range(low, high):
        mid = low + (high - low) // 2   # low + high / 2
        if arr[mid] == num:
            return "Found"
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return "Not Found"


def binary_search_recursion(arr, find, high, low, mid):

    if low > high:
        return 'Not found'
    if arr[mid] == find:
        return 'Found'

    if arr[mid] < find:
        return binary_search_recursion(arr, find, high, mid+1, low+(high-low)//2)
    else:
        return binary_search_recursion(arr, find, mid - 1, low, low+(high-low)//2)


array = [2, 10, 5, 6, 7]
search = int(input("Enter a number to search: "))
array.sort()
# [2, 5, 6, 7, 10]
low = 0
high = len(array)-1
mid = low + (high - low) // 2
print(binary_search_recursion(array, search, high, low, mid))
# print(binary_search(array, search))
