import random
def alphabet(eng_rus):
    if eng_rus==True:
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        return 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def encryptMessage(key, message, eng_rus):
    return translateMessage(key, message, 'encrypt', eng_rus)

def decryptMessage(key, message, eng_rus):
    return translateMessage(key, message, 'decrypt', eng_rus)

def translateMessage(key, message, mode, eng_rus):
    translated=[]
    keyIndex=0
    key=key.upper()
    LETTERS=alphabet(eng_rus)
    
    for symbol in message:
        num=LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num+=LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num-= LETTERS.find(key[keyIndex])
            num%= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS [num].lower())
            
            keyIndex += 1       
            if keyIndex == len(key):
                keyIndex=0 
        else:
            translated.append(symbol)
    return ''.join(translated)

def vigenere_cipher(key, message, mode, eng_rus):

    if mode=='encrypt':
        translated = encryptMessage(key, message, eng_rus)
    elif mode=="decrypt":
        translated=decryptMessage(key, message, eng_rus)

    return translated


with open('dictionary.txt', 'r') as f:
    a=list(map(str, f.readlines()))
with open('russian_dictionary.txt', 'r', encoding='utf-8') as s:
    b=list(map(str, s.readlines()))

def getRandomKey_3(eng_rus):
    if eng_rus:
        t=random.choice(a).split()
    else:
        t=random.choice(b).split()
    key=str(t[0])
    return ''.join(key)