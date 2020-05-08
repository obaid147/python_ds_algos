inp = input("Enter a String: ")

if 'A' <= inp[0] <= 'Z':
    inp = inp.upper()
else:
    inp = inp.lower()

print(inp)