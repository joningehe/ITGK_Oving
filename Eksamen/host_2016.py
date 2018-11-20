#Oppgave A)
parties = ['TeaParty', 'CoffeeParty', 'MilkParty', 'HouseParty', 'BeachParty']
def initElection2(parties):
    list = []
    for i in range(92):
        votes = []
        number = 0
        for i in range(len(parties)):
            votes.append(number)
        list.append(votes)
    return list

def initElection(parties):
    return [[vote_numbers for i in range(len(parties))] for j in range(distric_number)]

distric_number = 92
election = initElection(parties)

#Oppgave B)
def updateElection(election, district_number, vote_numbers):
    for i in range(leng(vote_numbers)):
        election[district][i] += vote_numbers[i]
    return election

#Oppgave C)
def printLeadP(election, parties):






#Oppgave 4
tall = 1
#A)
def i2_txt(tall):
    if tall == 0 or tall > 99:
        return 'Out of range'


    if tall < 20:
            return + D.get(tall)
    else:
        for nummer in tall:
            return D.get(tall*10)+'-'+D.(tall)

#B)
def i3_txt(tall):
    if tall < 100:
        return i2_txt(tall)
    else:
        hundre = tall // 100
        resten = tall % 100
        return D.get(hundre)+' hundred '+i2_txt(resten)

#C)
def i9_txt(tall):
    millions = tall // 1000000
    thousands = tall % 1000000
    resten =
    if millions != 0:
        return i3_txt(millions) 'millions' + i3_txt(thousands) + 'thousand and' i2_txt()

#D)
def add_words(setning)
    liste = [setning.split() for ch in setning]
    
