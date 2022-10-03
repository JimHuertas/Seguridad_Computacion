
#Sustituye: jxi, hxi, ñxn, uxv, wxv, yxz, xxr (tanto mayusculas como minusculas)  de un texto de entrada
def substitutions(line):
    line = list(line)
    cont = 0
    for i in line:
        match i:
            case 'j':
                line[cont] = 'i'
            case 'h':
                line[cont] = 'i'
            case '\xf1':
                line[cont] = 'n'
            case 'k':
                line[cont] = 'l'
            case 'u':
                line[cont] = 'v'
            case 'w':
                line[cont] = 'v'
            case 'y':
                line[cont] = 'z'
            case 'x':
                line[cont] = 'r'
            case 'J':
                line[cont] = 'I'
            case 'H':
                line[cont] = 'I'
            case '\xd1':
                line[cont] = 'N'
            case 'K':
                line[cont] = 'L'
            case 'U':
                line[cont] = 'V'
            case 'W':
                line[cont] = 'V'
            case 'Y':
                line[cont] = 'Z'
            case 'X':
                line[cont] = 'R'
        cont=cont+1
    line = ''.join(line)
    return line
        