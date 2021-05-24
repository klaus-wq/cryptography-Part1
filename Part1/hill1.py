from math import sqrt
from numpy import linalg, round, delete
from PyQt5 import QtWidgets

# text = 'кимоно'
# K = 'коловорот'

def matrix_algDop(arr, i, j, mod):
    tmp = delete(delete(arr,i,axis=0), j, axis=1)
    detTmp = round(linalg.det(tmp))
    return (pow(-1, (i+1)+(j+1)) * detTmp) % mod

def exgcd(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return x

def multiply(vector, matr, mod):
    res = []
    i = 0 #номер столбца
    while i != len(matr):
        res1 = 0
        for j in range(len(vector)):
            res1+=((matr[j][i] * vector[j]) % mod)
        res.append(res1 % mod)
        i+=1
    return res

def transpose(matr):
    i = 0
    res = []
    while i != len(matr):
        res1 = []
        for j in range(len(matr)):
            res1.append(matr[j][i])
        res.append(res1)
        i+=1
    return res

def codingHill(text, K):
    if not text or not K:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка!")
        msgBox.setText("Введите текст!")
        msgBox.exec_()
        return ("")
    if sqrt(len(K)) - int(sqrt(len(K))) != 0:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка!")
        msgBox.setText("Error1. Длина ключа должна быть квадратом целого числа!")
        msgBox.exec_()
        return ("")
    if len(text) % int(sqrt(len(K))) != 0:
        count = len(text)
        while count % int(sqrt(len(K))) != 0:
            count += 1
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка!")
        msgBox.setText("Error2. Длина текста должна быть кратна sqrt(key)!")
        msgBox.exec_()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка!")
        msgBox.setText("Ближайшая длина, кратная sqrt(key) = " + str(count))
        msgBox.exec_()
        return ("")

    dict = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"№;%:?*()_-+\\/.,@#$^&[]{}\'<>`~|\t\n '
    print(len(dict))

    size = int(sqrt(len(K)))
    key = []
    for i in range(int(size)):
        key1 = []
        for j in range(int(size)):
            key1.append(dict.index(K[j]))
        K = K[int(size):]
        key.append(key1)
    for i in key:
        print('key', i)

    lenText = len(text)
    textMatr = []
    for k in range(lenText//int(size)):
        P1 = []
        for p in range(int(size)):
            P1.append(dict.index(text[p]))
        text = text[int(size):]
        textMatr.append(P1)
    for i in textMatr:
        print('text', i)

    multMatr = []
    for i in range(len(textMatr)):
        multMatr.append(multiply(textMatr[i], key, len(dict)))
    for i in multMatr:
        print(i)

    res = ""
    for i in range(len(multMatr)):
        for j in range(len(multMatr[i])):
            res+=dict[multMatr[i][j]]
    print(res)
    return res

def decodingHill(res, K):
    if not K or not res:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка!")
        msgBox.setText("Введите текст!")
        msgBox.exec_()
        return ("")
    if sqrt(len(K)) - int(sqrt(len(K))) != 0:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка!")
        msgBox.setText("Error1. Длина ключа должна быть квадратом целого числа!")
        msgBox.exec_()
        return ("")

    dict = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"№;%:?*()_-+\\/.,@#$^&[]{}\'<>`~|\t\n '

    size = int(sqrt(len(K)))
    text = []
    for i in range((len(res)//size)):
        C2 = []
        for j in range(size):
            C2.append(dict.index(res[j]))
        res = res[size:]
        text.append(C2)

    key = []
    for i in range(int(size)):
        key1 = []
        for j in range(int(size)):
            key1.append(dict.index(K[j]))
        K = K[int(size):]
        key.append(key1)

    if int(linalg.det(key)) % len(dict) == 0:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка!")
        msgBox.setText("Det не может быть равен 0!")
        msgBox.exec_()
        return ("")

    keyObr = []
    for i in range(len(key)):
        keyM1 = []
        for j in range(len(key[i])):
            keyM1.append(matrix_algDop(key, i, j, len(dict)))
        keyObr.append(keyM1)
    keyObr = transpose(keyObr)
    print('keyM', keyObr)

    detKey = round(linalg.det(key)) % len(dict)
    print('detKey', detKey)
    detObr = exgcd(detKey, len(dict))
    print('detObr', detObr)

    keyObrdetObr = []
    for i in range(len(keyObr)):
        tmp = []
        for j in range(len(keyObr)):
            tmp.append((keyObr[i][j] * detObr) % len(dict))
        keyObrdetObr.append(tmp)

    multMatr = []
    for i in range(len(text)):
        multMatr.append(multiply(text[i], keyObrdetObr, len(dict)))
    for i in multMatr:
        print(i)

    resText = ""
    for i in range(len(multMatr)):
        for j in range(len(multMatr[i])):
            resText += dict[int(multMatr[i][j])]
    print(resText)

    return resText

# codingHill(text, K)
# decodingHill(codingHill(text, K), K)