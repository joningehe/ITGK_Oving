import time
from turtle import * #viktig å huske på å importere før funksjonen kjøres
def oppgave():
    print("Hei, jeg kan tegne en trekant")
    pensize(7)          # sett pennen 7 piksler tykk
    pen_color = str.lower(input('Vil du har lilla eller blågrønn trekant? (L/B) '))
    if pen_color == 'l':
        pencolor("#552988")     # sett pennefargen til lilla
    elif pen_color == 'b':
        pencolor("#5cbec9")     # sett pennefargen til teal
    else:
        print('Siden du valgte en ugyldig farge, velger vi en for deg :)') # vil egentlig loope denne til gyldig farge er valgt
        pencolor("#f58025")     # sett pennefargen til oransje
    bgcolor("#00509e")     # sett bakgrunnsfargen til NTNU sin farge
    fill_color = str.lower(input('Vil du ha gul eller blå fyll farge? (G/B)'))
    if fill_color == 'g':
        fillcolor("#d5d10e") # sett fyllfargen gul
    elif fill_color == 'b':
        fillcolor("#79a2ce") # sett fyllfargen til blå
    else:
        print('Ugyldig farge, vi setter den for deg ;)')
        fillcolor("#ad208e") # sett fyllfargen til rosa

    onske = str.lower(input('Ønsker du at trekanten peker opp eller ned? (O/N) '))
    if onske == 'o':
        begin_fill()
        forward(200)        # gå 100 piksler framover
        left(120)           # drei 120 grader venstre
        forward(200)
        left(120)
        forward(200)
        end_fill()
    elif onske == 'n':
        begin_fill()
        forward(200)        # gå 100 piksler framover
        right(120)           # drei 120 grader høyre, trekanten ender på et lavere punkt pekende nedover
        forward(200)
        right(120)
        forward(200)
        end_fill()
    else:
        print('Om du ikke forstod det betyr o "opp" og n "ned", vennligst tenk litt neste gang :)')
        oppgave()
    # Holder vinduet med tegningen åpent i 10 sekunder. Ha dette som siste linje i koden din
    time.sleep(10)

oppgave()#hele denne oppgaven hadde vært enklere i pycharm
