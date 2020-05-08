inp = input("Enter a String: ")

if inp[0] >= 'A' and inp[0] <='Z':
    inp = inp.upper()
else:
    inp = inp.lower()

print(inp)