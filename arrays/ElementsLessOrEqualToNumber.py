def m1():
    count = 0
    if n in arr:
        for i in arr:
            if i <= n:
                count += 1
        return count
    else:
        return f"{n} Not Found"


size = int(input("Enter Size of array: "))
arr = []
for i in range(size):
    n = int(input(f"Enter index {i} Int Array Element\n"))
    arr.append(n)
arr.sort()
n = int(input("Enter a number: "))
print(m1())