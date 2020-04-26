array1 = [1, 2, 3, 4, 5]
array2 = [1, 2, 3, 4]

for i in range(len(array1) + 1):
    if i & 1:
        print(i, end=' ')
print()
# =====================================

array1 = [111, 222, 333, 4449, 555]

for i in array1:
    j = i
    rev = 0
    rem = 0
    while j > 0:
        rem = j % 10
        rev = rev * 10 + rem
        j //= 10
    if i == rev:
        continue
    else:
        print(i, 0)

# ======================================

nums = [1, 0, 0, 4]
nums1 = [1, 2, 1]
for i in range(len(nums)):
    if nums[i] == 0:
        nums[i] = 5
print(nums)
