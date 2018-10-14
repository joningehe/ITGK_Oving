import math
def oppgave():
    print('Vi skal nå løse andregradsligninger. Til dette trenger vi å vite de tre verdiene for a, b og c')
    print('Om du ikke husker det er uttrykket "ax^2 + bx + c = 0".')
    a = float(input('Hva er verdien for "a"? '))
    b = float(input('Hva er verdien for "b"? '))
    c = float(input('Hva er verdien for "c"? '))
    d = (b ** 2) - (4 * a * c)  #uttrykket leter etter reele og imaginære røtter
    if d < 0:
        print('Løsningen har 2 imaginære løsninger.')
    elif d > 0:
        print('Løsningen har 2 reele løsninger.')
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print('Disse er', x1, 'og', x2)
    else:    #kan man skrive else på denne måten?
        print('Løsningen har 1 reel løsning (dobbeltrot).')
        x = (-b + math.sqrt(d)) / (2 * a)
        print('Denne er', x)
oppgave()

#funka på første forsøk, hva var tenkt opprinnelig?
