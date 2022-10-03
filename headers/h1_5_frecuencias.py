
frec_poema = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0,
    'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 
    'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 
    'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0,
    'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 
    'Z': 0,
}

def frecuencias(file):
    with open(file, 'r') as poema_pre:
        lines = poema_pre.readlines()
        for i in lines:
            line = list(i)
            for j in line:
                frec_poema[j] += 1
        poema_pre.close      
    frec_poema_sorted = sorted(frec_poema.items(), key=lambda x: x[1], reverse=True)


    return frec_poema_sorted