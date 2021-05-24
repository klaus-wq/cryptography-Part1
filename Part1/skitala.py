from PyQt5 import QtWidgets
import PySimpleGUI as sg

def codingSkitala(text, m):
    if text == "":
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Введите текст!")
        msgBox.exec_()
        return ("")
    for i in text:
        if i == "*":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Введите без звёздочек!")
            msgBox.exec_()
            return("")

    if m > len(text):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Должно быть меньше длины сообщения!")
        msgBox.exec_()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Длина сообщения = " + str(len(text)))
        msgBox.exec_()
        return ("")

    if m == 0:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Не может быть 0!")
        msgBox.exec_()
        return ("")

    n = (len(text) - 1) // m + 1
    res = ""
    m1 = m

    while len(text) < m1*n:
        text+="*"

    if n == 1 or m == 1:
        return text

    res+=text[0]
    m = m - 1
    i = j = 0
    while len(res) != len(text):
        i+=n
        i = i % len(text)
        res+=text[i]
        m = m - 1
        if m == 0 and len(res) != len(text):
            m = m1
            j += 1
            i = j
            res+=text[i]
            m = m - 1

    return res

def decodingSkitala(text, m):
    if text == "":
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Введите текст!")
        msgBox.exec_()
        return ("")
    if m == 0:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Не может быть 0!")
        msgBox.exec_()
        return ("")

    n = m
    m = (len(text) - 1) // m + 1
    res = ""
    m1 = m

    if m > len(text):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Должно быть меньше длины сообщения!")
        msgBox.exec_()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Длина сообщения = " + str(len(text)))
        msgBox.exec_()
        return ("")

    if n == 1 or m == 1:
        return text

    res+=text[0]
    m = m - 1
    i = j = 0
    while len(res) != len(text):
        i+=n
        i = i % len(text)
        res+=text[i]
        m = m - 1
        if m == 0 and len(res) != len(text):
            m = m1
            j += 1
            i = j
            res+=text[i]
            m = m - 1

    return res