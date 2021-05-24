# -*- coding: utf-8 -*-
text = "влцдутжбюцхъяррмшбрхцэооэцгбрьцмйфктъъюьмшэсяцпунуящэйтаьэдкцибр ьцгбрпачкъуцпъбьсэгкцъгуущарцёэвърюуоюэкааэбрняфукабъарпяъафкъиьжяффнйо яфывбнэнфуюгбрьсшьжэтбэёчюъюръегофкбьчябашвёэуъъюаднчжчужцёэвлрнчулб юпцуруньъшсэюъзкцхъяррнрювяспэмасчкпэужьжыатуфуярюравртубурьпэщлафоуф бюацмнубсюкйтаьэдйюнооэгюожбгкбрънцэпотчмёодзцвбцшщвщепчдчдръюьскасэг ъппэгюкдойрсрэвоопчщшоказръббнэугнялёкьсрбёуыэбдэулбюасшоуэтъшкрсдугэфл бубуъчнчтртпэгюкиугюэмэгюккъъпэгяапуфуэзьрадзьжчюрмфцхраююанчёчюъыхьъ цомэфъцпоирькнщпэтэузуябащущбаыэйчдфрпэцъьрьцъцпоилуфэдцойэдятррачкубу фнйтаьэдкцкрннцюабугюуубурьпйюэъжтгюркующоъуфъэгясуоичщщчдцсфырэдщэ ъуяфшёчцюйрщвяхвмкршрпгюопэуцчйтаьэдкцибрьцыяжтюрбуэтэбдуящэубъибрюв ъежагибрбагбрымпуноцшяжцечкфодщоъчжшйуъцхчщвуэбдлдъэгясуахзцэбдэулькнъ щбжяцэьрёдъьвювлрнуяфуоухфекьгцчччгэъжтанопчынажпачкъуъмэнкйрэфщэъьбуд эндадъярьеюэлэтчоубъцэфэвлнёэгфдсэвэёкбсчоукгаутэыпуббцчкпэгючсаъбэнэфърк ацхёваетуфяепьрювържадфёжбьфутощоявьъгупчршуитеачйчирамчюфчоуяюонкяжы кгсцбрясшчйотъъжрсщчл"

class BukvaAndChastota():
    bukva = ""
    chastota = 0

    def __init__(self, bukva):
        self.bukva = bukva
        self.chastota = 0

#приводим к одному регистру
def oneRegistr(text):
    dictRusUp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dictEngUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictEng = "abcdefghijklmnopqrstuvwxyz"
    dictRus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    if alphabet(text) == dictRusUp:
        for i in range(len(text)):
            for j in range(len(dictRus)):
                if text[i] == dictRus[j]:
                    text = text[:i] + dictRusUp[dictRus.index(text[i])] + text[i + 1:]
                    break
    elif alphabet(text) == dictEngUp:
        for i in range(len(text)):
            for j in range(len(dictEng)):
                if text[i] == dictEng[j]:
                    text = text[:i] + dictEngUp[dictEng.index(text[i])] + text[i + 1:]
                    break
    #print(text)
    return text

#какой алфавит
def alphabet(text):
    dictRus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dictEng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictEngStr = "abcdefghijklmnopqrstuvwxyz"
    dictRusStr = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    dict = ""
    for i in text:
        if i in dictRus or i in dictRusStr:
            dict = dictRus
        elif i in dictEng or i in dictEngStr:
            dict = dictEng
    return dict

#буква - частота
def findFreq(chastotaInStroka:list[BukvaAndChastota], stroka):
    for i in range(len(chastotaInStroka)):
        for j in range(len(stroka)):
            if stroka[j] == chastotaInStroka[i].bukva:
                chastotaInStroka[i].chastota += 1
    return None

#Ic в строке
def indexOfMatchesInStr(stroka, dict:str):
    chastotaInStroka = []
    for i in dict:
        chastotaInStroka.append(BukvaAndChastota(i))
    findFreq(chastotaInStroka, stroka)
    return chastotaInStroka

