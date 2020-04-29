index = int(input("Enter Index: "))

a, b = 0, 1
count = 0

if index == a:
    print(a)
elif index == b:
    print(b)
else:
    while count < index:
        a, b = b, a + b
        count += 1
    print(a)
