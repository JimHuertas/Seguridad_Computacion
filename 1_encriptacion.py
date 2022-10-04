from headers.h1_1_substitutions import substitutions
from headers.h1_2_eliminar_tildes import sin_tilde
from headers.h1_3_todo_a_mayuscula import todo_mayuscula
from headers.h1_4_modifiers import modifiers
from headers.h1_5_frecuencias import frecuencias
from headers.h1_6_kasiski import kasiski, dec_to_hex
from headers.h1_7_unicode import unicode
from headers.h1_8_utf_8_letter import letterAgain
from headers.h1_9_mani import mani

#Dictionary


def main():
    lines = list()
    with open('POEMA.txt') as poema:
        lines = poema.readlines()
        cont=0
        for i in lines:
            lines[cont] = substitutions(i)
            cont=cont+1
        cont=0
        for i in lines:
            lines[cont] = sin_tilde(i)
            cont=cont+1
        cont=0
        for i in lines:
            lines[cont] = todo_mayuscula(i)
            cont=cont+1
        cont=0
        for i in lines:
            lines[cont] = modifiers(i)
            #print("Length: " ,len(lines[cont]), " - ",lines[cont], end="")
            cont=cont+1
        poema.close()


    #Open n Write POEMA_PRE.txt
    with open('POEMA_PRE.txt', 'w') as poema_pre:
        for i in lines:
            poema_pre.write('%s' % i)
        poema_pre.close
    
    poema_dictionary = frecuencias('POEMA_PRE.txt')
    #print(poema_dictionary)
    keys = kasiski('POEMA_PRE.txt')
    #print(keys)

def post_encriptacion():
    text = unicode("POEMA_PRE.txt")
    with open('POEMA_PRE.txt', 'w') as poema_pre:
        poema_pre.write('%s' % text)
        poema_pre.close

    text = letterAgain("POEMA_PRE.txt")
    with open('POEMA_PRE.txt', 'w') as poema_pre:
        poema_pre.write('%s' % text)
        poema_pre.close

    text = mani('POEMA_PRE.txt')
    with open('POEMA_PRE.txt', 'w') as poema_pre:
        poema_pre.write('%s' % text)
        poema_pre.close

main()
post_encriptacion()