#Ic в матрице
def indexOfMatches(mtx:list, dict:str):
    arrOfIndexes = []
    for i in mtx:
        chastotaInStroka = indexOfMatchesInStr(i, dict)
        Ic = 0
        for symb in chastotaInStroka:
            Ic += ((symb.chastota * (symb.chastota - 1)) / (len(i) * (len(i) - 1)))
        arrOfIndexes.append(Ic)
    print('arr', arrOfIndexes)
    return arrOfIndexes

#сравнение, что все Ic больше - равно Ic эталонного
def arrIc(arr:list, Ic):
    for i in arr:
        if i < Ic:
            return False
    return True

#сдвиг
def sdvig(chastotaInEachStroka:list[BukvaAndChastota]):
    for i in range(1, len(chastotaInEachStroka)):
        chastotaInEachStroka[i].chastota, chastotaInEachStroka[0].chastota = chastotaInEachStroka[0].chastota, chastotaInEachStroka[i].chastota

def findSdvigForOneStr(chastotaInEachStroka: list[list[BukvaAndChastota]], numberOfStroka, mtx, dict):
    for t in range(len(dict)):
        Ic1 = 0
        for j in range(len(chastotaInEachStroka[numberOfStroka])):
            Ic1 += chastotaInEachStroka[0][j].chastota * chastotaInEachStroka[numberOfStroka][j].chastota
        Ic1 = Ic1 / (len(mtx[0]) * len(mtx[numberOfStroka]))
        if Ic1 >= 0.053:
            return t
        sdvig(chastotaInEachStroka[numberOfStroka])
    return 'Невозможно подобрать сдвиг!'

def lengthOfKey(text):
    text2 = ""
    text1 = oneRegistr(text)
    dict = alphabet(text1)
    for i in text1:
        if i in dict:
            text2+=i

    dictRus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dictEng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    IcRus = 0.0553
    IcEng = 0.0644
    Ic = 0
    if dict == dictRus:
        Ic = IcRus
    else:
        Ic = IcEng

    try:
        t = 1
        mtx = []
        for i in range(t):
            mtx.append("")
        for char in range(len(text2)):
            mtx[char % t] += text2[char]
        #print(mtx)
        arrOfIndexes = indexOfMatches(mtx, dict)

        while arrIc(arrOfIndexes, Ic) != True:
            t +=1
            mtx = []
            for i in range(t):
                mtx.append("")
            for char in range(len(text2)):
                mtx[char % t] += text2[char]
            #print(mtx)
            arrOfIndexes = indexOfMatches(mtx, dict)
    except Exception:
        print('ERROR!')
        return 'Error'

    lenKey = t
    return lenKey

def findKey(text, lenKey):
    text2 = ""
    text1 = oneRegistr(text)
    dict = alphabet(text1)
    for i in text1:
        if i in dict:
            text2 += i

    dictRus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dictEng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    IcRus = 0.0553
    IcEng = 0.0644
    Ic = 0
    if dict == dictRus:
        Ic = IcRus
    else:
        Ic = IcEng

    mtx = []
    for i in range(lenKey):
        mtx.append("")
    for char in range(len(text2)):
        mtx[char % lenKey] += text2[char]
    #print(mtx)

    chastotaInEachStroka = []
    for i in mtx:
        chastotaInEachStroka.append(indexOfMatchesInStr(i, dict))

    # indOfStr = []
    # for i in range(1, len(chastotaInEachStroka)):
    #     Ic1 = 0
    #     for j in range(len(chastotaInEachStroka[i])):
    #         Ic1 += (chastotaInEachStroka[0][j].chastota * chastotaInEachStroka[i][j].chastota) / (len(mtx[0]) * len(mtx[i]))
    #     indOfStr.append(Ic1)
    # print(indOfStr)

    sdvigArr = []
    for i in range(1, len(chastotaInEachStroka)):
        sdvigArr.append(findSdvigForOneStr(chastotaInEachStroka, i, mtx, dict))
    print(sdvigArr)
    for i in sdvigArr:
        if type(i) == str:
            print('ERROR!')
            return 'Error'

    key = []
    for i in range(len(dict)):
        keyOne = dict[i]
        for j in range(len(sdvigArr)):
            keyOne+=dict[(i - sdvigArr[j]) % len(dict)]
        key.append(keyOne)

    for i in key:
        print(i)

    return key

# lengthOfKey(text)
# findKey(text, lengthOfKey(text))
