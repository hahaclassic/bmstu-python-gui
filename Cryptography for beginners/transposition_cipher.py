import math, random

def encryptMessage(key, message):
    translated = ['']*key
    for column in range(key):
        index=column
        while index < len(message):
            translated[column]+=message[index]
            index+=key
    return ''.join(translated)

def decryptMessage(key, message):
    numOfColumns = int(math.ceil(len(message)/float(key)))
    numOfRows=key
    numOfShadedBoxes=(numOfColumns*numOfRows)-len(message)
    plaintext=['']*numOfColumns

    column= 0
    row=0

    for symbol in message:
        plaintext[column]+=symbol
        column+=1
        if (column == numOfColumns)or(column==numOfColumns-1 and row>=numOfRows-numOfShadedBoxes):
            column=0
            row+=1

    return ''.join(plaintext)

def transposition(key, message, mode):
    if mode=='encrypt':
        translated=encryptMessage(key, message)
    if mode == 'decrypt':
        translated=decryptMessage(key, message)
        
    return translated

def getRandomKey_2(text):
    return random.randint(2, len(text)//2)

