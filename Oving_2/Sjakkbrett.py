def oppgaveA():
    pos = str.lower(input('Skriv posisjon med bokstav først deretter tall uten mellomrom: '))
    bokstav = pos[0]
    tall = int(pos[1])
    if (bokstav == 'a') or (bokstav == 'c') or (bokstav == 'e') or (bokstav == 'g'):
        if (tall == 1) or (tall == 3) or (tall == 5) or (tall == 7):
            print('Svart')
        else:
            if (bokstav =='b') or (bokstav == 'd') or (bokstav == 'f') or (bokstav == 'h'):
                if (tall == 2) or (tall == 4) or (tall == 6) or (tall == 8):
                    print('Svart')
    else:
        print('Hvit')

def oppgaveA2():
    pos = str.lower(input('Skriv posisjon med bokstav først deretter tall uten mellomrom: '))
    bokstav = pos[0]
    tall = int(pos[1])
    if ((bokstav == 'a') or (bokstav == 'c') or (bokstav == 'e') or (bokstav == 'g')) and ((tall == 1) or (tall == 3) or (tall == 5) or (tall == 7)):
        print('Svart')
    elif ((bokstav =='b') or (bokstav == 'd') or (bokstav == 'f') or (bokstav == 'h')) and ((tall == 2) or (tall == 4) or (tall == 6) or (tall == 8)):
        print('Svart')
    else:
        print('Hvit')

oppgaveA2() # denne funker fordi jeg fucka opp ovenfor, gå mer i dybde på hvordan denne er fucka
#les om pos[]
