# -*- coding: utf-8 -*-
text = "мыгопцсвцрпбьбжбчыъшдьъюорпуънжыпьгбпцльлеидхчгзчнгжбрлгччгюцлздхекдшшвдлчщмъхсоккуцнпгичбрдышхяылияырньщжазшшкгтххичщмщппггтрихоржечщюыкнцяюнюгкхмътблтпшязышэипхъзынющърбыкщоьоырчмхэбчыъвцрльчмщокулдщлеыщлдчзгггпхгедцавпырдышбдаьмшдщмбцшпиеижзшшиусшачыжсщфрзчыриуцегепъпепфрямемиуъщщбугзипиццуузалпифуатхыикалгвччжеьоюбтыъзылочфупумрогььъзинмшдпггцшгакфмяышбьщшжыксгюкфияцлиотьюипхгяороэкьъзищмыкхъппшрюкнгздшрыпхэхвржгквкящшргпнгычцмъчщсъкквкюшагдцжяэуеяарпатцжкмрхуицжцпгггптлчффюащлещпълкыыэзчмщитклдьсгшдхбдышазжчрксуююхшкдуэлкыжпцмчжмлъмыищмачцлчыраечупакяздмвюяфузжьсзяищодошиэкхочъысэолружьжеьоиямегбзпжыьцюбищммчсжгкчгачьмждясопчщмжфпепъжвпчрчышодмшхьцжсечълтюшхьцжржьпмбзмжщдялдцлхяъьмбтвггцеущчшяжксггткжечзрдхэмопчъдъьмжчслтющмбьбжщцрржтнжчфжлттъгюьхъикьмгтвюжкяюхыыэдычгъчщмзшрцгчшясиылцзьгъччготырдышжфуыньщукьцьюяэлзитбгзуусмчпэичьлдмшбдшшрдхэхичыиябфмвъсжбтыъзчырчщеккзьлдьхмэпчлтхннжппгбдлаичъжипьлдтьгдщужцьсгдлпсвднюбушгакфжьжфпепъжвпчртъфляншжепъгщпъртбркдцлндшъгэцрккфрдчфллчшшвдушлгтфгялеичырньщжндъхгыцукясолчцчжачцмбоъжырлпъчнмжигжвсроакхмвтыфтуллупцсвпчэшдхмгпыздфжздмшнжчымщуфмиьнюзтхжхолжжьыюбулдямэччичюыьмгещрвзылабихюдшъгыпхггцежяцьгжпыудыкажпцггкцжвцрзчслидъжхичшлчышкгпнпьылзяшъжзцуичъжэгтбгъччгяхрьещшрямъсзкхмацшльшъгыъьющфкьзпмгакфмгтцмъььичсурушшвьщрауицудыкпыщэбдтырдщшлтарцки"

class BukvaAndChastota():
    bukva = ""
    chastota = 0

    def __init__(self, bukva):
        self.bukva = bukva
        self.chastota = 0

def findFreq(chastotaInStroka:list[BukvaAndChastota], stroka):
    for i in range(len(chastotaInStroka)):
        for j in range(len(stroka)):
            if stroka[j] == chastotaInStroka[i].bukva:
                chastotaInStroka[i].chastota += 1
    return None

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

def sdvig(text:str, dict:str):
    res = ""
    for i in range(len(text)):
        # if text[i] == dict[0]:
        #     res+=dict[len(dict) - 1]
        if text[i] == dict[len(dict) - 1]:
            res+=dict[0]
        else:
            res+=dict[dict.index(text[i]) + 1]
    return res

#считает наиболее встречающееся значение в массиве
def counter(arr:list):
    count = {}
    for each in arr:
        if each in count:
            count[each] += 1
        else:
            count[each] = 1
    return list(count.items())[0][0]

def lengthOfKey(text):
    text1 = oneRegistr(text)
    dict = alphabet(text1)
    dictRusUp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dictEngUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Ic = 0
    if dict == dictRusUp:
        Ic = 0.0553
    else:
        Ic = 0.0644
    text2 = ""
    for i in text1:
        if i in dict:
            text2+=i

    L = len(text2)
    arrSdvigiT = []
    for t in range(1, 201):
        matches = 0
        for i in range(1, L - t):
            if text2[i] == text2[i + t]:
                matches += 1
        if (matches / (L - t)) > Ic:
            arrSdvigiT.append(t)
    #print(arrSdvigiT)

    distance = []
    for i in range(1, len(arrSdvigiT)):
        distance.append(abs(arrSdvigiT[i] - arrSdvigiT[i - 1]))
    #print(distance)
    averageDistance = counter(distance)
    #print(averageDistance)

    return averageDistance

def x2(shifrotext:str, dict:str):
    dictRusUp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dictEngUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    freqObrRus = [0.062,0.014,0.038,0.013,0.025,0.072,0.0001,0.007,0.016,0.062,0.01,0.028,0.035,0.026,0.053,
            0.09,0.023,0.04,0.045,0.053,0.021,0.002,0.009,0.004,0.012,0.006,0.003,0.0004,0.016,0.014,0.003,0.006,0.018]
    freqObrEng = [0.081,0.016,0.032,0.036,0.123,0.023,0.016,0.051,0.071,0.001,0.005,0.04,0.022,0.072,
            0.079,0.023,0.002,0.06,0.066,0.096,0.031,0.009,0.02,0.002,0.019,0.001]
    if dict == dictRusUp:
        freq = freqObrRus
    else:
        freq = freqObrEng
    bukvaArray = []
    for i in dict:
        bukvaArray.append(BukvaAndChastota(i))

    # for i in range(len(bukvaArray)):
    #     print(bukvaArray[i].bukva, bukvaArray[i].chastota, end = ' ')
    # print('\n')
    findFreq(bukvaArray, shifrotext)
    # for i in range(len(bukvaArray)):
    #     print(bukvaArray[i].bukva, bukvaArray[i].chastota, end = ' ')

    x2 = 0
    for i in range(len(dict)):
        if bukvaArray[i].chastota != 0:
            x2+=pow((bukvaArray[i].chastota / len(shifrotext) - freq[i]), 2) / (freq[i])
    return x2

#индекс минимального элемента массива
def minIndexInArr(arr:list):
    min = 9999999999999
    index = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            index = i
    return index

def autocorrelationMethod(text, lengthOfKey):
    text1 = oneRegistr(text)
    dict = alphabet(text1)
    dictRusUp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dictEngUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Ic = 0
    if dict == dictRusUp:
        Ic = 0.0553
    else:
        Ic = 0.0644
    text2 = ""
    for i in text1:
        if i in dict:
            text2 += i

    mtx = []
    for k in range(lengthOfKey):
        mtx.append("")
    for char in range(len(text2)):
        mtx[char % lengthOfKey] += text2[char]
    #print(mtx)

    x2Arr = []
    for i in mtx:
        tmp = []
        for j in range(len(dict)):
            tmp.append(x2(i, dict))
            i = sdvig(i, dict)
        x2Arr.append(tmp)
    #print('x2Arr', x2Arr)
    minX2 = []
    key = []
    for i in x2Arr:
        key.append(minIndexInArr(i))
    #print(key)

    # for i in x2Arr:
    #     print(i)

    # print(minX2)
    # minX2Res = []
    # for i in minX2:
    #     minX2Res.append(i % len(dict))
    # print(minX2Res)

    keyText = ""
    for i in range(len(key)):
        keyText+=dict[key[i]]
    #print(keyText)

    return keyText

# lengthOfKey(text)
# autocorrelationMethod(text, lengthOfKey(text))