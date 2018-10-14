import random
def oppgave():
    nedre_grense = int(input('Velg nedre grense: '))
    ovre_grense = int(input('Velg øvre grense: '))
    tall = random.randint(nedre_grense, ovre_grense)
    gjett = int(input('Gjett tallet mellom grensene: '))
    while gjett != tall:
        gjett = int(input('Feil tall, prøv igjen ellr trykk q for å avslutte: '))
        #if gjett == str.lower(q):  kunne lagt til disse for å avslutte, måtte da vært while int(gjett) != eller nos likt
            #break
    print('Gratulerer du klarte å gjette riktig!')
oppgave()
