import random

def alphabet_1(eng_rus):
    if eng_rus==True:
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,'
    else:
        return 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890 !?.,'

def caesar_cipher_1(key, message, mode, eng_rus):
    
    SYMBOLS=alphabet_1(eng_rus)
    key=key%len(SYMBOLS)

    translated=''

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex=SYMBOLS.find(symbol)
            if mode=='encrypt':
                translatedIndex=symbolIndex+key
            elif mode=='decrypt':
                translatedIndex=symbolIndex-key
            if translatedIndex>=len(SYMBOLS):
                translatedIndex-=len(SYMBOLS)
            elif translatedIndex<0:
                translatedIndex+=len(SYMBOLS)
            translated+=SYMBOLS[translatedIndex]
        else:
            translated+=symbol
            
    return translated

def getRandomKey_1(eng_rus):
    LETTERS=alphabet_1(eng_rus)
    key = random.randint(1, len(LETTERS))
    return ''.join(str(key))