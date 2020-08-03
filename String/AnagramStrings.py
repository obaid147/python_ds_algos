def stringAnagram():
    s1 = 'Aamir'
    s2 = 'mariA'

    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


print(stringAnagram())