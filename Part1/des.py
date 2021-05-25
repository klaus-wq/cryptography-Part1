from PyQt5 import QtWidgets
from tkinter import Tk, Label
import time

def sdvig(str: str, n: int):
    arrTxt = str[n:] + str[:n]
    # arr = []
    # for i in range(len(str)):
    #     arr.append('')
    # for i in range(len(arr)):
    #     arr[(i - n) % len(arr)] = str[i]
    # arrTxt = ''
    # for i in arr:
    #     arrTxt += i
    return arrTxt


def xor(a: str, b: str):
    if len(a) > len(b):
        a = a.zfill(len(b))
    elif len(b) > len(a):
        b = b.zfill(len(a))
    # res = ""
    # for i in range(len(a)):
    #     if a[i] == '1':
    #         if b[i] == '1':
    #             res += '0'
    #         else:
    #             res += '1'
    #     if a[i] == '0':
    #         if b[i] == '1':
    #             res += '1'
    #         else:
    #             res += '0'
    res = bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a))
    return res


def extreme_bits(blocks6b: str):
    b = blocks6b[:1] + blocks6b[5:]
    return int(b, 2)


def middle_bits(blocks6b: str):
    b = blocks6b[1:5]
    return int(b, 2)


def substitutions(block48b: str):
    __Sbox = [
        [  # 0
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
        ],
        [  # 1
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        ],
        [  # 2
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
        ],
        [  # 3
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
        ],
        [  # 4
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
        ],
        [  # 5
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
        ],
        [  # 6
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
        ],
        [  # 7
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
        ]
    ]
    blocks6b = []
    for i in range(8):
        blocks6b.append(block48b[:6])
        block48b = block48b[6:]
    blocks32b = ''
    for i in range(len(blocks6b)):
        two_b = extreme_bits(blocks6b[i])
        four_b = middle_bits(blocks6b[i])
        blocks32b+=bin(__Sbox[i][two_b][four_b])[2:].zfill(4)
    return blocks32b


def func_F(R0: str, key: str):
    __EP = [
        32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1,
    ]
    __P = [
        16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25,
    ]
    expansion_permutation = initial_permutation(R0, __EP, 48)
    block48b = xor(expansion_permutation, key)
    block32b = substitutions(block48b)
    return initial_permutation(block32b, __P, 32)


def round_feistel_scheme(L0: str, R0: str, key: str):
    tmp = R0
    R0 = func_F(R0, key)
    R0 = xor(R0, L0)
    L0 = tmp
    return L0, R0

def feistel_scheme(L0: str, R0: str, keys, flag: int):
    if flag == 1:
        for i in range(len(keys)):
            L0, R0 = round_feistel_scheme(L0, R0, keys[i])
        L0, R0 = R0, L0
    else:
        for i in range(len(keys)):
            L0, R0 = round_feistel_scheme(L0, R0, keys[len(keys) - 1 - i])
        L0, R0 = R0, L0
    return L0, R0


def genKeys(key8b: str):
    __CP = [
        14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32,
    ]
    __K1P = [
        57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    ]
    __K2P = [
        63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4,
    ]
    keys = []
    key8bBin = ''
    for i in key8b:
        key8bBin += bin(ord(i))[2:].zfill(8)

    N1 = initial_permutation(key8bBin, __K1P, 28)
    N2 = initial_permutation(key8bBin, __K2P, 28)
    for i in range(16):
        if i == 0 or i == 1 or i == 8 or i == 15:
            n = 1
        else:
            n = 2
        N1 = sdvig(N1, n)
        N2 = sdvig(N2, n)
        N = N1 + N2
        keys.append(initial_permutation(N, __CP, 48))
    return keys


