import random
def oppgaveA(): #Forstår ikke hva som må fikses
    antall_studenter = int(input('Hvor mange studenter? '))
    antall_emner = int(input('Hvor mange emner? '))
    navn = ['Jon', 'Anders', 'Petter', 'Sander', 'Henrik', 'Øyvind', 'Mathias', 'Andreas', 'Kristine', 'Kristina', 'Malin', 'Ida', 'Eirin']
    emner = ['ITGK', 'Webtek', 'Matte A', 'Ex.phil']
    nummer = random.randint(0, 101)
    for navn in range(antall_studenter):
        for emner in range (antall_emner):
            if nummer > 80:
                print(navn, 'elsker', emner)
            elif nummer > 60:
                print(random.choice(navn), 'liker', random.choice(emner))
            elif nummer > 40:
                print(random.choice(navn), 'har ingen sterk mening om', random.choice(emner))
            elif nummer > 20:
                print(random.choice(navn), 'liker ikke', random.choice(emner))
            elif nummer == 0:
                print(random.choice(navn), 'hater', random.choice(emner))
            else:
                print('Noe må ha gått feil, kjør på nytt.')

def oppgaveA2(): #RIKTIG
    antall_studenter = int(input('Hvor mange studenter? '))
    antall_emner = int(input('Hvor mange emner? '))
    navn = ['Jon', 'Anders', 'Petter', 'Sander', 'Henrik', 'Mathias', 'Andreas', 'Kristine', 'Kristina', 'Malin', 'Ida', 'Eirin']
    emner = ['ITGK', 'Webtek', 'Matte A', 'Ex.phil']
    for i in range(antall_studenter):
        for j in range (antall_emner):
            tilfeldig = random.randint(0, 101)
            tilfeldig_navn = random.choice(navn)
            tilfeldig_emne = random.choice(emner)
            if tilfeldig > 80:
                print(tilfeldig_navn, 'elsker', tilfeldig_emne)
            elif tilfeldig > 60:
                print(tilfeldig_navn, 'liker', tilfeldig_emne)
            elif tilfeldig > 40:
                print(tilfeldig_navn, 'har ingen sterk mening om', tilfeldig_emne)
            elif tilfeldig > 20:
                print(tilfeldig_navn, 'liker ikke', tilfeldig_emne)
            elif tilfeldig > 0:
                print(tilfeldig_navn, 'møter ikke opp i forelesningene til', tilfeldig_emne)
            elif tilfeldig == 0:
                print(tilfeldig_navn, 'hater', tilfeldig_emne)
            else:
                print('Noe må ha gått feil, kjør på nytt.')

def oppgaveA3(): # denne funker, men oppfyller ikke de ekstra kravene
    antall_studenter = int(input('Hvor mange studenter? '))
    antall_emner = int(input('Hvor mange emner? '))
    for stud in range(antall_studenter):
        for emne in range(antall_emner):
            print('Stud', 1+stud, 'elsker emner', 1+emne, end=" ")

def oppgaveB(): # denne funker, men hvordan få bort mellomrom før og etter :
    for time in range(0, 24):
        for minutt in range(0,60):
            print(time,':',minutt)

def oppgaveC(): # kunne vært formatert finere
    for x in range (1, 11):
        for y in range (1, 11):
            print(x * y, end=" ")
        print()

oppgaveA3()
