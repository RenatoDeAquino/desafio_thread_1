from threading import Thread
import time
import random
beatriz = []
for z in range (0,20):
    ajuda = random.randint(65,90)
    beatriz.append(chr(ajuda))
print("lista fora de ordem: " , beatriz)

def Vogal(lista1):
    
    vogal = 0
    for x in range(0,len(lista1)):
        if lista1[x] in 'AEIOU':
            vogal += 1
            time.sleep(0.1)
            print("processando a contagem de vogal...")
            time.sleep(0.1)
    return print("o numero de vogais é: "+ str(vogal))
def Consoante(lista2):
    conso =['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    consoante = 0
    for y in range(0,len(lista2)):
        if lista2[y] in conso:
            consoante += 1
            time.sleep(0.1)
            print("processando a consoante...")
            time.sleep(0.1)
    return print("o numero de consoantes foi: " + str(consoante))
def sorte(lista3):
    sono = []
    for x in range(0,len(lista3)):
        sono.append(ord(lista3[x]))
    for y in range(0,len(sono)):
        for z in range(y,len(sono)):
            if sono[y] > sono[z]:
                ajuda = sono[y]
                sono[y] = sono[z]
                sono[z] = ajuda
                time.sleep(0.1)
                print("processando a ordenacao...")
    lista3 = []
    for x in range(0,len(sono)):
        lista3.append(chr(sono[x]))
    print(lista3)
    

vogal1 = Thread(target=Vogal,args=[beatriz])
consoante1 = Thread(target=Consoante,args=[beatriz])
sort1 = Thread(target=sorte,args=[beatriz])

vogal1.start()
consoante1.start()
sort1.start()
