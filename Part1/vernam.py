from PyQt5 import QtWidgets

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

def codingVernam(text, key, flag):
    if not text or not key:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка!")
        msgBox.setText("Введите текст!")
        msgBox.exec_()
        return ("")

    if len(text) != len(key):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка!")
        msgBox.setText("Длина ключа должна быть равна длине текста!")
        msgBox.exec_()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка!")
        msgBox.setText("Длина текста = "+str(len(text)))
        msgBox.exec_()
        return ("")

    textCode = []
    for i in text:
        textCode.append(ord(i))
    print('t', textCode)

    for i in range(len(textCode)):
        textCode[i] = (bin(textCode[i])[2:]).zfill(25)
    print(textCode)

    keyCode = []
    for i in key:
        keyCode.append(ord(i))

    for i in range(len(keyCode)):
        keyCode[i] = (bin(keyCode[i])[2:]).zfill(25)

    resText = ""
    for i in range(len(textCode)):
        tmp1 = xor(textCode[i], keyCode[i])
        #resText += str(chr(int(tmp1)))
        resText += str(chr(int(tmp1, 2)))

    return resText