from PyQt5 import QtWidgets
#буква шифруется относительно своего алфавита каждая?
def codingGronsfeld(text, key, flag):
    if not text or not key:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Введите текст!")
        msgBox.exec_()
        return ("")

    dict = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    key1 = ""
    dictNum = "0123456789"

    for i in key:
        if i not in dictNum:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Введите цифры!")
            msgBox.exec_()
            return ("")

    while len(key1) != len(text):
        key1 += key
        if len(key1) > len(text):
            key1 = key1[:len(text)]

    s = ""
    j = 0
    for i in text:
        if i in dict:
            s+=dict[(dict.index(i) + flag*int(key1[j])) % len(dict)]
        else:
            s+=i
        j+=1
    return s