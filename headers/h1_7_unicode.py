
from headers.h1_6_kasiski import dec_to_hex


def unicode(file):
    text = open(file, "r")
    text = text.readline()
    text = list(text)
    #print(text)
    for i in range(0, len(text)):
        text[i] = dec_to_hex(ord(text[i]))
    text = ''.join(text)

    return text
