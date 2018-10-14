def oppgave():
    hemmelig_ord = str.lower(input('Skriv inn et hemmelig ord: '))
    antall_liv = int(input('Skriv inn antall reserve liv: '))
    bokstaver = list(hemmelig_ord)
    i = list()
    while len(bokstaver) > 0:
        if antall_liv > 0:
            gjett = str.lower(input('Gjett på en bokstav: '))
            if gjett in bokstaver:
                print('Korrekt bokstav')
                bokstaver.remove(gjett)
            else:
                antall_liv -= 1
                print('Feil bokstav, prøv igjen')
        else:
            print('Du klarte det ikke')
            break
    if len(bokstaver) == 0:
        print('Gratulerer du klarte det!')
        print('Ordet var "', hemmelig_ord, '".')
    else:
        pass

oppgave()
