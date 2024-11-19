import sys
# Вы можете хотеть изменить переменные ниже, т.к. они являются важной частью достижения сохранности сообщения
BYTESHIFVALUE = 4
FACE = "NOFACE"
#Просто договоритесь с получателем об определенных настойках
def makeface(incode : bytes):
    chin = incode[len(incode)//2:]
    forehead = incode[:len(incode)//2]
    face = chin + forehead
    face = FACE.join(face[i:i+1] for i in range(0, len(face), 1)).encode("utf-8") 
    face = bin(int.from_bytes(face,byteorder=sys.byteorder) >> BYTESHIFVALUE) 
    face = (FACE * BYTESHIFVALUE) + face
    return face

def breakface(S, sub):
    i = 0
    while i < len(S):
        for e in sub:
            if S[i:].startswith(e):
                S = S[:i] + S[i+len(e):]
                i -= 1
                break
        else: i += 1
    return S

def deface(encoded : str):
    c = encoded.count(FACE)
    encoded = encoded[c*len(FACE):]
    en = int(encoded,2) << c
    enc = en.to_bytes(len(encoded),byteorder=sys.byteorder) 
    enco = enc.decode("utf-8") 
    encod = breakface(enco,FACE).split('\x00', 1)[0]
    if len(encod) % 2 != 0:
        chin = encod[(len(encod)//2)+1:]
        forehead = encod[:(len(encod)//2)+1]
    else:
        chin = encod[len(encod)//2:]
        forehead = encod[:len(encod)//2]
    face = chin + forehead
    print("Итог расшифровки : "+face)
    

if __name__ == "__main__":
    result = ''
    ch = input(" 1. Закодировать строку \n 2. Раскодировать строку \n 3. Моментальный тест \n >  ")
    if ch == "3":
        incode = input("Введите кодируемую строку : ").lower()
        face = makeface(incode)
        deface(face)
    if ch == "2":
        incode = input("Введите строку : ").lower()
        deface(incode)
    if ch == "1":
        incode = input("Введите кодируемую строку : ").lower()
        face = makeface(incode)
        print(face)