# начальная перестановка
# строка в дв СС и по какому массиву переставляем
def initial_permutation(binStr: str, arr: list, length: int):
    # afterPermutation = []
    # for i in range(length):
    #     afterPermutation.append('')
    # for i in range(len(afterPermutation)):
    #     afterPermutation[i] = binStr[arr[i] - 1]
    # afterPermutationStr = ''
    # for i in afterPermutation:
    #     afterPermutationStr += i
    afterPermutationStr = ''
    for i in range(length):
        afterPermutationStr += binStr[arr[i] - 1]
    return afterPermutationStr


def codingDES(block: str, flag: int, keys: list):
    __IP = [
        58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7,
    ]
    __FP = [
        40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25,
    ]

    afterInitPerm = initial_permutation(block, __IP, 64)

    L0 = afterInitPerm[:32]
    R0 = afterInitPerm[32:]
    L16, R16 = feistel_scheme(L0, R0, keys, flag)
    block64b = initial_permutation(L16 + R16, __FP, 64)
    return block64b

def ECB(keys1, text, flag: int):
    start = time.time()
    if not keys1 or keys1 == '':
        keys = genKeys('DESkey56')
    else:
        if len(keys1) != 16 * 48:
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
        keys = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(16):
            keys[i] = keys1[:48]
            keys1 = keys1[48:]

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
        block64b = codingDES(blocksBin[i], flag, keys)
        try:
            progress += percent
            label.config(text='\rОбработка завершена на %3d%%' % progress)
            root.update()
            #print('\rОбработка завершена на %3d%%' % progress, end = '', flush = True)
        except Exception:
            normal = 1
            pass
        for i in range(8):
            block64Int+=bytes([int(block64b[:8], 2)])
            block64b = block64b[8:]
    blocksText = after_coding(file, block64Int, flag)
    if normal == 0:
        root.destroy()
    print('Время выполнения: ', (time.time() - start)/60)
    return blocksText

def before_coding(text, flag: int):
    file = 0
    if type(text) == str:
        if flag == 1:
            textToInt = text.encode()
        else:
            textToInt = b''
            for i in text:
                textToInt+=bytes([ord(i)])
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

def CBC(keys1, text, flag: int, vector_init:str):
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
    if not keys1 or keys1 == '':
        keys = genKeys('DESkey56')
    else:
        if len(keys1) != 16 * 48:
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
        keys = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(16):
            keys[i] = keys1[:48]
            keys1 = keys1[48:]
    if not text:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Введите текст!")
        msgBox.exec_()
        return ("")

    blocksBin, file = before_coding(text, flag)
    percent = 100 / len(blocksBin)
    normal = 0
    root = Tk()

    label = Label(text='Progressbar')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.wm_geometry("+%d+%d" % (x, y))
    label.pack()

    if flag == 1:
        progress = 0
        block64Int = b''
        first_step = xor(blocksBin[0], vector_init)
        block64b = codingDES(first_step, flag, keys)
        block64b1 = block64b
        for k in range(8):
            block64Int += bytes([int(block64b[:8], 2)])
            block64b = block64b[8:]
        for p in range(1, len(blocksBin)):
            first_step = xor(block64b1, blocksBin[p])
            block64b = codingDES(first_step, flag, keys)
            block64b1 = block64b
            try:
                progress += percent
                label.config(text='\rОбработка завершена на %3d%%' % progress)
                root.update()
                # print('\rОбработка завершена на %3d%%' % progress, end = '', flush = True)
            except Exception:
                normal = 1
                pass
            # if p < len(blocksBin) - 1:
            #     first_step = xor(block64b, blocksBin[p+1])
            for k in range(8):
                block64Int += bytes([int(block64b[:8], 2)])
                block64b = block64b[8:]
    else:
        progress = 1
        block64Int = b''
        first_step = blocksBin[0]
        block64b = xor(vector_init, codingDES(blocksBin[0], flag, keys))
        for k in range(8):
            block64Int+=bytes([int(block64b[:8], 2)])
            block64b = block64b[8:]
        for p in range(1, len(blocksBin)):
            block64b = xor(first_step, codingDES(blocksBin[p], flag, keys))
            try:
                progress += percent
                label.config(text='\rОбработка завершена на %3d%%' % progress)
                root.update()
                # print('\rОбработка завершена на %3d%%' % progress, end = '', flush = True)
            except Exception:
                normal = 1
                pass
            for k in range(8):
                block64Int+=bytes([int(block64b[:8], 2)])
                block64b = block64b[8:]
            first_step = blocksBin[p]

    blocksText = after_coding(file, block64Int, flag)
    if normal == 0:
        root.destroy()
    return blocksText

