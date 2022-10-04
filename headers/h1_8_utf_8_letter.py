
def letterAgain(file):
    text = open(file, "r")
    text = text.readline()
    text = list(text)
    #print(text)
    for i in range(0, len(text)):
        if(text[i]==0,1,2,3,4,5,6,7,8,9):
            text[i]=chr(ord(text[i])+17)
    text=''.join(text)
    return text
