def leftRotateMethod3(array, rotateBy):
    rotate1(array)
    rotate2(array)
    pass


def rotate1(array, n):
    array[0], array[1]

def rotate2(array):
    # for i in range(n+1, len(array)):
    array.reverse()


# def leftRotateSecMethod(array, rotateBy):
#     for i in range(rotateBy):
#         Rotate(array)
#
#
# def Rotate(array):
#     temp = array[0]
#     for i in range(len(array)-1):
#         array[i] = array[i+1]
#     array[-1] = temp
#
#
# def leftRotateFirstMethod(arr, rotateBy):
#     newArray = []
#     # Time complexity: O(n)
#     # Space complexity: O(rotateBy)
#     for i in range(len(arr)):
#         if i < rotateBy:
#             newArray.append(arr[i])
#         else:
#             arr[i - rotateBy] = arr[i]
#
#     for i in range(rotateBy):
#         if rotateBy == 7:
#             break
#         arr[len(arr) - (rotateBy - i)] = newArray[i]


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
        leftRotateMethod3(array, n)
        print("After Rotation", array)
        print("----------------------")
    except ValueError:
        print("Enter a Number")
    except IndexError:
        print("Enter a valid Number")