def CFB(keys1, text, flag: int, vector_init:str):
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
    if not keys1 or keys1 == '':
        keys = genKeys('DESkey56')
    else:
        if len(keys1) != 16 * 48:
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
        keys = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(16):
            keys[i] = keys1[:48]
            keys1 = keys1[48:]
    if not text:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Введите текст!")
        msgBox.exec_()
        return ("")

    blocksBin, file = before_coding(text, flag)

    percent = 100 / len(blocksBin)
    progress = 1
    normal = 0
    root = Tk()

    label = Label(text='Progressbar')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.wm_geometry("+%d+%d" % (x, y))
    label.pack()

    if flag == 1:
        first_step = xor(blocksBin[0], codingDES(vector_init, 1, keys))
        block64b = first_step
        block64Int = b''
        for i in range(8):
            block64Int+=bytes([int(block64b[:8], 2)])
            block64b = block64b[8:]
        for p in range(1, len(blocksBin)):
            first_step = xor(blocksBin[p], codingDES(first_step, 1, keys))
            try:
                progress += percent
                label.config(text='\rОбработка завершена на %3d%%' % progress)
                root.update()
                # print('\rОбработка завершена на %3d%%' % progress, end = '', flush = True)
            except Exception:
                normal = 1
                pass
            block64b = first_step
            for i in range(8):
                block64Int+=bytes([int(block64b[:8], 2)])
                block64b = block64b[8:]
    else:
        first_step = xor(blocksBin[0], codingDES(vector_init, 1, keys))
        block64b = first_step
        block64Int = b''
        for i in range(8):
            block64Int+=bytes([int(block64b[:8], 2)])
            block64b = block64b[8:]
        for p in range(1, len(blocksBin)):
            first_step = xor(blocksBin[p], codingDES(blocksBin[p-1], 1, keys))
            try:
                progress += percent
                label.config(text='\rОбработка завершена на %3d%%' % progress)
                root.update()
                # print('\rОбработка завершена на %3d%%' % progress, end = '', flush = True)
            except Exception:
                normal = 1
                pass
            block64b = first_step
            for i in range(8):
                block64Int+=bytes([int(block64b[:8], 2)])
                block64b = block64b[8:]

    blocksText = after_coding(file, block64Int, flag)
    if normal == 0:
        root.destroy()
    return blocksText

def OFB(keys1, text, flag: int, vector_init:str):
    if not vector_init or vector_init == '':
        vector_init = '1110011110010101110010111001010010000111001010011100101001001011' #КАКОЙ БРАТЬ?
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
    if not keys1 or keys1 == '':
        keys = genKeys('DESkey56')
    else:
        if len(keys1) != 16 * 48:
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
        keys = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(16):
            keys[i] = keys1[:48]
            keys1 = keys1[48:]
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
    first_step = codingDES(vector_init, 1, keys)
    for p in range(len(blocksBin)):
        block64b = xor(first_step, blocksBin[p])
        try:
            progress += percent
            label.config(text='\rОбработка завершена на %3d%%' % progress)
            root.update()
            # print('\rОбработка завершена на %3d%%' % progress, end = '', flush = True)
        except Exception:
            normal = 1
            pass
        for i in range(8):
            block64Int+=bytes([int(block64b[:8], 2)])
            block64b = block64b[8:]
        first_step = codingDES(first_step, 1, keys)

    blocksText = after_coding(file, block64Int, flag)
    if normal == 0:
        root.destroy()
    return blocksText
