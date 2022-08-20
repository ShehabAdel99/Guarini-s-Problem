# 1 denotes black horses
# 2 denotes white horses
# 0 denotes empty space

counter = 0

#
def printArr(arr):
    for r in arr:
        for c in r:
            print(c, end=" ")
        print()
    print()


def move(arr, x, y, a, b):
    global counter
    arr[a][b] = arr[x][y]
    arr[x][y] = 0
    printArr(arr)
    counter = counter + 1


def goal(arr):
    if (arr == [[2, 2, 2], [0, 0, 0], [0, 0, 0], [1, 1, 1]]):
        return True
    else:
        return False


def specialCase(arr):
    move(arr, 2, 0, 1, 2)
    move(arr, 3, 2, 2, 0)
    move(arr, 2, 0, 0, 1)
    move(arr, 1, 2, 2, 0)
    move(arr, 2, 0, 3, 2)


def deliverWhite(a):
    if a[0][0] == 0:
        if a[3][2] == 2 and a[2][0] == 0 and a[1][2] == 0:
            move(a, 3, 2, 2, 0)
            move(a, 2, 0, 1, 2)
            move(a, 1, 2, 0, 0)
        elif a[3][1] == 2 and a[1][2] == 0:
            move(a, 3, 1, 1, 2)
            move(a, 1, 2, 0, 0)
    elif a[0][1] == 0:
        if a[3][0] == 2 and a[2][2] == 0:
            move(a, 3, 0, 2, 2)
            move(a, 2, 2, 0, 1)
        elif a[3][2] == 2 and a[2][0] == 0:
            move(a, 3, 2, 2, 0)
            move(a, 2, 0, 0, 1)
        else:
            specialCase(a)
    elif a[0][2] == 0:
        if a[3][0] == 2 and a[2][2] == 0 and a[1][0] == 0:
            move(a, 3, 0, 2, 2)
            move(a, 2, 2, 1, 0)
            move(a, 1, 0, 0, 2)
        elif a[3][1] == 2 and a[1][0] == 0:
            move(a, 3, 1, 1, 0)
            move(a, 1, 0, 0, 2)


def deliverBlack(a):
    if a[3][0] == 0:
        if a[0][2] == 1 and a[1][0] and a[2][2] == 0:
            move(a, 0, 2, 1, 0)
            move(a, 1, 0, 2, 2)
            move(a, 2, 2, 3, 0)
        elif a[0][1] == 1 and a[2][2] == 0:
            move(a, 0, 1, 2, 2)
            move(a, 2, 2, 3, 0)
    elif a[3][1] == 0:
        if a[0][0] == 1 and a[1][2] == 0:
            move(a, 0, 0, 1, 2)
            move(a, 1, 2, 3, 1)
        elif a[0][2] == 1 and a[1][0] == 0:
            move(a, 0, 2, 1, 0)
            move(a, 1, 0, 3, 1)
    elif a[3][2] == 0:
        if a[0][0] == 1 and a[1][2] == 0 and a[2][0] == 0:
            move(a, 0, 0, 1, 2)
            move(a, 1, 2, 2, 0)
            move(a, 2, 0, 3, 2)
        elif a[0][1] == 1 and a[2][0] == 0:
            move(a, 0, 1, 2, 0)
            move(a, 2, 0, 3, 2)


def solveBoard(a):
    if (not goal(a)):
        deliverWhite(a)
        deliverBlack(a)
    else:
        return
    solveBoard(a)


a = [[1, 1, 1], [0, 0, 0], [0, 0, 0], [2, 2, 2]]
move(a, 0, 0, 1, 2)
move(a, 1, 2, 2, 0)
solveBoard(a)
print("number of moves = ", counter)
