def oppgaveA():
    print('Skriv inn 7 heltall')
    i = 0
    summen = 0
    while i < 7:
        heltall = int(input('Heltall: '))
        summen = summen + heltall
        i = i + 1
    print('Summen av tallene dine er', summen)

def oppgaveB():
    start = 1
    stop = 1000
    for mult in range(1, stop):
        start *= mult
        if start > stop:
            break
    print('Tallet ditt er', start)

def oppgaveC(): #fucka litt opp på denne, prøv å loop
    terminer = 'Jeg'
    forsok = 1
    skriv_inn = input('Hvem er den beste personen i verden? (Trykk "q" for å avslutte) ')
    while skriv_inn != terminer:
        print('Svaret ditt var feil, prøv igjen')
        forsok += 1
        skriv_inn = input('Hvem er den beste personen i verden? (Trykk "q" for å avslutte) ')
        if str.lower(skriv_inn) == 'q':
            print('Du mislykkes, men prøvde', forsok, 'ganger.')
            break
        else:
            print('Korrekt, du brukte', forsok, 'forsøk.')

def oppgaveC2(): # denne ble bedre enn den forrige i mine øyne
    print('Skriv p?')
    skriv = str.lower(input(''))
    terminer = 'p'
    if skriv == terminer:
        print('Gratulerer, du brukte bare 1 forsøk på å gjøre det')
    else:
        antall = oppgaveCLoop(skriv, terminer)
        print('Du brukte', antall, 'forsøk.')

def oppgaveCLoop(skriv, terminer):
    antall = 1
    while skriv != terminer:
        print('Dette var desverre feil, prøv igjen')
        skriv = str.lower(input(''))
        antall = antall + 1
        if skriv == 'q'
    return (antall)
