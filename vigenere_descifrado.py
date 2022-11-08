import re
import helpers.descifrado_sin_clave as VIG
import helpers.descifrado_con_clave as VIG2


if __name__ == "__main__":
    with open("CIFRADO.txt") as txt:
        line = txt.readline()
        print("Cifrado: \n", line, '\n')
        key = input("Clave: ")
        new_ = VIG2.decipher(line, key)
        print("\nDescifrado: \n",new_)
        
        # print("\nSin Clave:")
        # decrip = VIG.analyze("es", line)
        # print("\nSin Clave:\n",decrip, '\n')
        

        # decipherDict = VIG.findPossibleKeys("es", line, 5)
        # print(decipherDict, '\n')

        # xd = VIG.analysePercentage("es", line)
        # print(xd, '\n')

        # med = VIG.analyseMatchScore("es", xd)
        # print(med)
        # print("(1) Decifrado con clave\n(2) Descifrado sin clave\n(0)Salir")
        # opc = int(input("Opc: "))
        # while(True):
        #     if(opc == 1):
        #         key = input("Key: ")
        #         vignere.decipher(line, key)
        #     elif(opc == 2):
        #         VIG.freqanalysis("en", line)
        #         VIG.ic("en", line)
        #     elif(opc==0):
        #         break
        #     else:
        #         print("Elige opcion valida")