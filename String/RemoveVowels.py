def remove_voewls(string):
    vowels = 'aeiouAEIOU'
    for i in string:
        if i in vowels:
            # string[x] = '' It shows item assignment not possible
            string = string.replace(i, "")
    print(string)


while True:
    str1 = input("Enter any string to remove all vowels from it: ")
    remove_voewls(str1)
