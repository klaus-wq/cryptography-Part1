from PyQt5 import QtWidgets
from tkinter import Tk, Label
import time

#возвращает массив из 8 элементов, где каждый элемент - это 32 бита
def genKeys_GOST(key256b:str):
    keys1 = key256b.encode()
    keys = []
    for i in range(8):
        keys.append(keys1[:4])
        keys1 = keys1[4:]
    keysBin = []
    for i in range(len(keys)):
        binStr = ''
        for j in keys[i]:
            binStr += bin(j)[2:].zfill(8)
        keysBin.append(binStr)
    return keysBin

def before_coding(text, flag: int):
    file = 0
    if type(text) == str:
        if flag == 1:
            textToInt = text.encode()
        else:
            textToInt = b''
            for i in text:
                textToInt += bytes([ord(i)])
    else:
        textToInt = text
        file = 1
        print('OK')

    blocks = []
    while len(textToInt) > 0:
        blocks.append(textToInt[:8])
        textToInt = textToInt[8:]

    count = 0
    if len(blocks[len(blocks) - 1]) != 8:
        while len(blocks[len(blocks) - 1]) != 8:
            count += 1
            blocks[len(blocks) - 1] += bytes([0])
        blocks[len(blocks) - 1] = blocks[len(blocks) - 1][:-1] + bytes([count])

    blocksBin = []
    for i in range(len(blocks)):
        binStr = ''
        for j in blocks[i]:
            binStr += bin(j)[2:].zfill(8)
        blocksBin.append(binStr)
    return blocksBin, file

def after_coding(file, block64Int, flag):
    if file == 0:
        if flag != 1:
            numb = block64Int[len(block64Int) - 1]
            print('n', numb)
            blocksText1 = block64Int
            j = 2
            for i in range(numb-1):
                if blocksText1[-j] == 0:
                    blocksText1 = blocksText1[:-1]
                    j = 1
                else:
                    break
            if len(blocksText1) < len(block64Int):
                blocksText1 = blocksText1[:-1]
            blocksText = ''
            for i in blocksText1:
                blocksText += chr(i)
        else:
            blocksText = ''
            for i in block64Int:
                blocksText += chr(i)
    else:
        if flag != 1:
            numb = block64Int[len(block64Int) - 1]
            print('n', numb)
            blocksText = block64Int
            j = 2
            for i in range(numb-1):
                if blocksText[-j] == 0:
                    blocksText = blocksText[:-1]
                    j = 1
                else:
                    break
            if len(blocksText) < len(block64Int):
                blocksText = blocksText[:-1]
        else:
            blocksText = block64Int
    return blocksText

def xor(a: str, b: str):
    if len(a) > len(b):
        a = a.zfill(len(b))
    elif len(b) > len(a):
        b = b.zfill(len(a))
    res = bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a))
    return res

def sdvig(str: str, n: int):
    arrTxt = str[n:] + str[:n]
    return arrTxt

def substitution(N1:str):
    __Sbox = [
        [9, 6, 3, 2, 8, 11, 1, 7, 10, 4, 14, 15, 12, 0, 13, 5],
        [3, 7, 14, 9, 8, 10, 15, 0, 5, 2, 6, 12, 11, 4, 13, 1],
        [14, 4, 6, 2, 11, 3, 13, 8, 12, 15, 5, 10, 0, 7, 1, 9],
        [14, 7, 10, 12, 13, 1, 3, 9, 0, 2, 11, 4, 15, 8, 5, 6],
        [11, 5, 1, 9, 8, 13, 15, 0, 14, 4, 2, 3, 12, 7, 10, 6],
        [3, 10, 13, 12, 1, 2, 0, 11, 7, 5, 9, 4, 8, 15, 14, 6],
        [1, 13, 2, 9, 7, 10, 6, 0, 8, 12, 4, 5, 15, 3, 11, 14],
        [11, 10, 15, 5, 0, 12, 14, 8, 6, 2, 3, 9, 1, 7, 13, 4]
    ]
    # 8 блоков по 4 бита
    blocks4b = []
    for i in range(8):
        blocks4b.append(N1[:4])
        N1 = N1[4:].zfill(4)
    blocksAfterSbox = ''
    for i in range(8):
        blocksAfterSbox+=bin(__Sbox[i][int(blocks4b[i], 2)])[2:].zfill(4)
    return sdvig(blocksAfterSbox, 11)

def round_feistel_scheme(L0: str, R0: str, key: str):
    # RES = (N1 + Ki) mod 2 ^ 32
    RES = bin((int(L0, 2) | int(key, 2)) % 2**32)[2:]

    # RES = RES -> Sbox, << 11
    RES = substitution(RES)
    L0, R0 = xor(RES, R0), L0
    return L0, R0

