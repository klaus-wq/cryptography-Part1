# -*- coding: utf-8 -*-
import re

import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QScrollArea
from window import Ui_MainWindow
import sys
from atbash import codingAtbash
from atbashWindow import Ui_AdbashWindow
from skitalaWindow import Ui_SkitalaWindow
from ceazarWindow import Ui_CaezarWindow
from skitala import codingSkitala, decodingSkitala
from caesar import codingCaesar
from polybiusWindow import Ui_PolybiusWindow
from polybius import codingPolybius, decodingPolybius, codingPolybius1
from alberti import codingAlberti
from albertiWindow import Ui_AlbertiWindow
from gronsfeld import codingGronsfeld
from gronsfeldWindow import Ui_GronsfeldWindow
from viginer import codingViginer
from viginerWindow import Ui_ViginerWindow
from cardano import codingCardano, decodingCardano
from richelieu import codingRichelieu
from cardanoWindow import Ui_CardanoWindow
from richelieuWindow import Ui_RichelieuWindow
from playfair import codingPlayfair, decodingPlayfair
from playfairWindow import Ui_PlayfairWindow
from vernam import codingVernam
from vernamWindow import Ui_VernamWindow
from hill1 import codingHill, decodingHill
from hillWindow import Ui_HillWindow
from gammWindow import Ui_GammWindow
from gamm import codingGamma, genGamma, xor, codingGamma1
from chastotaWindow import Ui_ChastWindow
from chastota import chastota, IshodnayaBukva, RaznitsaWithIshodnayaBukva, SearchRaznitsaForEachBukva, SearchChastotaInText, gistogramma, printBukva, zamena
from polialphabetWindow import Ui_PolialphabetWindow
import indexOfMatches
import autocorrelationMethod
import casiski
from desWindow import Ui_DesWindow
from des import ECB, genKeys, CBC, CFB, OFB
from gostWindow import Ui_GostWindow
from gost import genKeys_GOST, GOST_zamena, GOST_gamm

global correct_encoding
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        if self.ui.comboBox.currentText() == "Атбаш":
            self.ex = adbashWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Сцитала":
            self.ex = skitalaWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Квадрат Полибия":
            self.ex = polybiusWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Цезарь":
            self.ex = caezarWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Альберти":
            self.ex = albertiWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Гронсфельд":
            self.ex = gronsfeldWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Вижинер":
            self.ex = viginerWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Кардано":
            self.ex = cardanoWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Ришелье":
            self.ex = richelieuWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Плейфер":
            self.ex = playfairWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Вернам":
            self.ex = vernamWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Хилл":
            self.ex = hillWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Гаммирование":
            self.ex = gammWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Частотный анализ":
            self.ex = chastWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Криптоанализ полиалфавитных шифров":
            self.ex = polyWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "DES":
            self.ex = desWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "ГОСТ":
            self.ex = gostWindow()
            self.ex.show()


class adbashWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(adbashWindow, self).__init__()
        self.ui = Ui_AdbashWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)

    def btnClicked(self):
        self.ui.plainTextEdit_2.setPlainText(codingAtbash(self.ui.plainTextEdit.toPlainText()))

    def btnClicked_2(self):
        self.ui.plainTextEdit_3.setPlainText(codingAtbash(self.ui.plainTextEdit_2.toPlainText()))

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()

class skitalaWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(skitalaWindow, self).__init__()
        self.ui = Ui_SkitalaWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)

    def btnClicked(self):
        self.ui.plainTextEdit_2.setPlainText(codingSkitala(self.ui.plainTextEdit.toPlainText(), int(self.ui.spinBox.text())))

    def btnClicked_2(self):
        self.ui.plainTextEdit_3.setPlainText(decodingSkitala(self.ui.plainTextEdit_2.toPlainText(), int(self.ui.spinBox.text())).replace("*",''))

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.spinBox.clear()

class caezarWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(caezarWindow, self).__init__()
        self.ui = Ui_CaezarWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)

    def btnClicked(self):
        try:
            temp = int(self.ui.lineEdit_4.text())
        except Exception:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Введите число!")
            msgBox.exec_()
            return None
        self.ui.plainTextEdit_2.setPlainText(codingCaesar(self.ui.plainTextEdit.toPlainText(), temp, 1))

    def btnClicked_2(self):
        try:
            temp = int(self.ui.lineEdit_4.text())
        except Exception:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Введите число!")
            msgBox.exec_()
            return None
        self.ui.plainTextEdit_3.setPlainText(codingCaesar(self.ui.plainTextEdit_2.toPlainText(), temp, -1))

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.lineEdit_4.clear()

class polybiusWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(polybiusWindow, self).__init__()
        self.ui = Ui_PolybiusWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)

    def btnClicked(self):
        self.ui.plainTextEdit_2.setPlainText(codingPolybius1(self.ui.plainTextEdit.toPlainText(), 1))

    def btnClicked_2(self):
        self.ui.plainTextEdit_3.setPlainText(codingPolybius1(self.ui.plainTextEdit_2.toPlainText(), -1))

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()

class albertiWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(albertiWindow, self).__init__()
        self.ui = Ui_AlbertiWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)

    def btnClicked(self):
        self.ui.plainTextEdit_2.setPlainText(codingAlberti(self.ui.plainTextEdit.toPlainText(), self.ui.lineEdit.text(), self.ui.lineEdit_4.text(), 1))

    def btnClicked_2(self):
        self.ui.plainTextEdit_3.setPlainText(codingAlberti(self.ui.plainTextEdit_2.toPlainText(), self.ui.lineEdit.text(), self.ui.lineEdit_4.text(), -1))

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_4.clear()

class gronsfeldWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(gronsfeldWindow, self).__init__()
        self.ui = Ui_GronsfeldWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)

    def btnClicked(self):
        self.ui.plainTextEdit_2.setPlainText(codingGronsfeld(self.ui.plainTextEdit.toPlainText(), self.ui.lineEdit_4.text(), 1))

    def btnClicked_2(self):
        self.ui.plainTextEdit_3.setPlainText(codingGronsfeld(self.ui.plainTextEdit_2.toPlainText(), self.ui.lineEdit_4.text(), -1))

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.lineEdit_4.clear()

class viginerWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(viginerWindow, self).__init__()
        self.ui = Ui_ViginerWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)

    def btnClicked(self):
        self.ui.plainTextEdit_2.setPlainText(codingViginer(self.ui.plainTextEdit.toPlainText(), self.ui.lineEdit_4.text(), 1))

    def btnClicked_2(self):
        self.ui.plainTextEdit_3.setPlainText(codingViginer(self.ui.plainTextEdit_2.toPlainText(), self.ui.lineEdit_4.text(), -1))

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.lineEdit_4.clear()

class cardanoWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(cardanoWindow, self).__init__()
        self.ui = Ui_CardanoWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        #self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_4)
        self.ui.plainTextEdit.textChanged.connect(self.magic)

    def magic(self):
        tmp = self.ui.plainTextEdit.toPlainText()
        self.ui.label_4.setText(str(len(tmp)))

    def btnClicked(self):
        self.ui.label_5.setVisible(False)
        arr, res = codingCardano(self.ui.plainTextEdit.toPlainText(), int(self.ui.spinBox.text()))
        self.ui.plainTextEdit_3.setPlainText(res)
        res1 = decodingCardano(arr, res)
        self.ui.plainTextEdit_2.setPlainText(res1)
        arr = str(arr)
        arr = arr.replace('[', "")
        arr = arr.replace(']', "")
        arr = arr.replace("'", "")
        self.ui.label_5.setText(str(arr))
        self.ui.label_5.setVisible(False)

    #def btnClicked_2(self):
        #arr, res = codingCardano(self.ui.plainTextEdit.toPlainText(), int(self.ui.spinBox.text()))
        res1 = decodingCardano(arr, res)
        #self.ui.plainTextEdit_2.setPlainText(decodingCardano(self.ui.plainTextEdit_3.setPlainText, self.ui.label_5.text()))

    def btnClicked_4(self):
        #arr, res = codingCardano(self.ui.plainTextEdit.toPlainText(), int(self.ui.spinBox.text()))
        #self.ui.label_5.setText(str(arr))
        if self.ui.label_5.isVisible() == False:
            self.ui.label_5.setVisible(True)
        else:
            self.ui.label_5.setVisible(False)

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.spinBox.clear()
        self.ui.label_5.clear()

class richelieuWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(richelieuWindow, self).__init__()
        self.ui = Ui_RichelieuWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.risheleKeyValidator = QtGui.QRegExpValidator(QtCore.QRegExp("(\(([0-9]+\,)*[0-9]+\))+"))
        self.ui.lineEdit.setValidator(self.ui.risheleKeyValidator)

    def btnClicked(self):
        key = re.findall('\(([\d,]*)\)', self.ui.lineEdit.text())
        parts = []
        for i in key:
            parts.append([int(j) for j in i.split(',')])
        self.ui.plainTextEdit_3.setPlainText(codingRichelieu(self.ui.plainTextEdit.toPlainText(), parts, 1))

    def btnClicked_2(self):
        key = re.findall('\(([\d,]*)\)', self.ui.lineEdit.text())
        parts = []
        for i in key:
            parts.append([int(j) for j in i.split(',')])
        self.ui.plainTextEdit_2.setPlainText(codingRichelieu(self.ui.plainTextEdit_3.toPlainText(), parts, 2))

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.lineEdit.clear()

class playfairWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(playfairWindow, self).__init__()
        self.ui = Ui_PlayfairWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)

    def btnClicked(self):
        self.ui.plainTextEdit_2.setPlainText(codingPlayfair(self.ui.plainTextEdit.toPlainText(), self.ui.lineEdit_4.text()))

    def btnClicked_2(self):
        self.ui.plainTextEdit_3.setPlainText(decodingPlayfair(self.ui.plainTextEdit_2.toPlainText(), self.ui.lineEdit_4.text()))

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.lineEdit_4.clear()

class vernamWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(vernamWindow, self).__init__()
        self.ui = Ui_VernamWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_4)

    def btnClicked(self):
        self.ui.plainTextEdit_2.setPlainText(codingVernam(self.ui.plainTextEdit.toPlainText(), self.ui.lineEdit_4.text(), 1))

    def btnClicked_2(self):
        self.ui.plainTextEdit_3.setPlainText(codingVernam(self.ui.plainTextEdit_2.toPlainText(), self.ui.lineEdit_4.text(), -1))

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.lineEdit_4.clear()

    def btnClicked_4(self):
        if not self.ui.plainTextEdit.toPlainText() or not self.ui.lineEdit_4.text() or not self.ui.plainTextEdit_2.toPlainText():
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Введите данные!")
            msgBox.exec_()
            return ("")
        text = self.ui.plainTextEdit.toPlainText()
        textBin = ""
        for i in text:
            textBin+=bin(ord(i))[2:].zfill(25)
        key = self.ui.lineEdit_4.text()
        keyBin = ""
        for i in key:
            keyBin+=bin(ord(i))[2:].zfill(25)
        res = self.ui.plainTextEdit_2.toPlainText()
        res1 = ""
        for i in res:
            res1+=(i+'                       ')
        tmp1 = ""
        for i in range(len(textBin)):
            tmp1 += xor(textBin[i], keyBin[i])

        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")
        fil = open(path, 'w', encoding='utf-8')
        textRes = ""
        for i in text:
            textRes+=(i+'                       ')
        keyRes = ""
        for i in key:
            keyRes+=(i+'                       ')
        fil.write('Исходный текст:' + '\n')
        #fil.write(textRes + '\n')
        fil.write(textBin + '\n')
        #fil.write(keyRes + '\n')
        fil.write('Ключ:' + '\n')
        fil.write(keyBin + '\n')
        fil.write('Результат:' + '\n')
        fil.write(tmp1 + '\n')
        #fil.write(res1 + '\n')
        fil.close()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Успешно")
        msgBox.setText("Успешно выгружено!")
        msgBox.exec_()

class hillWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(hillWindow, self).__init__()
        self.ui = Ui_HillWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)

    def btnClicked(self):
        self.ui.plainTextEdit_2.setPlainText(codingHill(self.ui.plainTextEdit.toPlainText(), self.ui.lineEdit_4.text()))

    def btnClicked_2(self):
        self.ui.plainTextEdit_3.setPlainText(decodingHill(self.ui.plainTextEdit_2.toPlainText(), self.ui.lineEdit_4.text()))

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.lineEdit_4.clear()

class gammWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(gammWindow, self).__init__()
        self.ui = Ui_GammWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_4)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_5.clicked.connect(self.btnClicked_5)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.pushButton_6.clicked.connect(self.btnClicked_6)
        self.ui.pushButton_9.clicked.connect(self.btnClicked_9)
        self.ui.pushButton_7.clicked.connect(self.btnClicked_7)
        self.ui.pushButton_8.clicked.connect(self.btnClicked_8)

    #загрузить файл - зашифровать сообщение из файла
    def btnClicked_4(self):
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")

        file = open(path, 'rb')
        text = file.read()
        print(text)
        print('Файл считан!')
        file.close()
        if len(text) <= 50:
            self.ui.plainTextEdit.setPlainText(str(text))
        if not self.ui.plainTextEdit_4.toPlainText():
            # if not self.ui.lineEdit.text() or not self.ui.lineEdit_2.text() or not self.ui.lineEdit_3.text() or not self.ui.lineEdit_5.text():
            #     msgBox = QtWidgets.QMessageBox()
            #     msgBox.setWindowTitle("Ошибка")
            #     msgBox.setText("Введите ключ или данные для его генерации!")
            #     msgBox.exec_()
            #     return ("")
            res = genGamma(self.ui.lineEdit.text(), self.ui.lineEdit_2.text(), self.ui.lineEdit_3.text(), self.ui.lineEdit_5.text(), text)
            if len(res) <= 50:
                self.ui.plainTextEdit_4.setPlainText(str(res))
        else:
            res = self.ui.plainTextEdit_4.toPlainText()
        # if len(res) <= 500000:
        #     self.ui.plainTextEdit_4.setPlainText(str(res))
        print('гамма сгенерирована!')
        print('text', text)
        print('lenT', len(text))
        print('gam', res)
        print('lenG', len(res))
        res1 = codingGamma1(res, text)
        print('res1', res1)
        print('lenR', len(res1))
        print('Зашифровано!')

        if len(res1) < 50:
            self.ui.plainTextEdit_3.setPlainText(str(res1))
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Сообщение")
            msgBox.setText("Размер зашифрованного сообщения велик для вывода. Выберите файл для выгрузки!")
            msgBox.exec_()
            path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
            #print(path)
            if path == "":
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Откройте файл!")
                msgBox.exec_()
                return ("")
            fil = open(path, 'wb')
            fil.write(res1)
            fil.close()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Успешно")
            msgBox.setText("Успешно выгружено!")
            msgBox.exec_()

    def messbox(self, a, b):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle(a)
        msgBox.setText(b)
        msgBox.exec_()
        return ("")

    #зашифрование
    def btnClicked(self):
        res = codingGamma(self.ui.plainTextEdit_4.toPlainText(), self.ui.plainTextEdit.toPlainText())
        self.ui.plainTextEdit_3.setPlainText(res)

    #генерация гаммы
    def btnClicked_5(self):
        res = genGamma(self.ui.lineEdit.text(), self.ui.lineEdit_2.text(), self.ui.lineEdit_3.text(), self.ui.lineEdit_5.text(), self.ui.plainTextEdit.toPlainText())
        self.ui.plainTextEdit_4.setPlainText(str(res))

    #расшифрование
    def btnClicked_2(self):
        res = codingGamma(self.ui.plainTextEdit_4.toPlainText(), self.ui.plainTextEdit_3.toPlainText())
        self.ui.plainTextEdit_2.setPlainText(res)

    #выгрузить ключ в файл
    def btnClicked_6(self):
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        print(path)
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")
        fil = open(path, 'w', encoding='utf-8')
        fil.write(self.ui.plainTextEdit_4.toPlainText())
        fil.close()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Успешно")
        msgBox.setText("Успешно выгружено!")
        msgBox.exec_()
        return None

    #выгрузить в файл зашифрованное сообщение
    def btnClicked_9(self):

        correct_encoding = self.ui.label.text()

        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        print(path)
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")
        fil = open(path, 'w', encoding='utf-8')
        fil.write(self.ui.plainTextEdit_3.toPlainText())
        fil.close()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Успешно")
        msgBox.setText("Успешно выгружено!")
        msgBox.exec_()
        return None

    #зашифровать ключом из файла
    def btnClicked_7(self):
        editorProgram = 'notepad'
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")

        process = QtCore.QProcess(self)
        process.start(editorProgram, [path])

        self.setEnabled(False)
        process.finished.connect(lambda: self.setEnabled(True))

        fil = open(path, 'r', encoding='utf-8')
        text = fil.read()
        fil.close()
        self.ui.plainTextEdit_4.setPlainText(text)

    #расшифровать ключом из файла
    def btnClicked_8(self):
        editorProgram = 'notepad'
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")

        process = QtCore.QProcess(self)
        process.start(editorProgram, [path])

        self.setEnabled(False)
        process.finished.connect(lambda: self.setEnabled(True))

        fil = open(path, 'r', encoding='utf-8')
        text = fil.read()
        fil.close()
        self.ui.plainTextEdit_4.setPlainText(text)

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.plainTextEdit_4.clear()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_5.clear()



