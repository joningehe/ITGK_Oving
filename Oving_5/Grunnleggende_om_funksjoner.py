def siksak():
    print()
    print("**  **  **  **  **  **  **  **  **")
    print("  **  **  **  **  **  **  **  **")
    print()

def oppgaveA():
    print("Data fra spørreundersøkelse")
    siksak()
    print("Del 1: ... div. data her, ikke vist")
    siksak()
    print("Del 2: ... mer data ...")
    siksak()
    print("Del 3: ... enda mer data ...")
    siksak()
    print("Del 4: ... ytterligere data ...")

from turtle import *
def oppgaveB():
    def flyto(x, y):
        up()
        goto(x, y)
        down()

    def filled_circle(farge, radius):
        begin_fill()
        color(farge)
        circle(radius)
        end_fill()

    bgcolor("grey")

    #tegner ansikt
    flyto(0, -100)
    filled_circle("yellow", 100)

    # det ene øyet
    flyto(-30, 20)
    filled_circle("green", 20)

    # pupill
    filled_circle("black", 10)

    # det andre øyet
    flyto(30, 20)
    filled_circle("green", 20)

    # pupill
    filled_circle("black", 10)

    #munnen
    flyto(0, -50)
    pensize(5)
    color("red")
    circle(50,30)
    circle(50,-60)

def oppgaveC():
    def komparativ(adj):
        if len(adj) >= 8: # unøyaktig
            svar = "mer " + adj
        else:
            svar = adj + "ere"
        return svar

    def superlativ(adj):
        svar2 = adj + "est"
        return (svar2)

    adj = input("Beskriv deg selv med et adjektiv: ")
    print("Hah! Jeg er mye", komparativ(adj), "!")
    print ("Jeg er faktisk", superlativ(adj), "i hele verden.")

    adj = input("Skriv inn et adjektiv: ")
    svar = input("Hva er komparativ for " + adj + "? ")
    fasit = komparativ(adj)
    if svar == fasit:
        print("Korrekt!")
    else:
        print("Feil, det var", fasit)

    svar2 = input("Hva er superlativ for " + adj + "? ")
    fasit2 = superlativ(adj)
    if svar2 == fasit2:
        print("Korrekt!")
    else:
        print("Feil, det var", fasit2)

        #OppgaveD():
def main():
    oppgaveC()

main()
