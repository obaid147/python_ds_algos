my_str = 'mada'
new_str = ""
for i in my_str:
    new_str = i + new_str

print(my_str)
print(new_str)
if new_str == my_str:
    print('palindrome')
else:
    print("Not Palindrome")
