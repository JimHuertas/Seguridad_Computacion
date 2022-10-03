
#Sustituye: si es minuscula lo pasa a mayuscula - en un texto de entrada
def todo_mayuscula(line):
    line = list(line)
    cont = 0
    for i in line:
        if(ord(i)>= 97 and ord(i)<=122):
            #print(line[cont], end=' - ')
            line[cont] = chr(ord(i)-32)
        cont=cont+1
    line = ''.join(line)
    return line
        