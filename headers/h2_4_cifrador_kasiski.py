import re

NONLETTERS_PATTERN = re.compile('[^A-Z]')
MAX_KEY_LENGTH = 16 # will not attempt keys longer than this

def findRepeatSequencesSpacings(message):
    message = ''.join(message)
    message = NONLETTERS_PATTERN.sub('', message.upper())
    seqSpacings = {} # keys are sequences, values are list of int spacings
    for seqLen in range(3, 6):
        for seqStart in range(len(message) - seqLen):
            seq = message[seqStart:seqStart + seqLen]
            
            for i in range(seqStart + seqLen, len(message) - seqLen):
                print(seq)
                if message[i:i + seqLen] == seq:
                    print(seq)
                    if seq not in seqSpacings:
                        seqSpacings[seq] = [] # initialize blank list
                    seqSpacings[seq].append(i - seqStart)
    return seqSpacings