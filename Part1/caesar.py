from PyQt5 import QtWidgets

def codingCaesar(text, sdvig, temp):
    res = ""
    dictEng = "abcdefghijklmnopqrstuvwxyz"
    dictEngUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictRus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    dictRusUp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dictSymb = " `~!@#№$;%^:?*&()-+=_,./1234567890"
    for i in text:
        if i in dictEng:
            res += dictEng[(dictEng.index(i) + sdvig * temp) % len(dictEng)]
        elif i in dictEngUp:
            res += dictEngUp[(dictEngUp.index(i) + sdvig * temp) % len(dictEngUp)]
        elif i in dictRus:
            res += dictRus[(dictRus.index(i) + sdvig * temp) % len(dictRus)]
        elif i in dictRusUp:
            res += dictRusUp[(dictRusUp.index(i) + sdvig * temp) % len(dictRusUp)]
        elif i in dictSymb:
            res += i
        elif ord(i) <= 13 and ord(i) >= 0:
            res += i
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Введите текст!")
            msgBox.exec_()
            return ("")
    return res
