
map_num27 = {
    0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 
    9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'\u00d1', 15:'O', 16:'P', 
    17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X',
    25:'Y', 26:'Z'
}

map_abc27 = {
    'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 
    'J':9, 'K':10, 'L':11, 'M':12, 'N':13, '\u00d1':14, 'O':15, 'P':16, 
    'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 
    'Y':25, 'Z':26
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

def autoclave(clave, line="", n=27):
    cifrado = ""
    clave = clave.upper()
    cont = 0
    for i in line:
        if(i == '\n'):
            continue
        elif(i == ' '):
            continue
        elif(isTilde(i)):
            i = normalize(i.upper())
        if(ord(i)>= 97 and 122>=ord(i) or i=='\xf1'):
            # print(i, "  ", i.upper(), " - ",clave[cont])
            actual = clave[cont % len(clave)]
            clave += i.upper()
            nro_desplazamiento = (map_abc27[i.upper()]+ map_abc27[actual])%n
            cifrado += map_num27[nro_desplazamiento]
            cont+=1
        elif(ord(i)>= 65 and 90>=ord(i) or i=='\u00d1'):
            # print(i, "  ", i.upper(), " - ",clave[cont])
            actual = clave[cont % len(clave)]
            clave += i.upper()
            nro_desplazamiento = (map_abc27[i]+ map_abc27[actual])%n
            cifrado += map_num27[nro_desplazamiento]
            cont+=1
        else:
            continue 
    return cifrado

def cifrado_autoclave(M, clave, opc):
    cifrado = ""
    lines = list()
    with open(M) as txt:
        lines = txt.readlines()
        for line in lines:
            if(opc == 1):
                cifrado += autoclave(clave, line)
            else:
                cifrado += decifrado_autoclave(clave, line)
        return cifrado

def decifrado_autoclave(clave, line="", n=27):
    cifrado = ""
    clave = clave.upper()
    cont = 0
    for i in line:
        if(i == '\n'):
            continue
        elif(i == ' '):
            continue
        elif(isTilde(i)):
            i = normalize(i.upper())
        if(ord(i)>= 97 and 122>=ord(i) or i=='\xf1'):
            # print(i, "  ", i.upper(), " - ",clave[cont])
            actual = clave[cont % len(clave)]
            nro_desplazamiento = (map_abc27[i.upper()]- map_abc27[actual])%n
            cifrado += map_num27[nro_desplazamiento]
            clave += map_num27[nro_desplazamiento]
            cont+=1
        elif(ord(i)>= 65 and 90>=ord(i) or i=='\u00d1'):
            # print(i, "  ", i.upper(), " - ",clave[cont])
            actual = clave[cont % len(clave)]
            nro_desplazamiento = (map_abc27[i]- map_abc27[actual])%n
            cifrado += map_num27[nro_desplazamiento]
            clave += map_num27[nro_desplazamiento]
            cont+=1
        else:
            continue 
    return cifrado