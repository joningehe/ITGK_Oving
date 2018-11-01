    #Oppgave A
def string_iterator(string_input):
    for ch in string_input:
        print(ch)

string_iterator(string_input = input('Skriv inn tekst: '))

    #Oppgave B
def character_3(string_input_2):
    if len(string_input_2) >= 3:
        for i in range (2, 3):
            print(string_input_2[i])
    else:
        print('q')

character_3(string_input_2 = input('Skriv inn tekst: '))

    #Oppgave C
def biggest_index(string_input_3):
    biggest = 0
    for j in range(len(string_input_3)):
        if ord(string_input_3[j]) > biggest:
            biggest = ord(string_input_3[j])
    return chr(biggest)

print(biggest_index(string_input_3 = input('Skriv inn teskt: ')))
