import pyperclip, sys, random

def alphabet_4(eng_rus):
    if eng_rus==True:
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        return 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def keyIsValid(key, eng_rus):
    LETTERS=alphabet_4(eng_rus)
    keyList = list(key)
    letterList = list(LETTERS)
    keyList.sort()
    letterList.sort()

    return keyList == letterList

def encryptMessage(key, message, eng_rus):
    return translateMessage(key, message, 'encrypt', eng_rus)

def decryptMessage(key, message, eng_rus):
    return translateMessage(key, message, 'decrypt', eng_rus)

def translateMessage(key, message, mode, eng_rus):
    LETTERS=alphabet_4(eng_rus)
    translated = ''
    charsA = LETTERS
    charsB = key.upper()
    if mode == 'decrypt':
        charsA, charsB = charsB, charsA
    
    for symbol in message:
        if symbol in message:
            if symbol.upper() in charsA:
                symIndex = charsA.find(symbol.upper())
                if symbol.isupper():
                    translated += charsB[symIndex].upper()
                else:
                    translated += charsB[symIndex].lower()
            else:
                translated += symbol
    return translated

def simple_substitution_cipher_1(key, message, mode, eng_rus):
    if mode == 'encrypt':
        translated = encryptMessage(key, message, eng_rus)
    elif mode == 'decrypt':
        translated = decryptMessage(key, message, eng_rus)
    
    return translated


def getRandomKey_4(eng_rus):
    LETTERS=alphabet_4(eng_rus)
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

