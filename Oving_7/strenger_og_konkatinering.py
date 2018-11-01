    #Oppgave A
def string_returner(a, b):
    melding = a + " " + b
    return melding

print(string_returner(a = input('Skriv et ord: '), b = input('Skriv et ord: ')))

    #Oppgave B
def list_returner(liste):
    for i in liste:
        print(i, end="")
    print(" ")

liste = []
for li in range(4):
    input_liste = input('Skriv inn noe til liste: ')
    liste.append(input_liste)
list_returner(liste)

    #Oppgave C
def first_string_list(liste):
    for i in liste:
        print(i[0])

first_string_list(liste)

    #Oppgave D
#Funksjon 1 returnerer den fjerde bokstaven i hver streng, om lengden til
#strengen er over 3, bob.
#Funksjon 2 legger sammen strengen fra funksjon 1 med seg selv, så det som blir
#returnert fra streng 1*2, bobbob.
