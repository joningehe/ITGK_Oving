def oppgave():
    print("Dette er et program for å teste din sjenerøsitet.")
    har_epler = int(input("Hvor mange epler har du? "))
    if har_epler == 0:
        print("Æsj, det sier du bare for å slippe å gi noe!")
    else:
        gir_epler = int(input("Hvor mange kan du gi til meg? "))
        if gir_epler < (har_epler / 2):
            print("Du beholder det meste for deg selv...")
            resterende_epler = har_epler - gir_epler
            print("Du har nå", resterende_epler, "epler igjen.")
        else:
            print("Takk, det var snilt!")
            resterende_epler = har_epler - gir_epler
            if resterende_epler > 1:
                print("Du har nå", resterende_epler, "epler igjen.")
            elif resterende_epler == 1:
                print('Du har nå', resterende_epler, 'eple igjen.')
            else:
                print('Du har nå ingen epler igjen. Gi meg', -resterende_epler, 'neste gang vi møtes.')
oppgave()
