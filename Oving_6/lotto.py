import random
numbers = [num for num in range(1, 35)]
my_guess = [5, 8, 22, 34, 18, 14, 1]
n = 7
premier = [2749455, 102110, 3385, 95, 45]

def drawNumbers(numbers, n):
    seven_list = []
    for i in range(n):
        tilfeldig = random.randint(1, len(numbers)-1)
        seven_list.append(numbers.pop(tilfeldig))
    return seven_list

def compList(numbers, n):
    draw_numbers = drawNumbers(numbers, n)
    correct = 0
    for i in range(len(my_guess)):
        if my_guess[i] in draw_numbers:
            correct += 1
    print(correct)
    bonusNumbers(draw_numbers)

def bonusNumbers(draw_numbers):
    correct = 0
    bonus = 0
    for i in range(5):
        if my_guess[i] in draw_numbers[:5]:
            correct += 1
    for i in range(5, 7):
        if my_guess[i] in draw_numbers[5:]:
            bonus += 1
    if correct == 7:
        return premier[0]
    elif correct == 6 and bonus = 1:
        return premier[1]
    elif correct == 6:
        return premier[2]
    elif correct == 5:
        return premier[3]
    elif correct == 4 and bonus == 1:
        return premier[4]
    else:
        return 'Du vant ikke'
print(compList(numbers, n))
