def oppgave():
    print('INFO')
    print('Dette programmet besvarer om din utleie av egen bolig er skattepliktig.')
    print('Først trenger vi å vite hvor stor del av boligen du har leid ut.')
    print('Angi dette i prosent, 100 betyr hele boligen, 50 betyr halve,')
    print('20 en mindre del av boligen som f.eks. en hybel.')
    print('-----------------------------------------------------------------------')

    print('DATAINNHENTING:')
    type_bolig = str.lower(input('Er boligen sekundærbolig eller fritidsbolig? (J/N)'))
    if type_bolig == 'j' or type_bolig == 'fritid' or type_bolig == 'sekundær':
        datainnhenting2()
    else:
        andel_utleid = float(input('Oppgi hvor mye av boligen som ble utleid: '))
        print('-----------------------------------------------------------------------')
        print('DATAINNHENTING')
        if andel_utleid > 0 and type_bolig == 'n':
            datainnhenting(andel_utleid)#sender variabelen videre
        else:
            print('Inntekten er ikke skattepliktig')

def datainnhenting(andel_utleid):#henter variabelen fra der den var sendt
    bo = str.lower(input('Bor du i leiligheten? (J/N)'))
    if bo == 'j' and andel_utleid <= 50:
        print('Inntekten er ikke skattepliktig.')
    else:
        inntekt = float(input('Hvor mye er inntekten fra leie? '))
        if inntekt < 20000:
            print('Inntekten er ikke skattepliktig')
        else:
            print('Skattepliktig beløp er kr:', inntekt)

def datainnhenting2():
    sekundær_eller_ferie = str.lower(input('"S" for sekundær eller "F" for fritid'))
    if sekundær_eller_ferie == 'sekundær' or sekundær_eller_ferie == 'sekundærbolig' or sekundær_eller_ferie == 's':
        print('Inntekt skattes fra første krone')
    else:
        antall_boliger = int(input('Hvor mange fritidsboliger leier du ut?'))
        print('Du kan leie ut inntil', antall_boliger * 10000, 'kroner skattefritt.')
        inntekt = int(input('Hvor mye er inntekten fra leie per bolig? ')) * 3
        skattepliktig = 0.85 * (inntekt - (antall_boliger * 10000))
        print('Skattepliktig beløp er kr:', skattepliktig)

oppgave() # se over datainnhenting2 om noe ikke funker
