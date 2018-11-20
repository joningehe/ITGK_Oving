    #Oppgave 3 Programmering Gjennomsnittsmåling (30%):
#(år, måned, dag) og (timer, minutter, sekunder)
#box_a.txt  box_b.txt

    #Oppgave 3a)
def file_to_table(filename):
    list = []
    f = open(filename, r)
    x = f.readlines()
    for i in range(len(x)):
        y = x[i]
        for len(x) in range(len(y)):
            split(' , ')
            z=[]
            z.append(int(y[0,4])+','int(y[4,6])+','int(y[6,8])+','int(y[8,10])+','int(y[10,12])+','int(y[12,14])+','+str(y[14,21]))
            list.append(z)
    f.close()
#Lager en tom liste, åpner filen, leser ut alt som lister, kjører gjennom lengden av lister, henter ut alt inni hver liste,
#splitter basert på ' , ', legger til ny liste, legger ny liste til top liste list


    #Oppgave 3b)
def time_diff(start, end):
    start.strip(',')
    end.strip(',')
    if start[7] == end[7]:
        return (start[8:] - end[8:])
    else:
        difference = diff_date(start[:8], end[:8]) * (24*60*60)
        return (start[8:] - end[8:] + difference)
#Kunne her brukt kun nederste funksjon, men antar at bilen ikke bruker 1 måned på å kjøre denne strekningen
#så vil aldri falle på samme dato i måneden. Funksjonen returnerer forskjellen mellom tallene i posisjon
#8 og utover etter at ',' er fjernet. Legger til 24*3600 om det er mer enn 1 dag.

    #Oppgave 3c)
def check_min_distance(car_table, diff):
    car_table.stip(', ')
    car_1 = car_table[]
    for i in range(len(car_table)):

#SCRAP OPPGAVENE OVER, SER AT DE IKKE FUNKER FORDI TIME/DATE IKKE ER CONSISTENT

    #Oppgave 3d)
def list_el_cars(car_table):
    el_biler = 0
    for i in range(len(car_table)):
        if 'el' in str.lower(car_table[i]):
            el_biler += 1
    return el_biler

    #oppgave 3e)
import random
def generate_license_numbers(amount):
    list = []
    letters = [BS, CV, EL, FY, KU, LE, NB, PC, SY, WC]
    for i in range(amount):
        number = str(letters[randint(0, 9)]+randint(1,9)+randint(0,9)+randint(0,9)+randint(0,9)+randint(0,9))
        if number in list:
            try:
                number = str(letters[randint(0, 9)]+randint(1,9)+randint(0,9)+randint(0,9)+randint(0,9)+randint(0,9))
        else:
        list.append(number)

#Ganse sikker på at jeg kunne brukt random.randint istedenfor import, men basically så tar den tilfeldig letters og
#nummer, sannsynlihheten lav for gjenbruk.

    #oppgave 3f)
def list_speeders(filename_a, filename_b, speed_limit, distance):
    pass


    #oppgave 4a)
def formatTime(seconds):
    sekunder = seconds % (24*60)
    minutter = (seconds % 24)
    timer = seconds // 24
    #usikker på hva de vil

    #oppgave 4b)
def valuesDecember():
    first = 3*3600 + 18*60
    period = 12*3600 + 25*60 + 12
    return first, period

    #oppgave 4c)
def genTides():
    
