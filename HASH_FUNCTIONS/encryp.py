import sys
from sha1 import sha1
from sha256 import generate_hash
from md4 import MD4
from md5 import MD5

def bytesToString(bytes):
    return bytes.decode("utf-8") 


def main():
    if len(sys.argv) > 1:
        messages = [msg.encode() for msg in sys.argv[1:]]
        for message in messages:
            print(message, "-> Que cifrado eliges:\n(1) MD4\n(2) MD5\n(3) SHA256\n(4) SHA1\n(0) Salir")
            opc = int(input("Opc: "))
            match opc:
                case 1:
                    print("MD4(\"",bytesToString(message),"\") -> ", MD4(message).hexdigest(), sep="")
                case 2:
                    toString = bytesToString(message)
                    print("MD5(\"",bytesToString(message),"\") -> ", MD5.hash(toString), sep="")
                case 3:
                    print("SHA256(\"",bytesToString(message),"\") -> ", generate_hash(message).hex(), sep="")
                case 4:
                    print("SHA1(\"",bytesToString(message),"\") -> ", sha1(message), sep="")
                case 0:
                    break
            print("\n")
    else:
        print("Put some msg to encrypt with MD4")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
