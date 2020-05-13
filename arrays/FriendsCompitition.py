def competition(person1, person2, person1Score, person2Score):
    if len(person1) != len(person2):
        return 'Cannot Compare'
    else:
        for i in range(len(person1)):
            if person1[i] > person2[i]:
                person1Score += 1
            elif person1[i] < person2[i]:
                person2Score += 1
    return person1Score, person2Score


if __name__ == '__main__':
    # person1 = [4, 2, 7]
    # person2 = [5, 6, 3]
    person1 = [4, 2, 7]
    person2 = [5, 2, 8]
    person1Score = 0
    person2Score = 0
    res = competition(person1, person2, person1Score, person2Score)
    print(res)