
#Sustituye: Elimina los espacios en blanco y los signos de puntuación de cada linea
def modifiers(line):
    result = list()
    line = list(line)
    cont = 0
    for i in line:
        if((ord(i)>= 65 and ord(i)<=90)):
            result.append(line[cont])
        cont=cont+1
    result = ''.join(result)
    return result
        