class chastWindow(QtWidgets.QMainWindow):
    global bukvaArray
    def __init__(self):
        super(chastWindow, self).__init__()
        self.ui = Ui_ChastWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.pushButton_5.clicked.connect(self.btnClicked_5)
        self.ui.pushButton_6.clicked.connect(self.btnClicked_6)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_4)

    def btnClicked(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.plainTextEdit_3.clear()

    def btnClicked_3(self):
        global bukvaArray
        try:
            text, bukvaArray = chastota(self.ui.plainTextEdit.toPlainText())
        except Exception:
            return ("")
        else:
            self.ui.plainTextEdit_2.setPlainText(text)
            self.ui.plainTextEdit_3.setPlainText((printBukva(bukvaArray)))


    def btnClicked_5(self):
        global bukvaArray
        try:
            gistogramma(self.ui.plainTextEdit.toPlainText(), bukvaArray)
        except Exception:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Нажмите сначала расшифровать!")
            msgBox.exec_()
            return ("")

    def btnClicked_6(self):
        global bukvaArray
        #text, bukvaArray = chastota(self.ui.plainTextEdit.toPlainText())
        try:
            restext, bukvaArray = zamena(self.ui.lineEdit.text(), self.ui.lineEdit_2.text(), bukvaArray, self.ui.plainTextEdit_2.toPlainText())
            self.ui.plainTextEdit_3.setPlainText((printBukva(bukvaArray)))

        except Exception:
            return ("")
        else:
            self.ui.plainTextEdit_2.setPlainText(restext)

    def btnClicked_4(self):
        global bukvaArray
        encoding = [
            'utf-8',
            'cp500',
            'utf-16',
            'GBK',
            'windows-1251',
            'ASCII',
            'US-ASCII',
            'Big5'
        ]

        correct_encoding = ''

        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")

        for enc in encoding:
            try:
                open(path, encoding=enc).read()
            except (UnicodeDecodeError, LookupError):
                pass
            else:
                correct_encoding = enc
                print('Done!')
                print(correct_encoding)
                break

        file = open(path, 'r', encoding=correct_encoding)
        text = file.read()
        print(text)
        print('Файл считан!')
        file.close()
        if len(text) <= 50:
            self.ui.plainTextEdit.setPlainText(str(text))
        res1, bukvaArray = chastota(text)
        print('Зашифровано!')

        if len(res1) < 50:
            self.ui.plainTextEdit_2.setPlainText(str(res1))
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Сообщение")
            msgBox.setText("Размер расшифрованного сообщения велик для вывода. Выберите файл для выгрузки!")
            msgBox.exec_()
            path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
            # print(path)
            if path == "":
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Откройте файл!")
                msgBox.exec_()
                return ("")
            fil = open(path, 'w', encoding=correct_encoding)
            fil.write(res1)
            fil.close()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Успешно")
            msgBox.setText("Успешно выгружено!")
            msgBox.exec_()

    def btnClicked_2(self):
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        print(path)
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")
        fil = open(path, 'w', encoding='utf-8')
        fil.write(self.ui.plainTextEdit_2.toPlainText())
        fil.close()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Успешно")
        msgBox.setText("Успешно выгружено!")
        msgBox.exec_()
        return None

class polyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(polyWindow, self).__init__()
        self.ui = Ui_PolialphabetWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.pushButton_6.clicked.connect(self.btnClicked_6)
        self.ui.pushButton_8.clicked.connect(self.btnClicked_8)
        self.ui.pushButton_7.clicked.connect(self.btnClicked_7)
        self.ui.pushButton_5.clicked.connect(self.btnClicked_5)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_4)

    def btnClicked_4(self):
        self.ui.comboBox_2.clear()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_4.clear()
        self.ui.lineEdit.clear()


    #найти длину ключа
    def btnClicked_2(self):
        if not self.ui.plainTextEdit.toPlainText():
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Введите текст!")
            msgBox.exec_()
            return ("")
        else:
            if self.ui.comboBox.currentText() == "Метод индексных совпадений":
                try:
                    self.ui.lineEdit.setText(str(indexOfMatches.lengthOfKey(self.ui.plainTextEdit.toPlainText())))
                except Exception:
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setWindowTitle("Ошибка")
                    msgBox.setText("Не удалось определить длину ключа!")
                    msgBox.exec_()
                    return ("")
            if self.ui.comboBox.currentText() == "Автокорреляционный метод":
                try:
                    self.ui.lineEdit.setText(str(autocorrelationMethod.lengthOfKey(self.ui.plainTextEdit.toPlainText())))
                except Exception:
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setWindowTitle("Ошибка")
                    msgBox.setText("Не удалось определить длину ключа!")
                    msgBox.exec_()
                    return ("")
            if self.ui.comboBox.currentText() == "Метод Касиски":
                try:
                    self.ui.lineEdit.setText(str(casiski.lengthOfKey(self.ui.plainTextEdit.toPlainText())))
                except Exception:
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setWindowTitle("Ошибка")
                    msgBox.setText("Не удалось определить длину ключа!")
                    msgBox.exec_()
                    return ("")

    #найти ключ
    def btnClicked_3(self):
        if not self.ui.plainTextEdit.toPlainText() or not self.ui.lineEdit.text():
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Заполните поля!")
            msgBox.exec_()
            return ("")
        else:
            if self.ui.comboBox.currentText() == "Метод индексных совпадений":
                try:
                    arr = indexOfMatches.findKey(self.ui.plainTextEdit.toPlainText(), int(self.ui.lineEdit.text()))
                    if type(arr) == str:
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setWindowTitle("Ошибка")
                        msgBox.setText("Не удалось определить ключ!")
                        msgBox.exec_()
                        return ("")
                    else:
                        self.ui.comboBox_2.clear()
                        for i in arr:
                            self.ui.comboBox_2.addItem(i)
                except Exception:
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setWindowTitle("Ошибка")
                    msgBox.setText("Не удалось определить ключ!")
                    msgBox.exec_()
                    return ("")
            if self.ui.comboBox.currentText() == "Автокорреляционный метод":
                try:
                    self.ui.plainTextEdit_4.setPlainText(autocorrelationMethod.autocorrelationMethod(self.ui.plainTextEdit.toPlainText(), int(self.ui.lineEdit.text())))
                except Exception:
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setWindowTitle("Ошибка")
                    msgBox.setText("Не удалось определить ключ!")
                    msgBox.exec_()
                    return ("")
            if self.ui.comboBox.currentText() == "Метод Касиски":
                try:
                    self.ui.plainTextEdit_4.setPlainText(casiski.casiski(self.ui.plainTextEdit.toPlainText(), int(self.ui.lineEdit.text())))
                except Exception:
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setWindowTitle("Ошибка")
                    msgBox.setText("Не удалось определить ключ!")
                    msgBox.exec_()
                    return ("")

    #применить ключ
    def btnClicked_6(self):
        self.ui.plainTextEdit_4.setPlainText(self.ui.comboBox_2.currentText())

    #расшифровать
    def btnClicked_8(self):
        if not self.ui.plainTextEdit.toPlainText() or not self.ui.plainTextEdit_4.toPlainText():
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Заполните поля!")
            msgBox.exec_()
            return ("")
        else:
            self.ui.plainTextEdit_2.setPlainText(rasshifrovka(self.ui.plainTextEdit.toPlainText(), self.ui.plainTextEdit_4.toPlainText()))

    #гистограмма
    def btnClicked_7(self):
        if not self.ui.plainTextEdit.toPlainText():
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Заполните поля!")
            msgBox.exec_()
            return ("")
        else:
            text = self.ui.plainTextEdit.toPlainText()
            text1 = indexOfMatches.oneRegistr(text)
            dictRus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
            dictEng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            dictEngStr = "abcdefghijklmnopqrstuvwxyz"
            dictRusStr = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            dict = indexOfMatches.alphabet(text1)
            text2 = ""
            for i in text1:
                if i in dict:
                    text2+=i
            bukvaAndFreq = []
            for i in dict:
                bukvaAndFreq.append(indexOfMatches.BukvaAndChastota(i))
            indexOfMatches.findFreq(bukvaAndFreq, text2)

            index = np.arange(len(dict))
            values1 = []

            tmp = []
            for i in range(len(dict)):
                for j in range(len(bukvaAndFreq)):
                    if bukvaAndFreq[j].bukva == dict[i]:
                        res = bukvaAndFreq[j].bukva
                        values1.append(bukvaAndFreq[j].chastota)
                        tmp.append(res)
                        break

            plt.figure(figsize=(12, 7))
            bw = 0.4
            plt.title("Frequency", fontsize=20)
            plt.bar(index, values1, bw, color='b')
            plt.xticks(index + bw, tmp)
            plt.show()
            return None

    def btnClicked_5(self):
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        print(path)
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")
        fil = open(path, 'w', encoding='utf-8')
        fil.write(self.ui.plainTextEdit_2.toPlainText())
        fil.close()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Успешно")
        msgBox.setText("Успешно выгружено!")
        msgBox.exec_()
        return None


    def btnClicked(self):
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")

        file = open(path, 'r', encoding='utf-8')
        text = file.read()
        print(text)
        print('Файл считан!')
        lengthOfKey = 0
        file.close()
        if len(text) <= 50:
            self.ui.plainTextEdit.setPlainText(str(text))
        if self.ui.comboBox.currentText() == "Метод индексных совпадений":
            lengthOfKey = indexOfMatches.lengthOfKey(text)
            if lengthOfKey == 0:
                lengthOfKey = autocorrelationMethod.lengthOfKey(text)
                if lengthOfKey == 0:
                    lengthOfKey = casiski.lengthOfKey(text)
        elif self.ui.comboBox.currentText() == "Автокорреляционный метод":
            lengthOfKey = autocorrelationMethod.lengthOfKey(text)
            if lengthOfKey == 0:
                lengthOfKey = indexOfMatches.lengthOfKey(text)
                if lengthOfKey == 0:
                    lengthOfKey = casiski.lengthOfKey(text)
        elif self.ui.comboBox.currentText() == "Метод Касиски":
            lengthOfKey = casiski.lengthOfKey(text)
            if lengthOfKey == 0:
                lengthOfKey = autocorrelationMethod.lengthOfKey(text)
                if lengthOfKey == 0:
                    lengthOfKey = indexOfMatches.lengthOfKey(text)
        print('Длина ключа определена!!')

        print(lengthOfKey)
        # if len(str(lengthOfKey)) < 10:
        #     self.ui.lineEdit.setText(str(lengthOfKey))

        key = casiski.casiski(text, lengthOfKey)

        # if len(key) < 10:
        #     self.ui.plainTextEdit_4.setPlainText(key)
        #else:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Сообщение")
        msgBox.setText("Выберите файл для выгрузки ключа!")
        msgBox.exec_()
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        # print(path)
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")
        fil = open(path, 'w', encoding='utf-8')
        fil.write(key)
        fil.close()

        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Сообщение")
        msgBox.setText("Выберите файл для выгрузки расшифрованного сообщения!")
        msgBox.exec_()
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        # print(path)
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")
        fil = open(path, 'w', encoding='utf-8')
        fil.write(rasshifrovka(text, key))
        fil.close()

        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Успешно")
        msgBox.setText("Успешно выгружено!")
        msgBox.exec_()


