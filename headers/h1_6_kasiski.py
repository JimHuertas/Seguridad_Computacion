import re

NONLETTERS_PATTERN = re.compile('[^A-Z]')
MAX_KEY_LENGTH = 16 # will not attempt keys longer than this


def dec_to_hex(num):
    txt = hex(num)
    txt = list(txt)
    txt.reverse()
    txt.pop()
    txt.pop()
    txt.reverse()
    txt = ''.join(txt)
    txt = txt.upper()
    return txt


def findRepeatSequencesSpacings(message):
    message = ''.join(message)
    message = NONLETTERS_PATTERN.sub('', message.upper())
    seqSpacings = {} # keys are sequences, values are list of int spacings
    for seqLen in range(3, 6):
        for seqStart in range(len(message) - seqLen):
            seq = message[seqStart:seqStart + seqLen]
            for i in range(seqStart + seqLen, len(message) - seqLen):
                if message[i:i + seqLen] == seq:
                    if seq not in seqSpacings:
                        seqSpacings[seq] = [] # initialize blank list
                    seqSpacings[seq].append(i - seqStart)
    return seqSpacings

def getUsefulFactors(num):
    if num < 2:
        return [] # numbers less than 2 have no useful factors
    factors = [] # the list of factors found
    for i in range(2, MAX_KEY_LENGTH + 1): # don't test 1
        if num % i == 0:
            factors.append(i)
            factors.append(int(num / i))
    if 1 in factors:
        factors.remove(1)

    return list(set(factors))

def getItemAtIndexOne(x):
    return x[1]

def getMostCommonFactors(seqFactors):
    factorCounts = {} # key is a factor, value is how often if occurs
    for seq in seqFactors:
        factorList = seqFactors[seq]
        for factor in factorList:
            if factor not in factorCounts:
                factorCounts[factor] = 0
            factorCounts[factor] += 1
    factorsByCount = []

    for factor in factorCounts:
        if factor <= MAX_KEY_LENGTH:
            factorsByCount.append( (factor, factorCounts[factor]) )

    factorsByCount.sort(key=getItemAtIndexOne, reverse=True)

    return factorsByCount


def kasiskiExamination(txt):
    repeatedSeqSpacings = findRepeatSequencesSpacings(txt)
    seqFactors = {}
    for seq in repeatedSeqSpacings:
        seqFactors[seq] = []
        for spacing in repeatedSeqSpacings[seq]:
            seqFactors[seq].extend(getUsefulFactors(spacing))

    factorsByCount = getMostCommonFactors(seqFactors)
    allLikelyKeyLengths = []
    for twoIntTuple in factorsByCount:
        allLikelyKeyLengths.append(twoIntTuple[0])
    return allLikelyKeyLengths


def kasiski(file):
    text = open(file, "r")
    text = list(text)
    list_trigrama = kasiskiExamination(text)

    return list_trigrama
    