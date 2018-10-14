def oppgaveA():
    tall = int(input('Skriv inn et tall: '))
    if tall >= 0:
        print('Absoluttverdien til', tall, 'er', tall)
    else:
        print('Absoluttverdien til', tall, 'er', absol(tall))

def absol(tall):
    tall = -(tall)
    return(tall)


def oppgaveB():
    knop = float(input('Oppgi farten din i knop: '))
    print('Det blir', round(hastighet(knop), 2), 'km/t.')

def hastighet(knop):
    knop_ms = (0.514444444 * 3.6)
    kmt = (knop * knop_ms)
    return(kmt)


def oppgaveC():
    fot = int(input("Oppgi antall fot: "))
    tommer = int(input("Oppgi antall tommer: "))
    cm = imp2cm(fot, tommer)
    print("Det blir", round(cm), "cm")

def imp2cm(fot, tommer):
    fotkonv = (fot * 12)
    tommerkonv = ((tommer + fotkonv) * 2.54)
    return(tommerkonv)

def oppgaveD():
    def cmyk2rgb(C, M, Y, K):
        R = round(255 * (1 - C) * (1 - K))
        G = round(255 * (1 - M) * (1 - K))
        B = round(255 * (1 - Y) * (1 - K))
        return(R, G, B)


    print("Oppgi farge i CMYK og få det konvertert til RGB.")
    C = float(input("C: "))
    M = float(input("M: "))
    Y = float(input("Y: "))
    K = float(input("K: "))
    R, G, B = cmyk2rgb(C, M, Y, K)
    print("Som RGB:", R, G, B)

    # viser fargen på skjermen:
    from turtle import colormode, bgcolor
    colormode(255)
    bgcolor(int(R), int(G), int(B))

oppgaveA()
oppgaveB()
oppgaveC()
oppgaveD()
