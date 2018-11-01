    #Oppgave A
def blokkbostav_split(streng_1):
    return(str.upper(streng_1.strip()))

print(blokkbostav_split(streng_1 = input('Skriv inn en setning: ')))

    #Oppgave B
def karakter_split(streng_2, karakter):
    return(streng_2.split(karakter))

print(karakter_split(streng_2 = input('Skriv en setning: '), karakter = input('Skriv en bokstav: ')))

    #Oppgave C
#Kodesnutten vil returnere:
#"The more you weigh, the harder you are to kidnap. Stay safe. Eat cake."
#Dette er fordi 'eat' er i s2

    #Oppgave D
for i in range(1, 8):
    print('Z'*i)
for j in range(7, 0, -1):
    print('Z'*j)
