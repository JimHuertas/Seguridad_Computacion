
def mani(file):
    text = open(file, "r")
    text = text.readline()
    text = list(text)
    #print(text)
    cont=1
    for i in range(0, len(text)):
        if(i%20==0 and i != 0):
            text.insert(i*cont, 'MANI')
            cont=cont+1
    text = ''.join(text)
    return text