def feistel_scheme(block:str, keys:list, flag:int):
    L0 = block[:32]
    R0 = block[32:]
    if flag == 1:
        # K0, K1, K2, K3, K4, K5, K6, K7, K0, K1, K2, K3, K4, K5, K6, K7, K0, K1, K2, K3, K4, K5, K6, K7
        for i in range(3):
            for j in range(len(keys)):
                L0, R0 = round_feistel_scheme(L0, R0, keys[j])
        # K7, K6, K5, K4, K3, K2, K1, K0
        for i in range(len(keys)):
            L0, R0 = round_feistel_scheme(L0, R0,  keys[len(keys) - 1 - i])
        L0, R0 = R0, L0
    else:
        # K0, K1, K2, K3, K4, K5, K6, K7
        for i in range(len(keys)):
            L0, R0 = round_feistel_scheme(L0, R0, keys[i])
        # K7, K6, K5, K4, K3, K2, K1, K0, K7, K6, K5, K4, K3, K2, K1, K0, K7, K6, K5, K4, K3, K2, K1, K0
        for i in range(3):
            for j in range(len(keys)):
                L0, R0 = round_feistel_scheme(L0, R0, keys[len(keys) - 1 - j])
        L0, R0 = R0, L0
    return L0 + R0

def GOST_zamena(keys1, text, flag):
    start = time.time()
    if not keys1 or keys1 == '':
        keys = genKeys_GOST('this_is_a_pasw_for_GOST_28147_89')
    else:
        if len(keys1) != 256:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Ошибка в ключе!")
            msgBox.exec_()
            return ("")
        for i in keys1:
            if (i != '1' and i != 1 and i != '0' and i != 0) == True:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка в ключе!")
                msgBox.exec_()
                return ("")
        keys = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(8):
            keys[i] = keys1[:32]
            keys1 = keys1[32:]

    if not text:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Введите текст!")
        msgBox.exec_()
        return ("")

    blocksBin, file = before_coding(text, flag)

    percent = 100 / len(blocksBin)
    progress = 0
    normal = 0
    root = Tk()

    label = Label(text='Progressbar')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.wm_geometry("+%d+%d" % (x, y))
    label.pack()

    block64Int = b''
    for i in range(len(blocksBin)):
        block64b = feistel_scheme(blocksBin[i], keys, flag)
        try:
            progress += percent
            label.config(text='\rОбработка завершена на %3d%%' % progress)
            root.update()
            #print('\rОбработка завершена на %3d%%' % progress, end = '', flush = True)
        except Exception:
            normal = 1
            pass
        for j in range(8):
            block64Int+=bytes([int(block64b[:8], 2)])
            block64b = block64b[8:]

    blocksText = after_coding(file, block64Int, flag)
    if normal == 0:
        root.destroy()
    print('Время выполнения: ', (time.time() - start) / 60)
    return blocksText

def GOST_gamm(keys1, text, flag, vector_init):
    start = time.time()
    if not keys1 or keys1 == '':
        keys = genKeys_GOST('this_is_a_pasw_for_GOST_28147_89')
    else:
        if len(keys1) != 256:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Ошибка в ключе!")
            msgBox.exec_()
            return ("")
        for i in keys1:
            if (i != '1' and i != 1 and i != '0' and i != 0) == True:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка в ключе!")
                msgBox.exec_()
                return ("")
        keys = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(8):
            keys[i] = keys1[:32]
            keys1 = keys1[32:]
    if not vector_init or vector_init == '':
        vector_init = '1110011110010101110010111001010010000111001010011100101001001011'
    else:
        if len(vector_init) != 64:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Ошибка в векторе инициализации!")
            msgBox.exec_()
            return ("")
        for i in vector_init:
            if (i != '1' and i != 1 and i != '0' and i != 0) == True:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка в векторе инициализации!!")
                msgBox.exec_()
                return ("")
    if not text:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Введите текст!")
        msgBox.exec_()
        return ("")

    blocksBin, file = before_coding(text, flag)

    percent = 100 / len(blocksBin)
    progress = 0
    normal = 0
    root = Tk()

    label = Label(text='Progressbar')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.wm_geometry("+%d+%d" % (x, y))
    label.pack()

    if flag == 1:
        N = vector_init
        block64Int = b''
        for i in range(len(blocksBin)):
            gamma = feistel_scheme(N, keys, 1)
            try:
                progress += percent
                label.config(text='\rОбработка завершена на %3d%%' % progress)
                root.update()
                # print('\rОбработка завершена на %3d%%' % progress, end = '', flush = True)
            except Exception:
                normal = 1
                pass
            block64b = xor(gamma, blocksBin[i])
            N = block64b
            for j in range(8):
                block64Int += bytes([int(block64b[:8], 2)])
                block64b = block64b[8:]
    else:
        N = vector_init
        block64Int = b''
        for i in range(len(blocksBin)):
            gamma = feistel_scheme(N, keys, 1)
            try:
                progress += percent
                label.config(text='\rОбработка завершена на %3d%%' % progress)
                root.update()
                # print('\rОбработка завершена на %3d%%' % progress, end = '', flush = True)
                time.sleep(0.01)
            except Exception:
                normal = 1
                pass
            block64b = xor(gamma, blocksBin[i])
            for j in range(8):
                block64Int += bytes([int(block64b[:8], 2)])
                block64b = block64b[8:]
            N = blocksBin[i]

    blocksText = after_coding(file, block64Int, flag)
    if normal == 0:
        root.destroy()
    print('Время выполнения: ', (time.time() - start) / 60)
    return blocksText
