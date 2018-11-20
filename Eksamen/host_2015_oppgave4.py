write_to_grades = open('grades.py', 'w')
write_to_grades.write(NTNU_scores = (89, 77, 65, 53, 41, 0))
write_to_grades.write(NTNU_letters = ('A', 'B', 'C', 'D', 'E', 'F'))
write_to_grades.write(TASKS = ('1', '2a', '2b', '2c', '3a', '3b', '3c', '3d', '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h'))
write_to_grades.write(WEIGHTS = (25, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5))
write_to_grades.close()

def makeArray(Numbers, Texts):
    complete_list = [i for i in Numbers]
    for i in range(len(complete_list)):
        complete_list[i].append(Texts[i])
    return complete_list

def computeScore(Points, WEIGHTS):
    score = []
    for i in range(len(Points)):
        weighted_points = (Points[i] * (WEIGHTS[i])
        score.append(weighted_points)
    return float(sum(score)/100, 1)

    return sum(Points[i]*WEIGHTS[i] for i in range(len(Points)))/100 #?

def score2Letter(scoreSum, limitLetters):
    if scoreSum >= 89:
        return limitLetters[0]
    elif scoreSum >= 77:
        return limitLetters[1]
    elif scoreSum >= 65:
        return limitLetters[2]
    elif scoreSum >= 53:
        return limitLetters[3]
    elif scoreSum >= 41:
        return limitLetters[4]
    else:
        return limitLetters[5]


def addCandidate(candidateNumber, Scores, WEIGHTS):
    try:
        exam = open('eksamen.txt', 'w+')
    except Exception as e:
        print(e)
    for i in range(len(Scores)):
        exam.write(candidateNumber+'    '+Scores[i].replace(',', '  ')+computeScore(Scores[i], WEIGHTS))
    exam.close()


def readResultFile(filename):
    file = open(filename, 'r')
    new_list = [[line in file] for j in range(len(file))]
    file.close()
    return new_list

def checkResultOK(filename, WEIGHTS):
    check = open(filename, 'r')
    for line in check:
        if line[0].count() > 1:
            return False
        elif (line[1:17] < 0) or line[1:17] > 10):
            return False
        elif line[17] != computeScore(line[1:17], WEIGHTS):
            return False
        else:
            return True

def listAll(filename, limitLEtters):
    
