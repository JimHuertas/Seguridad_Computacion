map_abc27 = {
    'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 
    'J':9, 'K':10, 'L':11, 'M':12, 'N':13, '\u00d1':14, 'O':15, 'P':16, 
    'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 
    'Y':25, 'Z':26
}
map_num27 = {
    0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 
    9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'\u00d1', 15:'O', 16:'P', 
    17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X',
    25:'Y', 26:'Z'
}
map_tildes = ['á','é', 'í', 'ó','ú']

def isTilde(chr):
    for i in map_tildes:
        if(chr == i):
            return True
    return False

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def cifrado_cesar(b,M,n=27):
    cifrado = ""
    lines = list()
    with open(M) as txt:
        lines = txt.readlines()
        for line in lines:
            for i in line:
                if(i == '\n'):
                    continue
                elif(i == ' '):
                    continue
                elif(isTilde(i)):
                    i = normalize(i.upper())
                if(ord(i)>= 97 and 122>=ord(i) or i=='\xf1'):
                    nro_desplazamiento = (map_abc27[i.upper()]+b)%n
                    cifrado += map_num27[nro_desplazamiento]
                elif(ord(i)>= 65 and 90>=ord(i) or i=='\u00d1'):
                    nro_desplazamiento = (map_abc27[i]+b)%n
                    cifrado += map_num27[nro_desplazamiento]
                else:
                    continue 
        txt.close() 
    return cifrado

def decifrado_cesar(M,b,n=27):
    decifrado = ""
    for i in M:
        nro_desplazamiento = (map_abc27[i.upper()]-b)%n
        decifrado += map_num27[nro_desplazamiento]
    return decifrado