index = int(input("Enter Index: "))

a, b, c = 0, 1, 0

while c < index:
    a, b = b, a + b
    c += 1
print(a)

