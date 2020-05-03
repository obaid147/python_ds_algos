def m1():
    count = 0
    for i in range(len(arr)-1):
        if arr[i] <= n:
            count += 1
    return count


arr = [1, 2, 2, 2, 3, 4]  # ip 3, op 5
# arr = [1,2,3,4,5,6,7,8,9]  # ip 9 op 9

n = int(input("Enter a number: "))
print(m1())