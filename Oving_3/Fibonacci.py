def oppgave(): #funker, stygg, men funker, vet ikke hvorfor skitt funker
    k = int(input('k: '))
    a = 0
    b = 1
    i = 0
    sum = 0
    if k == 0:
        print(a)
        print(a)
    elif k == 1:
        print(b)
        print(b)
    else:
        print(a)
        print(b)
        print(b)
        for i in range(k-2):
            a = b - a
            b = a + b
            i += 1
            sum += b
            print(b)
        print(sum+2)

def oppgave2():
    k = int(input('k: '))
    a = 0
    b = 1
    i = 0
    sum = 0
    for i in range(k):
        if i == 0:
            print (a)
        elif i == 1:
            print (b)
        else:
            a = b - a
            b = a + b
            i += 1
            sum += b
            print(b)
    print(sum)

oppgave()
