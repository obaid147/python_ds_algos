array1 = [1, 2, 3, 4, 5]
array2 = [1, 2, 3, 4]
i = i+2
for i in range(1, len(array1) + 1):
    if i & 1:
        print(i, end=' ')
print()
# =====================================


# ======================================

nums = [1, 0, 0, 4]
nums1 = [1, 2, 1]
for i in range(len(nums)):
    if nums[i] == 0:
        nums[i] = 5
print(nums)
