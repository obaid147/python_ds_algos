import time

arr = [1, 2, 3, 4, 5, 6]
i = 0
while True:
    time.sleep(1)
    print(arr[i % len(arr)])
    i += 1
