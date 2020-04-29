index = int(input("Enter Index: "))

n1, n2 = 0, 1
count = 0

if index == n1:
    print(n1)
elif index == n2:
    print(n2)
else:
    while count < index:
        n1, n2 = n2, n1+n2
        count += 1
    print(n1)