def rasshifrovka(text, key):
    dictRus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dictEng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictEngStr = "abcdefghijklmnopqrstuvwxyz"
    dictRusStr = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    dict = ""
    dict1 = ""
    for i in text:
        if i in dictRus:
            dict = dictRus
            dict1 = dictRusStr
        elif i in dictRusStr:
            dict = dictRusStr
            dict1 = dictRus
        elif i in dictEng:
            dict = dictEng
            dict1 = dictEngStr
        elif i in dictEngStr:
            dict = dictEngStr
            dict1 = dictEng
    res = ""
    resKey = ""
    count = 0
    for i in text:
        if i in dict or i in dict1:
            resKey+=key[count % len(key)]
            count+=1
    count = 0
    for i in range(len(text)):
        if text[i] in dict and resKey[count] in dict:
            res += dict[(dict.index(text[i]) - dict.index(resKey[count])) % len(dict)]
            count+=1
        elif text[i] in dict and resKey[count] in dict1:
            res += dict[(dict.index(text[i]) - dict1.index(resKey[count])) % len(dict)]
            count+=1
        elif text[i] in dict1 and resKey[count] in dict1:
            res += dict1[(dict1.index(text[i]) - dict1.index(resKey[count])) % len(dict1)]
            count+=1
        elif text[i] in dict1 and resKey[count] in dict:
            res += dict1[(dict1.index(text[i]) - dict.index(resKey[count])) % len(dict1)]
            count+=1
        else:
            res+=text[i]
    return res

class desWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(desWindow, self).__init__()
        self.ui = Ui_DesWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_4)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_6.clicked.connect(self.btnClicked_6)
        self.ui.pushButton_5.clicked.connect(self.btnClicked_5)
        self.ui.pushButton_7.clicked.connect(self.btnClicked_7)
        self.ui.pushButton_8.clicked.connect(self.btnClicked_8)

    #Зашифровать
    def btnClicked(self):
        text = self.ui.plainTextEdit.toPlainText()
        keys = self.ui.plainTextEdit_2.toPlainText()
        if self.ui.comboBox.currentText() == 'ECB - режим электронной кодовой книги':
            try:
                self.ui.plainTextEdit_3.setPlainText(str(ECB(keys, text, 1)))
            except Exception:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка!")
                msgBox.exec_()
                return ("")
        if self.ui.comboBox.currentText() == 'CBC - режим сцепления блоков шифротекста':
            # try:
            vector_init = self.ui.plainTextEdit_5.toPlainText()
            self.ui.plainTextEdit_3.setPlainText(str(CBC(keys, text, 1, vector_init)))
            # except Exception:
            #     msgBox = QtWidgets.QMessageBox()
            #     msgBox.setWindowTitle("Ошибка")
            #     msgBox.setText("Ошибка!")
            #     msgBox.exec_()
            #     return ("")
        if self.ui.comboBox.currentText() == 'CFB - режим обратной связи по шифротексту':
            try:
                vector_init = self.ui.plainTextEdit_5.toPlainText()
                self.ui.plainTextEdit_3.setPlainText(str(CFB(keys, text, 1, vector_init)))
            except Exception:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка!")
                msgBox.exec_()
                return ("")
        if self.ui.comboBox.currentText() == 'OFB - режим обратной связи по выходу':
            try:
                vector_init = self.ui.plainTextEdit_5.toPlainText()
                self.ui.plainTextEdit_3.setPlainText(str(OFB(keys, text, 1, vector_init)))
            except Exception:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка!")
                msgBox.exec_()
                return ("")

    #Расшифровать
    def btnClicked_4(self):
        text = self.ui.plainTextEdit_3.toPlainText()
        keys = self.ui.plainTextEdit_2.toPlainText()
        if self.ui.comboBox.currentText() == 'ECB - режим электронной кодовой книги':
            try:
                self.ui.plainTextEdit_4.setPlainText(str(ECB(keys, text, 2)))
            except Exception:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка!")
                msgBox.exec_()
                return ("")
        if self.ui.comboBox.currentText() == 'CBC - режим сцепления блоков шифротекста':
            try:
                vector_init = self.ui.plainTextEdit_5.toPlainText()
                self.ui.plainTextEdit_4.setPlainText(str(CBC(keys, text, 2, vector_init)))
            except Exception:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка!")
                msgBox.exec_()
                return ("")
        if self.ui.comboBox.currentText() == 'CFB - режим обратной связи по шифротексту':
            try:
                vector_init = self.ui.plainTextEdit_5.toPlainText()
                self.ui.plainTextEdit_4.setPlainText(str(CFB(keys, text, 2, vector_init)))
            except Exception:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка!")
                msgBox.exec_()
                return ("")
        if self.ui.comboBox.currentText() == 'OFB - режим обратной связи по выходу':
            try:
                vector_init = self.ui.plainTextEdit_5.toPlainText()
                self.ui.plainTextEdit_4.setPlainText(str(OFB(keys, text, 2, vector_init)))
            except Exception:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка!")
                msgBox.exec_()
                return ("")

    #Сгенерировать ключ по умолчанию
    def btnClicked_3(self):
        try:
            keys = genKeys('DESkey56')
            keysText = ''
            for i in keys:
                keysText+=i
            self.ui.plainTextEdit_2.setPlainText(keysText)
        except Exception:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Ошибка!")
            msgBox.exec_()
            return ("")

    #Загрузить ключ из файла
    def btnClicked_2(self):
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")

        fil = open(path, 'r', encoding='utf-8')
        keys = fil.read()
        fil.close()
        for i in keys:
            if i != '1' or i != 1 or i != '0' or i != 0 or len(keys) != 16 * 48:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка в ключе!")
                msgBox.exec_()
                return ("")
        self.ui.plainTextEdit_2.setPlainText(keys)

    #Выгрузить в файл
    def btnClicked_6(self):
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")
        fil = open(path, 'w', encoding='utf-8')
        fil.write(self.ui.plainTextEdit_3.toPlainText())
        fil.close()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Успешно")
        msgBox.setText("Успешно выгружено!")
        msgBox.exec_()
        return None

    def btnClicked_5(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.plainTextEdit_4.clear()

    #Загрузить файл для зашифровки
    def btnClicked_7(self):
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл для зашифровки')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")

        file = open(path, 'rb')
        text = file.read()
        file.close()
        fileToIntArr = []
        for i in text:
            fileToIntArr.append(int(i))
        keys = ''
        if self.ui.plainTextEdit_2.toPlainText() == '':
            keys = ''
        else:
            keys = self.ui.plainTextEdit_2.toPlainText()
        code = bytearray(b"")
        if self.ui.comboBox.currentText() == 'ECB - режим электронной кодовой книги':
            code = ECB(keys, text, 1)
        if self.ui.comboBox.currentText() == 'CBC - режим сцепления блоков шифротекста':
            vector_init = self.ui.plainTextEdit_5.toPlainText()
            code = CBC(keys, text, 1, vector_init)
        if self.ui.comboBox.currentText() == 'CFB - режим обратной связи по шифротексту':
            vector_init = self.ui.plainTextEdit_5.toPlainText()
            code = CFB(keys, text, 1, vector_init)
        if self.ui.comboBox.currentText() == 'OFB - режим обратной связи по выходу':
            vector_init = self.ui.plainTextEdit_5.toPlainText()
            code = OFB(keys, text, 1, vector_init)

        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Сообщение")
        msgBox.setText("Размер зашифрованного сообщения велик для вывода. Выберите файл для выгрузки!")
        msgBox.exec_()
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")
        fil = open(path, 'wb')
        fil.write(code)
        fil.close()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Успешно")
        msgBox.setText("Успешно выгружено!")
        msgBox.exec_()

    #Загрузить файл для расшифровки
    def btnClicked_8(self):
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл для расшифровки')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")

        file = open(path, 'rb')
        text = file.read()
        file.close()
        fileToIntArr = []
        for i in text:
            fileToIntArr.append(int(i))
        keys = ''
        if self.ui.plainTextEdit_2.toPlainText() == '':
            keys = ''
        else:
            keys = self.ui.plainTextEdit_2.toPlainText()
        code = bytearray(b"")
        if self.ui.comboBox.currentText() == 'ECB - режим электронной кодовой книги':
            code = ECB(keys, text, 11)
        if self.ui.comboBox.currentText() == 'CBC - режим сцепления блоков шифротекста':
            vector_init = self.ui.plainTextEdit_5.toPlainText()
            code = CBC(keys, text, 11, vector_init)
        if self.ui.comboBox.currentText() == 'CFB - режим обратной связи по шифротексту':
            vector_init = self.ui.plainTextEdit_5.toPlainText()
            code = CFB(keys, text, 11, vector_init)
        if self.ui.comboBox.currentText() == 'OFB - режим обратной связи по выходу':
            vector_init = self.ui.plainTextEdit_5.toPlainText()
            code = OFB(keys, text, 11, vector_init)

        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Сообщение")
        msgBox.setText("Размер расшифрованного сообщения велик для вывода. Выберите файл для выгрузки!")
        msgBox.exec_()
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")
        fil = open(path, 'wb')
        fil.write(code)
        fil.close()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Успешно")
        msgBox.setText("Успешно выгружено!")
        msgBox.exec_()


class gostWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(gostWindow, self).__init__()
        self.ui = Ui_GostWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_4)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_6.clicked.connect(self.btnClicked_6)
        self.ui.pushButton_5.clicked.connect(self.btnClicked_5)
        self.ui.pushButton_7.clicked.connect(self.btnClicked_7)
        self.ui.pushButton_8.clicked.connect(self.btnClicked_8)

    #Зашифровать
    def btnClicked(self):
        text = self.ui.plainTextEdit.toPlainText()
        keys = self.ui.plainTextEdit_2.toPlainText()
        if self.ui.comboBox.currentText() == 'Простая замена':
            try:
                self.ui.plainTextEdit_3.setPlainText(GOST_zamena(keys, text, 1))
            except Exception:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка!")
                msgBox.exec_()
                return ("")
        if self.ui.comboBox.currentText() == 'Гаммирование с обратной связью':
            try:
                vector_init = self.ui.plainTextEdit_5.toPlainText()
                self.ui.plainTextEdit_3.setPlainText(str(GOST_gamm(keys, text, 1, vector_init)))
            except Exception:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка!")
                msgBox.exec_()
                return ("")

    #Расшифровать
    def btnClicked_4(self):
        text = self.ui.plainTextEdit_3.toPlainText()
        keys = self.ui.plainTextEdit_2.toPlainText()
        if self.ui.comboBox.currentText() == 'Простая замена':
            try:
                self.ui.plainTextEdit_4.setPlainText(str(GOST_zamena(keys, text, 2)))
            except Exception:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка!")
                msgBox.exec_()
                return ("")
        if self.ui.comboBox.currentText() == 'Гаммирование с обратной связью':
            try:
                vector_init = self.ui.plainTextEdit_5.toPlainText()
                self.ui.plainTextEdit_4.setPlainText(str(GOST_gamm(keys, text, 2, vector_init)))
            except Exception:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка!")
                msgBox.exec_()
                return ("")

    #Сгенерировать ключ по умолчанию
    def btnClicked_3(self):
        try:
            keys = genKeys_GOST('this_is_a_pasw_for_GOST_28147_89')
            keysText = ''
            for i in keys:
                keysText+=i
            self.ui.plainTextEdit_2.setPlainText(keysText)
        except Exception:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Ошибка!")
            msgBox.exec_()
            return ("")

    #Загрузить ключ из файла
    def btnClicked_2(self):
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")

        fil = open(path, 'r', encoding='utf-8')
        keys = fil.read()
        fil.close()
        for i in keys:
            if i != '1' or i != 1 or i != '0' or i != 0 or len(keys) != 256:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Ошибка в ключе!")
                msgBox.exec_()
                return ("")
        self.ui.plainTextEdit_2.setPlainText(keys)

    #Выгрузить в файл
    def btnClicked_6(self):
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")
        fil = open(path, 'w', encoding='utf-8')
        fil.write(self.ui.plainTextEdit_3.toPlainText())
        fil.close()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Успешно")
        msgBox.setText("Успешно выгружено!")
        msgBox.exec_()
        return None

    def btnClicked_5(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.plainTextEdit_4.clear()

    #Загрузить файл для зашифровки
    def btnClicked_7(self):
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл для зашифровки')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")

        file = open(path, 'rb')
        text = file.read()
        file.close()
        fileToIntArr = []
        for i in text:
            fileToIntArr.append(int(i))
        keys = ''
        if self.ui.plainTextEdit_2.toPlainText() == '':
            keys = ''
        else:
            keys = self.ui.plainTextEdit_2.toPlainText()
        code = bytearray(b"")
        if self.ui.comboBox.currentText() == 'Простая замена':
            code = GOST_zamena(keys, text, 1)
        if self.ui.comboBox.currentText() == 'Гаммирование с обратной связью':
            vector_init = self.ui.plainTextEdit_5.toPlainText()
            code = GOST_gamm(keys, text, 1, vector_init)

        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Сообщение")
        msgBox.setText("Размер зашифрованного сообщения велик для вывода. Выберите файл для выгрузки!")
        msgBox.exec_()
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")
        fil = open(path, 'wb')
        fil.write(code)
        fil.close()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Успешно")
        msgBox.setText("Успешно выгружено!")
        msgBox.exec_()

    #Загрузить файл для расшифровки
    def btnClicked_8(self):
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл для расшифровки')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")

        file = open(path, 'rb')
        text = file.read()
        file.close()
        fileToIntArr = []
        for i in text:
            fileToIntArr.append(int(i))
        keys = ''
        if self.ui.plainTextEdit_2.toPlainText() == '':
            keys = ''
        else:
            keys = self.ui.plainTextEdit_2.toPlainText()
        code = bytearray(b"")
        if self.ui.comboBox.currentText() == 'Простая замена':
            code = GOST_zamena(keys, text, 11)
        if self.ui.comboBox.currentText() == 'Гаммирование с обратной связью':
            vector_init = self.ui.plainTextEdit_5.toPlainText()
            code = GOST_gamm(keys, text, 11, vector_init)

        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Сообщение")
        msgBox.setText("Размер расшифрованного сообщения велик для вывода. Выберите файл для выгрузки!")
        msgBox.exec_()
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")
        fil = open(path, 'wb')
        fil.write(code)
        fil.close()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Успешно")
        msgBox.setText("Успешно выгружено!")
        msgBox.exec_()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())