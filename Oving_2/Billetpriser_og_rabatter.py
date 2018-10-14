def oppgave():
    dager_til_reise = int(input('Hvor mange dager er det til du skal reise?'))
    if dager_til_reise >= 14:
        print('Du kan få minstepris på 199,-')
        minstepris = str.lower(input('Denne kan ikke refunderes, ønsker du den fortsatt (J/N)'))
        if minstepris == 'j':
            print('Takk for pengene, god reise!')
        else:
            alder = int(input('Hvor gammel er du?'))
            if alder < 16:
                print('Da blir billettprisen din på 220,-')
            else:
                status = str.lower(input('Er du senior (60+), militær i uniform eller student? (J/N)'))
                if status == 'j':
                    print('Da blir billetprisen din på 330,-')
                else:
                    print('Beklager, du må desverre betale fullpris på 440,-')
    else:
        alder = int(input('Hvor gammel er du?'))
        if alder < 16:
            print('Da blir billettprisen din på 220,-')
        else:
            status = str.lower(input('Er du senior (60+), militær i uniform eller student? (J/N)'))
            if status == 'j':
                print('Da blir billetprisen din på 330,-')
            else:
                print('Beklager, du må desverre betale fullpris på 440,-')

oppgave() # hvordan redirecter man til tidligere linje for å slippe å måtte skrive inn alt på nytt?

#gjør ikke oppgaveD
