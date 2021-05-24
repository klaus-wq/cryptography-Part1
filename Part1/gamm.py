from PyQt5 import QtWidgets

def binar(n):
    b = ""
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b

def ten(n):
    b = ""
    while n > 0:
        b = str(n % 10) + b
        n = n // 10
    return b

def xor(a, b):
    res = ""
    for i in range(len(a)):
        if a[i] == '1':
            if b[i] == '1':
                res+='0'
            else:
                res+='1'
        if a[i] == '0':
            if b[i] == '1':
                res+='1'
            else:
                res+='0'
    return res

def genGamma(a, b, m, X0, text):
    if not a or not b or not m or not X0 or not text:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Заполните все поля!")
        msgBox.exec_()
        return ("")

    try:
        a = int(a)
    except Exception:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Введите число!")
        msgBox.exec_()
        return ("")

    try:
        b = int(b)
    except Exception:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Введите число!")
        msgBox.exec_()
        return ("")

    try:
        m = int(m)
    except Exception:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Введите число!")
        msgBox.exec_()
        return ("")

    try:
        X0 = int(X0)
    except Exception:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Введите число!")
        msgBox.exec_()
        return ("")

    if int(m) < 2:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("m >= 2!")
        msgBox.exec_()
        return ("")

    #X0 = 7
    res = [X0]
    while len(res) != len(text):
        res.append((a*X0 + b) % m)
        X0 = (a*X0 + b) % m
    res = str(res)
    res = res.replace(",", "")
    res = res.replace("[", "")
    res = res.replace("]", "")
    #print(res)
    return res


def codingGamma(gamma, text):
    #    arrGamm = list(genGamma(a, b, m, X0, text).split(' '))
    if not text or not gamma:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Заполните поле ключа и текста!")
        msgBox.exec_()
        return ("")

    arrGamm = list(gamma.split(' '))
    for i in range(len(arrGamm)):
        try:
            X0 = int(arrGamm[i])
        except Exception:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Введите число!")
            msgBox.exec_()
            return ("")

    if len(arrGamm) != len(text):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Длина ключа должна быть равна длине текста!")
        msgBox.exec_()
        return ("")

    gammCodeBin = []
    for i in range(len(arrGamm)):
        gammCodeBin.append((bin(int(arrGamm[i]))[2:]).zfill(25))
        #gammCodeBin.append((binar(int(arrGamm[i]))).zfill(25))
    #print('g', gammCodeBin)

    textCode = []
    for i in text:
        textCode.append(ord(i))

    textCodeBin = []
    for i in range(len(text)):
        textCodeBin.append((bin(int(textCode[i]))[2:]).zfill(25))
        #textCodeBin.append((binar(int(ord(text[i])))).zfill(25))
    #print('t', textCodeBin)

    resCode = ""
    for i in range(len(textCodeBin)):
        tmp1 = xor(textCodeBin[i], gammCodeBin[i])
        resCode+=chr(int(tmp1, 2))
    #print(resCode)

    return resCode

def codingGamma1(gamma, text):
    #    arrGamm = list(genGamma(a, b, m, X0, text).split(' '))
    if not text or not gamma:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Заполните поле ключа и текста!")
        msgBox.exec_()
        return ("")

    arrGamm = list(gamma.split(' '))
    for i in range(len(arrGamm)):
        try:
            X0 = int(arrGamm[i])
        except Exception:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Введите число!")
            msgBox.exec_()
            return ("")

    if len(arrGamm) != len(text):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Длина ключа должна быть равна длине текста!")
        msgBox.exec_()
        return ("")

    gammCodeBin = []
    for i in range(len(arrGamm)):
        gammCodeBin.append((bin(int(arrGamm[i]))[2:]).zfill(25))

    textCodeBin = []
    for i in range(len(text)):
        textCodeBin.append((bin(text[i])[2:]).zfill(25))

    resCode = bytearray(b"")
    for i in range(len(textCodeBin)):
        tmp1 = xor(textCodeBin[i], gammCodeBin[i])
        resCode.append(int(tmp1, 2) % 256)

    return resCode