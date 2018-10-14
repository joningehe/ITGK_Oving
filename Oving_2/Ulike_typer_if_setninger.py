def oppgaveA():
    tid = int(input("Hvor mange minutt har kaken stått i ovnen? "))
    if tid >= 50:
        print("Kaken kan tas ut av ovnen.")
    print("Tips til servering: vaniljeis.")

def oppgaveB():
    epler = int(input("Hvor mange epler har du? "))
    barn = int(input("Hvor mange barn passer du? "))
    if barn > 0:
        print("Da blir det", epler // barn, "epler til hvert barn")
        print("og", epler % barn, "epler til overs til deg selv.")
    print("Takk for i dag!")

def oppgaveC():
    alder = int(input('Skriv inn din alder:'))
    if alder >= 18:
        print('Du kan stemme.')
    else:
        print('Du kan ikke stemme')

def oppgaveD():
    alder = int(input('Skriv inn din alder:'))
    if alder >= 18:
        print('Du kan stemme.')
    elif alder >=16:
        print('Du kan stemme ved lokalvalg, men ikke stortingsvalg.')
    else:
        print('Du kan ikke stemme.')

def oppgaveE():
    alder = int(input('Skriv inn din alder for korrekt pris:'))
    if alder >= 67:
        print('Billetpris: 40kr')
    elif alder >= 26:
        print('Billetpris: 80kr')
    elif alder >= 12:
        print('Billetpris: 50kr')
    elif alder >= 3:
        print('Billetpris: 30kr')
    else:
        print('Din billet er gratis')

oppgaveA()
oppgaveB()
oppgaveC()
oppgaveD()
oppgaveE()
