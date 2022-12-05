import hashlib

def bytesToString(bytes):
    return bytes.decode("utf-8") 

def MD4(text):
    hashObject = hashlib.new('md4', text)
    digest = hashObject.hexdigest()
    return digest

def MD5(text):
    result = hashlib.md5(text)
    return result.hexdigest()

def SHA256(text):
    hashed_string = hashlib.sha256(text).hexdigest()
    return hashed_string

def SHA1(text):
    hash_object = hashlib.sha1(text)
    pbHash = hash_object.hexdigest()
    return pbHash

def main():
    txt = input("Mensaje: ")
    txt = [msg.encode() for msg in list(txt.split(" "))]
    print("Algoritmos:\n(1) MD4\n(2) MD5\n(3) SHA256\n(4) SHA1\n(0) Salir")
    opc = int(input("Opc: "))
    match opc:
        case 1:
            for word in txt:
                print("MD4(\"",bytesToString(word),"\"): ", MD4(word), sep="")
        case 2:
            for word in txt:
                print("MD5(\"",bytesToString(word),"\"): ", MD5(word), sep="")
        case 3:
            for word in txt:
                print("SHA256(\"",bytesToString(word),"\"): ", SHA256(word), sep="")
        case 4:
            for word in txt:
                print("SHA1(\"",bytesToString(word),"\"): ", SHA1(word), sep="")
        case 0:
            print("Elige una opcion valida, SALIENDO...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
