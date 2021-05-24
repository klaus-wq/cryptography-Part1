# -*- coding: utf-8 -*-
#text = "СЪСШ ЩГЖИСЮБЩЫРО ФЧ РЛЫОУУПЦЛЫ ЦЙУБЭЫФСЮДЯ ЛКЧААЮЦЩДХИЯ Б ХЙЕУЖ ШЩ ЧЙХК ЯПУЩА УОРЧЙ ЧЬЩ ЬЙЬЩУЙЙЧ Е ПЛЖЮС ЧАХОИ ЩЦ ЛЩДФСНБЮСЛ Щ ЙККЦЖЦЛЩ ЭЙСНШТ ЩЧЫОВХЮДИ ЗЗН ЛЪЯД ЛЕЖОН ЕЮЧЪЛМСРТЖЦЬВЖ ЛГСЗЙЬЧШ НФЧЗ ЧЮАЮЕ ЛЖЙКУАХЙНАИЕЬВ ЙЦЛ ККФЩУЮИЙЧ З ЬЦСЙВГЫХ СОЗЖЪНШШО ЛЪЯД ЦСЗНКЕШЛГЫХ ЦЩЗШО ЦСПЛЛТП С ЧАХЙВЩ ЮЙЦСЗХФС КЗСАХЦЩ СЙФФЗШО ЛЪЯД РЛЬНГЫХЪЖ ДПХЛЕЗ НФЧГХЛ ШЙ ШУЩ ЮОЕЛХЧУЛУ ЩКЯЙЛЩНКЫЭА ЕЧРЮЗЫГЧЖФЖ ЩЦ ЧРШЙЛЩМ ДЛВОЖЫРО КЙЯЛЫОЖЧЖФПШЙЪНХ ХЙЕЩЖ СЪСШ СЬЛРНГ ШПРТЗПЗН ЧЕЧУЦЖЪЕЩУС РЫСОНШЙ ЩЩТЖЛТЕЗ СЪСПХЛ СПРЬЛЕСЧШЙЪНХЩ ЪЙУЖЫЬЛ ЯЧВАЕЧИ ЩРЩТ ОЕФЖЫХЪЖ ДХЩЩЩХОВХЮДФ ЩРЩТ Щ ЗМУВ ЫЩГЕПЫЛЖПЯЛЩ Е ШУБЭЫЛЯЖ ЛЩДФСНБЮСЖ ШПБВЩ КЛЩА УОРЧЙ С ЛЪЯД Р ЮЯЙЭЩИЙЯЩ ЭЧНЛЯДФ ДЙРЧБЩЫРО ЫФЖ НЖЫФМ ЕРУЛКФТЕЗ У ЬЩУ ЧНШЙЪЖЧКИ ЧЩЫЙЕЧЗАФДЭСФ ЮЙНЭЩСЦТА З СЪСШ РГФПЛТ З ЙЪЬЛЕО ЛР ИОСЩХ АФЧЭЧ ЩЮЯОЧАИОЬШЙО ЦСЙМУБУХЬЛЖ ЪЩНЖЩСБЮСФ НЗНГЯХСЮАКУЛА ЬЙЧБМС Л ГЖФФШПШУБЕФФШЮЧФ ЛЪЬЮАЮСФ НИИ ДЛЯЧЫЛ ЙЩЪБЮСОЛЕЙЬШЙТ СЩЬЦЛ НЖЫФМ Е НФЧКУЩЕ КЙЧК ЮОЩФЦЧЧЩУЧ УБЬЦЩЛЪЩГЖЗО ЛЪЯ ЫГЯ ЭЙЕ ЧЙФПЯЙ ШУЩ ОЫЛР АЪВЛЕСЖР ЪЬЧАХ ЧААКШФЦЖЦГ НЖЫЖЕ ЕЧОЕЙПЬЛКЫП ЩЮЫФСЖЪЬЛТ С РЛЫОУУПЫФТГЦЩМ ЫОЖЧЖФПШЙЪНЩ УЦЩЪЙЧАСПРЛА ХСЦЛЕ ЛЛНЙЛ ЗЛЯХ ЛЪЯ ЦФЩЬКФУЮЧ ЕБЭ ЦФЩЬКФУЮЧ ЯШЙМЩЛЪЩГЖЗО СЩЬЦЛ ЯЙЫЩСАЗ ЩШЗ ЧНСППГЫХ УГЯ ЮОЛЖЪОСШЙ ХЬЛРЧЩФЯЙОЩЖ ЦФДУЧНСД ЦГ ЗЮОЫШЩЗ РРЙПФДХЕ ЛЪЯ ЧЧШЙМЩ ЧЗШГ ЕЙНФТЗ"
text = "влцдутжбюцхъяррмшбрхцэооэцгбрьцмйфктъъюьмшэсяцпунуящэйтаьэдкцибр ьцгбрпачкъуцпъбьсэгкцъгуущарцёэвърюуоюэкааэбрняфукабъарпяъафкъиьжяффнйо яфывбнэнфуюгбрьсшьжэтбэёчюъюръегофкбьчябашвёэуъъюаднчжчужцёэвлрнчулб юпцуруньъшсэюъзкцхъяррнрювяспэмасчкпэужьжыатуфуярюравртубурьпэщлафоуф бюацмнубсюкйтаьэдйюнооэгюожбгкбрънцэпотчмёодзцвбцшщвщепчдчдръюьскасэг ъппэгюкдойрсрэвоопчщшоказръббнэугнялёкьсрбёуыэбдэулбюасшоуэтъшкрсдугэфл бубуъчнчтртпэгюкиугюэмэгюккъъпэгяапуфуэзьрадзьжчюрмфцхраююанчёчюъыхьъ цомэфъцпоирькнщпэтэузуябащущбаыэйчдфрпэцъьрьцъцпоилуфэдцойэдятррачкубу фнйтаьэдкцкрннцюабугюуубурьпйюэъжтгюркующоъуфъэгясуоичщщчдцсфырэдщэ ъуяфшёчцюйрщвяхвмкршрпгюопэуцчйтаьэдкцибрьцыяжтюрбуэтэбдуящэубъибрюв ъежагибрбагбрымпуноцшяжцечкфодщоъчжшйуъцхчщвуэбдлдъэгясуахзцэбдэулькнъ щбжяцэьрёдъьвювлрнуяфуоухфекьгцчччгэъжтанопчынажпачкъуъмэнкйрэфщэъьбуд эндадъярьеюэлэтчоубъцэфэвлнёэгфдсэвэёкбсчоукгаутэыпуббцчкпэгючсаъбэнэфърк ацхёваетуфяепьрювържадфёжбьфутощоявьъгупчршуитеачйчирамчюфчоуяюонкяжы кгсцбрясшчйотъъжрсщчл"

