num = 1006
r = 0
rem = 0
s = ""
while num > 0:
    rem = num % 10
    r *= 10 + rem
    num //= 10
    if rem == 0:
        rem = 5
    s += str(rem)

x = int(s)
s1 = ""
while x > 0:
    rem = x % 10
    r *= 10 + x
    x //= 10
    s1 += str(rem)
print(s1)