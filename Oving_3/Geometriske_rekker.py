def oppgaveA():
    r = float(input('r: '))
    n = int(input('n: '))
    i = 0
    total = 0
    while i <= n:
        total = total + (r ** i)
        i += 1
    print(total)

def oppgaveC():
    r = float(input('r: '))
    tol = float(input('tol: '))
    i = 0
    total = 0
    #grense = ((1 - (r ** (n-1)) / (1 - r))
    grense = (1 / (1-r))
    while total <= grense - tol:
        total = total + (r ** i)
        i += 1
    print('Det tok', i, 'løkker og differansen mellom den virkelige og estimerte verdi var', grense-total)

oppgaveC()
