def gcd(a, b):
    while b != 0:
        gammel_b = b
        b = a % b
        a = gammel_b
    return a

def oppgaveA():
    a = int(input('a: '))
    b = int(input('b: '))
    print(gcd(a, b))


def reduce_fraction():
    a = int(input('Tall 1: '))
    b = int(input('Tall 2: '))
    d = gcd(a, b)
    print('a =', a, 'og b =', b, 'så d=', int(a/d), '/', int(b/d))

oppgaveA()
reduce_fraction()
