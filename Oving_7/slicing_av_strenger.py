    #Oppgave A
def fourth_string_returner(sentence):
    print(array_1[3::4])

fourth_string_returner(sentence = input('Skriv inn en setning: '))

    #Oppgave B
def last_two_returner(array):
    letters = ""
    for i in array:
        letters += i[-2:]
    return letters

array = []
for li in range(4):
    input_liste = input('Skriv inn noe til liste: ')
    array.append(input_liste)

print(last_two_returner(array))

    #Oppgave C
#Streng 2 er korrekt, 1 prøver å putte en streng direkte inn i midten av et
#argument og streng 3 har syntaxfeil.
