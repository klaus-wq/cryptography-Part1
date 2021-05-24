from numpy import rot90, hstack, vstack, array, add, append, dtype, where
from random import randint, choice
import string
from PyQt5 import QtWidgets

def codingCardano(text, size):
    if not text:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Введите текст!")
        msgBox.exec_()
        return ("")

    #4 матрицы размера size на size, для мусора
    global res
    while len(text)%(4*size*size) != 0:
        #text += "*"
        text += choice(string.ascii_letters)

    arr1 = []
    k = 1
    for i in range(size):
        mtx = []
        for j in range(size):
            mtx.append(str(k))
            k+=1
        arr1.append(mtx)

    arr3 = rot90(arr1)
    arr4 = rot90(arr3)
    arr2 = rot90(arr4)

    arr1 = array(arr1, dtype="U25")
    arr3 = array(arr3, dtype="U25")
    arr2 = array(arr2, dtype="U25")
    arr4 = array(arr4, dtype="U25")

    #tmp=[2, 4, 4, 1, 3, 4, 2, 1, 2]
    for k in range(1, size*size + 1):
        #numberMtx=tmp[k-1]
        numberMtx = randint(1, 4)
        if numberMtx == 1:
            for i in range(len(arr1)):
                for j in range(len(arr1)):
                    if arr1[i][j] == str(k):
                        arr1[i][j] += 'X'
        if numberMtx == 2:
            for i in range(len(arr2)):
                for j in range(len(arr2)):
                    if arr2[i][j] == str(k):
                        arr2[i][j] += 'X'
        if numberMtx == 3:
            for i in range(len(arr3)):
                for j in range(len(arr3)):
                    if arr3[i][j] == str(k):
                        arr3[i][j] += 'X'
        if numberMtx == 4:
            for i in range(len(arr4)):
                for j in range(len(arr4)):
                    if arr4[i][j] == str(k):
                        arr4[i][j] += 'X'

    arr11 = hstack((arr1, arr2))  # вправо
    arr12 = hstack((arr3, arr4))  # вправо
    arr = vstack((arr11, arr12))  # вниз
    print(arr)

    restext=""
    for r in range(len(text)//(size*size*4)):
        res = []
        for i in range(size * 2):
            res.append([""] * size * 2)

    #поворачиваем 4 раза и кодируем, символов = size*size по 4 раза
        for p in range(4):
            for k in range(1, size*size + 1):
                i, j = where(arr == str(k) + "X")
                res[int(i)][int(j)] = text[k-1]
            arr = rot90(arr)
            text = text[size*size:]

        for i in range(len(res)):
            for k in range(len(res[i])):
                restext+=res[i][k]
    print(restext)
    return arr, restext

def decodingCardano(arr, text):
    size = len(arr)//2

    res = ""
    for r in range(len(text)//(size*size*4)):
        mtx = []
        for i in range(size*2):
            mtx1 = []
            for j in range(size*2):
                mtx1.append(text[0])
                text=text[1:]
            mtx.append(mtx1)
        for i in mtx:
            print(i)

        for p in range(4):
             for k in range(1, size * size + 1):
                 i, j = where(arr == str(k) + "X")
                 res += mtx[int(i)][int(j)]
             arr = rot90(arr)
    print(res)
    return res

#arr, res = codingCardano("Привет, мир!", 4)
#print(res)
#res1 = decodingCardano(arr, res)
#print(res1)