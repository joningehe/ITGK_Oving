oppgaveA = [1, 2, 3, 4, 5, 6]

def is_six_at_edge():
    return (oppgaveA[-1] == 6 or oppgaveA[0] == 6) #bruk return for å få false/true avhengig av uttrykket er riktig

print(is_six_at_edge())

def average(oppgaveB):  #hvordan får jeg lista til å bli seperert med input space
    listB = []
    for tall in oppgaveB:
        listB.append(int(tall))
    return(round(sum(listB) / len(listB)))

print(average(oppgaveB = input('Skriv inn tall: ')))

def median(oppgaveC):
    oppgaveC.sort()
    median = ((len(oppgaveC) // 2))
    return(oppgaveC[median])


print(median(oppgaveC = [1,4,2,5,3]))
