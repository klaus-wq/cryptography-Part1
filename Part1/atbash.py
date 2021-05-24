from PyQt5 import QtWidgets

def codingAtbash(text):
    dictEng = "abcdefghijklmnopqrstuvwxyz"
    dictEngUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictRus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    dictRusUp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dictSymb = " `~!@#№$;%^:?*&()-+=_,./1234567890"
    res = ""
    for i in text:
        if i in dictEng:
            res += dictEng[len(dictEng) - dictEng.index(i) - 1]
        elif i in dictEngUp:
            res += dictEngUp[len(dictEngUp) - dictEngUp.index(i) - 1]
        elif i in dictRus:
            res += dictRus[len(dictRus) - dictRus.index(i) - 1]
        elif i in dictRusUp:
            res += dictRusUp[len(dictRusUp) - dictRusUp.index(i) - 1]
        elif i in dictSymb:
            res+=i
        elif ord(i) <= 13 and ord(i) >= 0:
            res+=i
        else:
            #QtWidgets.QMessageBox.critical(super, "Error", "Error", QtWidgets.QMessageBox.Ok)
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Введите текст!")
            msgBox.exec_()
            return("")
    return res
