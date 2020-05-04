def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    for i in string:
        if i in vowels:
            # string[i] = '' It shows item assignment not possible
            string = string.replace(i, "")
    print(string)


while True:
    str1 = input("Enter a String: ")
    remove_vowels(str1)