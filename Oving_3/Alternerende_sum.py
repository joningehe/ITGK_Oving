def oppgaveA():
    n = int(input('n: '))
    i = 0
    sum = 0
    for i in range (n+1):
        a = i ** 2
        if a % 2 == 0:
            suma = (-a)
        else:
            suma = a
        sum += suma
    print(sum)

def oppgaveB(): #funker ikke, se på
    k = int(input('k: '))
    i = 0
    sum = 0
    a = i ** 2
    while a < k:
        a = i ** 2
        if a % 2 == 0:
            suma = (-a)
        else:
            suma = a
        sum += suma
        i += 1
    print(sum, i)

oppgaveA()
