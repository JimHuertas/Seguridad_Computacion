import itertools
import json

def pick_alphabet(lang):
    alphabet = []
    if lang == 'es':
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    if lang == 'en':
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    return alphabet

def pick_frequent(lang):
    if lang == "es":
        freqLetters = ["E","A","O","S","N","R","I","L","D","U","T","C","M","P","Q","Y","B","H","V","G","J","F","Z","Ñ","K","W","X"]
    else:
        freqLetters = ["E","T","A","O","I","N","S","H","R","D","L","C","U","M","W","F","G","Y","P","B","V","K","J","X","Q","Z"]
    return freqLetters

def analysePercentage(lang, word):
    alphabet = pick_alphabet(lang)
    freqdict = {}
    total = 0
    for i in alphabet:
        freqdict[i] = 0
    for i in word:
        if i.isalpha():
            freqdict[i] += 1
            total += 1
    for k in freqdict:
        freqdict[k] = round((freqdict[k]/total)*100,2)
    freqdict = dict(sorted(freqdict.items(), key=lambda item: item[1],reverse=True))
    return freqdict


def analyseMatchScore(lang,freqdict):
    alphabet = pick_frequent(lang)
    matchScoreQuarts = len(alphabet)//4
    mostFreqAlphabet = list(itertools.islice(alphabet,matchScoreQuarts))
    leastFreqAlphabet = list(itertools.islice(reversed(alphabet),matchScoreQuarts))
    mostFreqWord = list(itertools.islice(list(freqdict),matchScoreQuarts))
    leastFreqWord = list(itertools.islice(reversed(list(freqdict)),matchScoreQuarts))
    matchScore = 0
    maxMatchScore = 2*matchScoreQuarts
    for i in mostFreqWord:
        if i in mostFreqAlphabet:
            matchScore += 1
    for i in leastFreqWord:
        if i in leastFreqAlphabet:
            matchScore += 1
    return round(matchScore/maxMatchScore,2)

def DetectLanguage(lang, word):
    return 0.9

def findIC(lang,word):
    alphabet = pick_alphabet(lang)
    N = len(word)
    denominator = N*(N-1)
    freqdict = {}
    for i in alphabet:
        freqdict[i] = 0
    for i in word:
        if i.isalpha():
            freqdict[i] += 1
    for i in freqdict:
        freqdict[i] *= freqdict[i]-1
    ic = round(sum(freqdict.values())/denominator,4)
    return ic

def analyze(lang,word):
    alphabet = pick_alphabet(lang)
    k = len(alphabet)//2
    rotatedWord = word
    icdict = {}
    for i in range (1,k+1):
        icdict[i] = 0
        rotatedWord = rotatedWord[1:] + rotatedWord[:1]
        print(rotatedWord, " - ", i)
        count = 0
        for j in range(len(word)):
            if rotatedWord[j] == word[j]:
                count += 1
        icdict[i] = round(count/len(word),4)
    icdict = dict(sorted(icdict.items(), key=lambda item: item[1],reverse=True))
    return icdict

def decryption(lang, word="", key=""):
    alphabet  = pick_alphabet(lang)
    output = []
    N = len(alphabet)
    key_num = 0
    word = word.upper()
    key = key.upper()
    for i in word:
        if i.isalpha():
            Ci = alphabet.index(i)
            Ki = alphabet.index(key[key_num])
            key_num += 1
            if key_num == len(key):
                key_num = 0
            output.append(alphabet[(Ci + N - Ki) % N])
        else:
            output.append(i)
    output = ''.join(output)
    return output

def hack(lang,word):
    potentialLetters = {}
    alphabet = pick_alphabet(lang)
    for i in alphabet:
        bruteDecrypt = decryption(lang,word,i)
        matchScore = analyseMatchScore(lang,analysePercentage(lang,bruteDecrypt))
        potentialLetters[i] = matchScore
    potentialLetters = sorted(potentialLetters, key=potentialLetters.get, reverse=True)[:3]  # type: ignore
    return potentialLetters

def findPossibleKeys(lang,word,keylen):
    word = ''.join(word.strip().split())
    word = list(map(''.join,zip(*[iter(word)]*keylen)))
    decipherDict = {}
    for i in range(0,keylen):
        cachelist = ''.join([letter[i] for letter in word])
        decipherDict[i] = 0
        decipherDict[i] = hack(lang,cachelist)
    return decipherDict

def finalProcessing(lang,decipherDict,word,keylen):
    for indexes in itertools.product(range(3),repeat=keylen):
        key = ''
        for i in range(keylen):
            key += decipherDict[i][indexes[i]][0]
        decryption_ = decryption(lang,word,key)
        score = DetectLanguage(lang,decryption_)
        if score > 0.8:
            choice = 0
            print("Key:", key, ", descodificación: ", decryption_)
            print("Continuar con otros? (y/n)")
            choice = input()
            while choice != "y" and choice != "n":
                print("(y/n)")
                choice = input()
            if choice == "n":
                return key

def freqanalysis(lang,word):
    word = ''.join(filter(str.isalpha, word))
    percentage = analysePercentage(lang, word)
    percentage = json.dumps(percentage)
    print("Resultado en .JSON:",percentage)

def vigeneredecrypt(lang,word,key):
    result = decryption(lang,word,key)
    print(result)
    choice = ''
    while not (choice == "y" or choice == "n"):
        choice = input("escribir en el archivo? (y/n) >")
    if choice == 'y':
        with open('out.txt','w') as f:
            f.write(result)
        print("El resultado se va a escribir en un archivo -> out.txt")

def decipher(lang,word):
    word = ''.join(filter(str.isalpha, word))
    possibleKeys = analyze(lang,word)
    print("Posibles longitudes de clave detectadas:", *possibleKeys, sep=', ')
    keylen = int(input("Introduzca la longitud de la clave: "))
    decipherDict = findPossibleKeys(lang, word, keylen)
    key = finalProcessing(lang, decipherDict, word, keylen)
    print("Key:",key)
    choice = ''
    while not (choice == "y" or choice == "n"):
        choice = input("Descifrar con la clave recibida? (y/n) >")
    if choice == "y":
       vigeneredecrypt(lang,word,key)
