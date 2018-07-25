# Erik Skogfeldt
# 07-25-2018
alphaRot = int(input('Enter a integer for ceasar cypher: '))
sentence = str(input('Enter cleartext to be encyphered: '))
cypherText = ""
words = []


for line in sentence:
    for ch in line:
        if (ord(ch) > 96 and ord(ch) < 123):
            cypherText = cypherText + chr(((ord(ch)+alphaRot - 97) % 26) + 97)
        elif (ord(ch) > 64 and ord(ch) < 91):
            cypherText = cypherText + chr(((ord(ch)+alphaRot - 65) % 26) + 65)
        else:
            cypherText = cypherText + ch

words = str.split(cypherText)
