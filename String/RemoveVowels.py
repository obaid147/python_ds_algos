def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    str1 = ""
    for i in string:
        if i in vowels:
            # string[i] = '' It shows item assignment not possible
            str1 = str1 + string[i]
    print(str1)


while True:
    str1 = input("Enter a String: ")
    remove_vowels(str1)