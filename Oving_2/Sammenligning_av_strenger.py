def oppgaveA():
    a = str.lower(input('Skriv inn matvare'))
    b = str.lower(input('Skriv inn en annen matvare'))
    if a == b:
        print('Matvarene er like')
    else:
        print('Matvarene er ikke like')
#str.lower() returnerer lower-case bokstaver

def oppgaveB():
    a = str.lower(input('Skriv inn navn'))
    b = str.lower(input('Skriv inn et nytt navn'))
    if a < b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)
#viser seg at ola < ole siden navnene gjort om til tall er forskjellig
#trenger ingen egen kommando for dette

def oppgaveC():
#Kode 1 vil printe 'k er større enn b'
#Kode 2 vil printe la før ny
#Kode 3 vil printe 'druer'
    pass


#!!!!!!!!!!!!MÅ TESTES!!!!!!!!!!!!!!
oppgaveA()
oppgaveB()
