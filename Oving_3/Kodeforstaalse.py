def oppgaveA(): # lest ikke oppgaven godt nok, svaret blir 101011001 fordi while a betyr så lenge a er et tall>0
    a=345
    b=''
    while a or b=='':
        b=str(a%2)+b
        a=a//2
    print(b)

    #Det skrives ut 1, først gjøres b om til summen av modulo 345 som er 1
    #Deretter gjøres heltalldiv av 344//2 som er 122
    #Modulo av 122%2 er 0 som betyr 0 + 1
    #B er altså 1
    #så "1 " printes

#Dette svaret var feil, riktig var 101011001

def oppgaveB():
    for x in range(0, 10, 2):
        print(x, end='')
        if x%4==0:
            print( ": Dette tallet går opp i 4-gangern")
        else:
            print()
#_blank
#_blank
#Dette tallet går opp i 4-gangern
#_blank
#Dette tallet går opp i 4-gangen

#FEIL!!!!!!!!!!!!!!!!!!!!!!

#0: Dette tallet går opp i 4-gangern
#2
#4: Dette tallet går opp i 4-gangern
#6
#8: Dette tallet går opp i 4 gangern
#Husk på at 0 modulo 4 == 0 og være obs på hva som faktisk står i print setningen

def oppgaveC():
    i = 1
    while i<10:
        i = i*2
    print(i)
#512 (2^9)
#FFFFEEEEEIIILL!!!!!
#Riktig svar er 6
#Begynner som 1, deretter blir den 2, deretter blir den 4, deretter 8, deretter 16 som er > 10 og løkka avsluttes

def oppgaveD():
    i = 1
    j = 3
    while j>0:
        i = i*2
        j = j - 1
    print(i)
#8
#riktig

def oppgaveE():
    i = 5
    for x in range(i):
        for y in range(x+1):
            print("*", end="")
        print()
#*
#* *
#* * *
#* * * *
#* * * * *
#riktig
