from math import sqrt
def divisable(a, b):
    if a % b == 0:
        return True
    else:
        return False

def oppgaveA():
    a = int(input('a: '))
    b = int(input('b: '))
    print(divisable(a, b))

def isPrime():
    a = int(input('a: '))
    b = 2
    for b in range(b, a):
        if divisable(a, b):
            return False
        b += 1
    return True

def isPrime2():
    a = int(input('a: '))
    b = 2
    if a % 2 == 0:
        return False
    else:
        while b < round(sqrt(a) + 0.5):
            if divisable(a, b):
                return False
            b += 1
    return True

print(oppgaveA())
print(isPrime())
print(isPrime2())
