#               Method2
#       Time complexity --> O(n*rotateBy)


def method2(array, rotateBy):
    for i in range(rotateBy):
        rotate2(array)


def rotate2(array):
    temp = array[0]
    for i in range(len(array)-1):
        array[i] = array[i+1]
    array[-1] = temp

#               Method1
#       Time complexity --> O(n) ; aux-space --> O(rotateby) --> O(no of rotations.)
def method1(arr, rotateBy):
    newArray = []
    for i in range(len(arr)):
        if i < rotateBy:
            newArray.append(arr[i])
        else:
            arr[i - rotateBy] = arr[i]

    for i in range(rotateBy):
        if rotateBy == 7:
            break
        arr[len(arr) - (rotateBy - i)] = newArray[i]


while True:
    #use regex to validate if its a number
    array = [1, 2, 3, 4, 5, 6, 7]
    print("Current array ", array)
    print("Press 0 for EXIT")
    try:
        n = int(input("Enter indices to rotate: "))
        if n == 0:
            print("Exiting.....")
            exit(1)
        method1(array, n)
        method2(array, n)
        print("After Rotation", array)
        print("----------------------")
    except ValueError:
        print("Enter a Number")
    except IndexError:
        print("Enter a valid Number")


