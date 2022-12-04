from headers.h1_6_kasiski import findRepeatSequencesSpacings
from headers.h2_1_cifrado_cesar import cifrado_cesar, decifrado_cesar
from headers.h2_2_cifrado_vignere import cifrado_vignere, decifrado_vignere
from headers.h2_3_cifrado_autoclave import cifrado_autoclave



if __name__ == "__main__":
    # Cifrado de Cesar
    # print("###########################")
    # print("##   CIFRADO DE CESAR    ##")
    # print("###########################")
    # b = int(input("Nro. de desplazamiento: "))
    # cifrado = cifrado_cesar(b, "INPUT.txt")
    # decifrado = decifrado_cesar(cifrado, b)
    # print("Cifrado:", cifrado)
    # print("Decifrado:",decifrado)

    # Cifrado de Vignere
    print("#############################")
    print("##   CIFRADO DE VIGNERE    ##")
    print("#############################")
    clave = input("Clave: ")
    # alfabeto = int(input("(1) mod 27\n(2) mod 191\nOpc: "))
    print(cifrado_vignere("INPUT.txt", clave, 1))


    # cifrado = "GYLKWQRVEBTPXDJRQDDVQNPHHGQGUWRNPPWHRGCONLJOHMÑCOXEEAVASIÑDOEQPETAPVHEOPEKRXYAEVRUHAÑVNRSIVPZBSXINLEWSMGBSHEEITVDEENSVR"
    # decifrado = decifrado_vignere(cifrado,"PEDRONAVAJA")
    # print(decifrado)

    # print("###############################")
    # print("##   CIFRADO DE AUTOCLAVE    ##")
    # print("###############################")
    # clave = input("Clave: ")
    # opc = int(input("(1) Cifrado\n(2) Descifrado\nOpc: "))
    # print(cifrado_autoclave("AUTOCLAVE.txt", clave, opc))


    # print("###############################")
    # print("##    CIFRADO DE KASISKI     ##")
    # print("###############################")

    # cadena = "LNUDVMUYRMUDVLLPXAFZUEFAIOVWVMUOVMUEVMUEZCUDVSYWCIVCFGUCUNYCGALLGRCYTIJTRNNPJQOPJEMZITYLIAYYKRYEFDUDCAMAVRMZEAMBLEXPJCCQIEHPJTYXVNMLAEZTIMUOFRUFC"
    # a = findRepeatSequencesSpacings(cadena)
    # print(a)