class SubstrAndInd():
    substring = ""
    indexes = []
    distance = 0

    def __init__(self, substring):
        self.substring = substring
        self.indexes = []
        self.distance = 0

#приводим к одному регистру
def oneRegistr(text):
    dictRusUp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЫЭЮЯ"
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
    print(text)
    return text

#какой алфавит
def alphabet(text):
    dictRus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЫЭЮЯ"
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

def objInArr(obj:SubstrAndInd, arr:list[SubstrAndInd]):
    for i in arr:
        if obj.substring == i.substring:
            return False
    return True

def searchCombinations(text:str, count:int):
    arrOfInd = []
    for i in range(int(len(text)/count)):
            obj = SubstrAndInd(text[i:i + count])
            #arrOfInd.append(obj)
            obj.indexes.append(i)
            for k in range(i + count, len(text) - count):
                if text[i:i + count] == text[k:k + count]:
                    obj.indexes.append(k)
            if len(obj.indexes) > 3 and objInArr(obj, arrOfInd):
                arrOfInd.append(obj)
    return arrOfInd

def gcd(a:int, b:int):
    while (b):
        t = b
        b = a % b
        a = t
    return a

def lengthOfKey(text):
    dict = alphabet(text)
    text2 = oneRegistr(text)
    text1 = ""
    for i in text2:
        if i in dict:
            text1+=i
    arrOfInd = searchCombinations(text1, 3)
    for i in range(len(arrOfInd)):
        print(arrOfInd[i].substring, arrOfInd[i].indexes)

    for i in range(len(arrOfInd)):
        if len(arrOfInd[i].indexes) > 3: #3 - число вхождений
            rasst = []
            for j in range(1, len(arrOfInd[i].indexes) - 1):
                rasst.append(abs(arrOfInd[i].indexes[j - 1] - arrOfInd[i].indexes[j]))
                nod = rasst[0]
                for k in range(len(rasst)):
                    nod = gcd(nod, rasst[k])
                arrOfInd[i].distance = nod

    for i in range(len(arrOfInd)):
        if arrOfInd[i].distance != 0:
            print((arrOfInd[i].substring, arrOfInd[i].indexes, arrOfInd[i].distance))

    lengthOfKey = 1
    nod = []
    for i in range(len(arrOfInd)):
        if arrOfInd[i].distance != 0:
            nod.append(arrOfInd[i].distance)
            lengthOfKey = nod[0]
            for j in range(len(nod)):
                lengthOfKey = gcd(lengthOfKey, nod[j])
    print(lengthOfKey)

    return lengthOfKey

def casiski(text, lengthOfKey):
    dict = alphabet(text)
    dictFreq = ""
    dictEngFreq = "ETAOINSHRDLCUMWFGYPBVKXJQZ"
    dictRusFreq = "ОЕАИНТСРВЛКМДПУЯЫЬГЗБЧЙХЖШЮЦЩЭФЪЁ"
    dictRus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЫЭЮЯ"
    dictEng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if dict == dictRus:
        dictFreq = dictRusFreq
    else:
        dictFreq = dictEngFreq
    text2 = oneRegistr(text)
    text1 = ""
    for i in text2:
        if i in dict:
            text1+=i

    mtx = []
    for k in range(lengthOfKey):
        mtx.append("")
    for char in range(len(text1)):
        mtx[char % lengthOfKey] += text1[char]
    print(mtx)

    popularSymb = []
    for i in range(len(mtx)):
        bukva = ""
        cifra = 0
        for k in dict:
            if mtx[i].count(k)>cifra:
                bukva = k
                cifra = mtx[i].count(k)
        popularSymb.append(bukva)
    print(popularSymb)
    key = ""
    for i in range(len(popularSymb)):
        if dict == dictRus:
            key += dict[abs(dict.index(popularSymb[i]) - dict.index('О'))]
        else:
            key += dict[abs(dict.index(popularSymb[i]) - dict.index('E'))]
    print(key)

    return key

# lengthOfKey(text)
# casiski(text, lengthOfKey(text))