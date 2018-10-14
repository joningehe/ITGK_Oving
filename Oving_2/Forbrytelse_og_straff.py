def oppgaveA():
    # leser inn data
    prom = float(input("Hvor stor var promillen? "))
    motor = input("Var farkosten en motorvogn? (j/n) ")
    f = input("Var personen fører av vognen? (j/n) ")
    leds = input("Var personen ledsager ved øvekjøring? (j/n) ")
    n = input("Var det nødrett? (j/n) ")

    # vurderer straffbarhet
    if prom < 0.2 and motor == "j" and f == "j" or leds == "j" and n == "n":
       print("Det var straffbar promillekjøring.")
    else:
        print("Ikke straffbart, ingen bot.")

def oppgaveB():
    # leser inn data
    prom = float(input("Hvor stor var promillen? "))
    motor = input("Var farkosten en motorvogn? (j/n) ")
    f = input("Var personen fører av vognen? (j/n) ")
    leds = input("Var personen ledsager ved øvekjøring? (j/n) ")
    n = input("Var det nødrett? (j/n) ")

    # vurderer straffbarhet
    if prom > 0.2 and (motor == "j" and f == "j" or leds == "j" and n == "n"):
       print("Det var straffbar promillekjøring.")
    else:
        print("Ikke straffbart, ingen bot.")

def oppgaveC():
    prom = float(input("Hvor stor var promillen? "))
    if prom > 0.5:
        print("Bot: en halv brutto månedslønn, samt fengsel.")
    elif prom > 0.4:
        print("Forelegg: 10000,-")
    elif prom > 0.2:
        print("Forelegg: 6000,-")
    elif prom < 0.2:
        print("Ikke straffbart, ingen bot.")


def oppgaveD():
    # leser inn data
    prom = float(input("Hvor stor var promillen? "))
    nekt = input("Nektet å samarbeide ved legetest? (j/n) ")
    tidl = input("Tidligere dømt for promillekjøring? (j/n) ")
    if tidl == "j":
        aar = int(input("Antall år siden siste domfellelse: "))
    else:
        aar = 999

    # vurderer inndragning av førerkort
    if tidl == ("j" and prom > 0.2) or (nekt == "j" and aar < 5):
        print("Førerkort inndras for alltid.")
    elif prom > 1.2 or nekt == "j":
        print("Førerkort inndras minst 2 år.")
    elif prom > 0.8:
        print("Førerkort inndras 20-22 mnd.")
    elif prom > 0.5:
        print("Førerkort inndras vanligvis 18 mnd.")
    elif prom > 0.2:
        print("Førerkort inndras inntil 1 år.")
    else:
        print("Ingen inndragning av førerkort.")


def oppgaveE():
    # leser inn data
    prom = float(input("Hvor stor var promillen? "))
    motor = input("Var farkosten en motorvogn? (j/n) ")
    f = input("Var personen fører av vognen? (j/n) ")
    leds = input("Var personen ledsager ved øvekjøring? (j/n) ")
    n = input("Var det nødrett? (j/n) ")
    nekt = input("Nektet å samarbeide ved legetest? (j/n) ")
    tidl = input("Tidligere dømt for promillekjøring? (j/n) ")
    if tidl == "j":
        aar = int(input("Antall år siden siste domfellelse: "))

    # legg til din kode nedenfor her:

oppgaveA()
oppgaveB()
oppgaveC()
oppgaveD()
