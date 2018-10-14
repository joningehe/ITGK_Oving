def oppgave1():
    antall = int(input('Hvor mange adjektiv ønsker du? '))
    for i in range(antall):
        adj = input("Beskriv deg selv med et adjektiv? ")
        print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
    print("Takk for nå!")


def oppgave2():
    antall = int(input('Hvor mange adjektiv ønsker du?'))
    i = 0
    while i < 3:
        adj = input("Beskriv deg selv med et adjektiv? ")
        print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
        i += 1  # øker i med 1
    print("Takk for nå!")


def oppgave3():
    i = 42
    print('Du har', i, 'bokstaver til din disposisjon.')
    while i > 0:
        adj = input("Beskriv deg selv med et adjektiv? ")
        print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
        i -= len(adj)  # trekker fra string lengde på adj fra i
        if i > 0:   #la på if/else for å unngå å få -i til disposisjon
            print('Du har', i, 'bokstaver til din disposisjon.')
        else:
            print("Takk for nå!")

def oppgave4():
    print("Oddetallene fra 1 til 20:")
    for number in range(1, 20, 2):
        print(number, end = " ")
    print()

    print("Tallene i 3-gangen mellom 12 og 25:")
    for number in range(12, 25, 3):
        print(number, end = " ")
    print()

    print("Tallene i 5-gangen mellom 20 og 81:")
    for number in range(20, 81, 5):
        print(number, end = " ")
    print()

    print("Tallsekvensen 48, 56, 64, 72, 80")
    for number in range(48, 81, 8):
        print(number, end = " ")
    print()

    print("Telle baklengs fra 100 til 80, med intervall på -3, dvs. 100, 97, ...:")
    for number in range(100, 80, -3):
        print(number, end = " ")
    print()

def oppgave5():
    print ('Tallene 1 til 5:')
    for number in range (1, 5):
        print(number, end = " ")
    print()

def oppgave6():
    for value in range(15, 1, -1):
        print(value)

from turtle import *
def oppgave7():
    vinkel = int(input('Velg vinkel på firkanten din: '))
    i = 500/vinkel
    while i < 500:
        forward(500/vinkel)
        left(vinkel)
        i = i + vinkel
#litt svak, funker ikke helt som planlagt, men dette er prinsippet for auto-stop

oppgave7()
