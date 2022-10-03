
#Sustituye: remueve todas las tildes (tanto mayusculas como minusculas)  de un texto de entrada
def sin_tilde(line):
    line = list(line)
    cont = 0
    for i in line:
        match i:
            case '\xe1':
                line[cont] = 'a'
            case '\xe9':
                line[cont] = 'e'
            case '\xed':
                line[cont] = 'i'
            case '\xf3':
                line[cont] = 'o'
            case '\xfa':
                line[cont] = 'u'
            case '\xc1':
                line[cont] = 'A'
            case '\xc9':
                line[cont] = 'E'
            case '\xcd':
                line[cont] = 'I'
            case '\xd3':
                line[cont] = 'O'
            case '\xda':
                line[cont] = 'U'
        cont=cont+1
    line = ''.join(line)
    return line
        