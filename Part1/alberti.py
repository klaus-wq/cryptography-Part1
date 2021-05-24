from PyQt5 import QtWidgets

def codingAlberti(text, key, keyToShifr, flag):
    #на пустоту
    if not text or not key or not keyToShifr:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Введите текст!")
        msgBox.exec_()
        return ("")
    #dictSymb = " `~!@#№$;%^:?*&()-+=_,./1234567890"
    #keyToShifr = "ALBERTICIPHER"
    dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    tabl = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"



    keyToShifr = keyToShifr[::-1]
    for i in keyToShifr:
        if i not in dict:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Введите текст!")
            msgBox.exec_()
            return ("")
        else:
            tabl = tabl[:tabl.rfind(i)] + tabl[tabl.rfind(i)+1:]
            tabl = i + tabl
    #print(tabl)
    key1 = ""

    for i in key:
        if i not in dict:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Введите текст из алфавита!")
            msgBox.exec_()
            return ("")

    #догоняем ключ до длины текста и оставляем символы не из словаря
    j = 0
    for i in text:
        if i not in dict or (ord(i) <= 13 and ord(i) >= 0):
            key1 += i
        else:
            key1 += key[j]
            j+=1
        if j == len(key):
            j = 0
    #print(key1)

    s = []
    for i in key1:
        #if dict.rfind(i) != -1:
        s.append(dict.rfind(i))
    #print(s)

    res = ""
    for i in range(len(text)):
        if text[i] in dict:
            if flag == 1:
                res += tabl[(dict.rfind(text[i]) - s[i] - 1)% len(dict)]
            else:
                res += dict[(tabl.rfind(text[i]) + s[i] + 1)% len(dict)]
        else:
            res += text[i]

    # j = 0
    # for i in text:
    #     if i in dict:
    #         res+=tabl[(dict.index(i) - int(s[j])-1) % len(dict)]
    #         j+=1
    #     else:
    #         res+=i
    return res
