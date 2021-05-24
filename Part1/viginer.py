from PyQt5 import QtWidgets

def codingViginer(text, key, flag):
    global tmpDict
    #на пустоту ввода
    if not text or not key:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Введите текст!")
        msgBox.exec_()
        return ("")
    dictEngUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictEng = "abcdefghijklmnopqrstuvwxyz"
    dictRusUp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dictRus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    key1 = ""

    #какой алфавит первый символ из алфавита
    for i in text:
        if i in dictEng:
            tmpDict = dictEng
            break
        elif i in dictEngUp:
            tmpDict = dictEngUp
            break
        elif i in dictRus:
            tmpDict = dictRus
            break
        elif i in dictRusUp:
            tmpDict = dictRusUp
            break
        else:
            tmpDict = []

    for i in text:
        if (i in dictRus) or (i in dictRusUp) or (i in dictEng) or (i in dictEngUp):
            if i not in tmpDict:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Текст должен быть из одного алфавита!")
                msgBox.exec_()
                return ("")

    for i in key:
        if (i in dictRus) or (i in dictRusUp) or (i in dictEng) or (i in dictEngUp):
            if i not in tmpDict:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Алфавит ключа и текста не совпадает!!")
                msgBox.exec_()
                return ("")
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Ключ только из символов!")
            msgBox.exec_()
            return ("")

    #догоняем ключ до длины текста
    while len(key1) != len(text):
        key1 += key
        if len(key1) > len(text):
            key1 = key1[:len(text)]
    #print(key1)

    s = ""
    j = 0
    for i in text:
        if i in dictEng:
            s+=dictEng[(dictEng.index(i) + flag*dictEng.index(key1[j]))% len(dictEng)]
        elif i in dictEngUp:
            s+=dictEngUp[(dictEngUp.index(i) + flag*dictEngUp.index(key1[j])) % len(dictEngUp)]
        elif i in dictRus:
            s+=dictRus[(dictRus.index(i) +flag*dictRus.index(key1[j])) % len(dictRus)]
        elif i in dictRusUp:
            s+=dictRusUp[(dictRusUp.index(i) + flag*dictRusUp.index(key1[j])) % len(dictRusUp)]
        else:
            s+=i
        j+=1
    return s