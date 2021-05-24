from PyQt5 import QtWidgets
#text = "Криптография"
#key = "(3, 1, 2)(1, 2, 1)"

def codingRichelieu(text, key, flag):
    if not text or not key:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Введите текст!")
        msgBox.exec_()
        return ("")
    for i in key:
        for j in range(len(i)):
            if int(i[j]) < 1 or int(i[j]) > len(i) or len(i) != len(set(i)):
                print('len', len(i))
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка в ключе!!")
                msgBox.exec_()
                return ("")
    lenText = len(text)
    if flag == 1:
        res = ""
        for i in range(len(key)):
            text1 = text[:len(key[i])]
            print('text1', text1)
            for j in range(len(key[i])):
                res+=text1[int(key[i][j]) - 1]
            text = text[len(key[i]):]
        print('text', text)
        if len(res) != lenText:
            res+=text
        print('res', res)
    else:
        print('key', key)
        print('text', text)
        resArray = []
        for i in range(len(key)):
            res1 = []
            for k in range(len(key[i])):
                res1.append("")
            text1 = text[:len(key[i])]
            for j in range(len(key[i])):
                res1[(int(key[i][j])) - 1] = text1[j]
            text = text[len(key[i]):]
            resArray.append(res1)
        if len(resArray) != lenText:
            resArray.append(text)
        res = ""
        for i in range(len(resArray)):
            for j in range(len(resArray[i])):
                res+=resArray[i][j]

    # except Exception:
    #     print('Error!')
    #     return None
    return res
