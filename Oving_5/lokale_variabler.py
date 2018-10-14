def oppgaveA():
    pass
    #kodesnutt 1 har en feil i cakes() siden variabelen cake blir called før den er definert
    #kodesnutt 2 har en feil siden cupcake er lokal variabel som blir called i en annen funksjon enn der hvor den er definert i
    #kodesnutt 3 har ingen variabel cake

def oppgaveB():
    def funksjon1(x, y):
        num = x // y
        return(num)

    def funksjon2(x):
        num = x ** 2
        return(num)

    x = int(input('Skriv inn x: '))
    y = int(input('Skriv inn y: '))
    num = funksjon1(x, y)
    print('Helltallsdivisjon av', x, 'over', y, 'gir', num)
    x = int(input('Skriv inn x: '))
    num = funksjon2(x)
    print('Kvadratet av', x, 'er', num)

oppgaveB()

#C, nei, den siste verdien til variabelen vil overskrive den andre, fører kun til problem om koden ikke er strukturert riktig
