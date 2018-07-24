

alphaRot = int(input('Enter a integer for ceasar cypher: '))
sentence = str(input('Enter cleartext to be encyphered: '))
cypherText = ""
words = []


for line in sentence:  
    for ch in line:	
        if (ord(ch) > 96 and ord(ch) < 123):
            cypherText = cypherText + chr( ( (ord(ch)+alphaRot - 97) % 26 ) + 97 )
        elif (ord(ch) > 64 and ord(ch) < 91):
            cypherText = cypherText + chr( ( (ord(ch)+alphaRot - 65) % 26) + 65 )
        else:
            cypherText = cypherText + ch
            
            #print( "character " + ch + " could not be read" )
words = str.split(cypherText)
x = 0
y = 0

diff = []

for y in range(len(words) ):

    diff.append("")
    for x in range( len(words[y])):
        ##print("x : " + str(x) + ", y : " + str(y) + ", letter : ", words[y][x])
        diff[y] += (str(ord(words[y][x]) - ord(words[y][0])))
        
