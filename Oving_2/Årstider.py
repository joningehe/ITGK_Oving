def arstider():
    maaned = str.lower(input('Hvilken måned er det? '))
    dato = int(input('Hvilken dato er det? '))
    if (maaned == 'desember' and dato >= 21) or (maaned == 'januar') or maaned == ('februar') or (maaned == 'mars' and dato < 20):
        print('Vinter')
    elif (maaned == 'mars' and dato >= 20) or (maaned == 'april') or maaned == ('mai') or (maaned == 'juni' and dato < 21):
        print('Vår')
    elif (maaned == 'juni' and dato >= 21) or (maaned == 'juli') or maaned == ('august') or (maaned == 'september' and dato < 22):
        print('Sommer')
    else:
        print('Høst')

arstider() # koden er ugly af men funker :) om jeg legger på en siste linje for høst hvor jeg gjentar det samme som tidligere
#vil jeg kunne avslutte med en else som sier "ugyldig dato" om annen input enn 1-31 på dato og ugyldig måned


def arstider2():
    maaned = str.lower(input('Hvilken måned er det? '))
    dato = int(input('Hvilken dato er det? '))
