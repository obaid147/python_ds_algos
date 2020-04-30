index = int(input("Enter Index: "))

a = 0
b = 1
c = 0
#TC: O(n)
while c < index:
    a, b = b, a+b
    c += 1
print(a)