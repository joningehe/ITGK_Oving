from turtle import*
def oppgaveA():
    for i in range(4):
        forward(100)
        left(90)

def oppgaveB():
    for i in range(16, 0, -3):
        pensize(i)
        forward(50)

def oppgaveC():
    spiraler = 4*(int(input('Hvor mange runder i spiralen? (maks 9)')))
    for i in range(spiraler):
        ny_lengde = 250-(7*i) #i vil her starte som 0 siden spiral starter på 0 og øker til 4*input
        if ny_lengde <= 0:
            break
        else:
            forward(ny_lengde)
            left(90)

def oppgaveD():
    antall_kanter = int(input('Hvor mange kanter ønsker du i polygonet? '))
    omkrets = int(input('Hvor stor omkrets skal polygonet ha? '))
    vinkel = (360 / antall_kanter)
    lengde = (omkrets / antall_kanter)
    for i in range(antall_kanter):
        forward(lengde)
        left(vinkel)

def oppgaveE(): # se på senere
    antall_kanter = int(input('Hvor mange kanter ønsker du i polygonet? '))
    omkrets = int(input('Hvor stor omkrets skal polygonet ha? '))
    vinkel = (360 / antall_kanter)
    lengde = (omkrets / antall_kanter)
    for i in range(antall_kanter):
        forward(lengde)
        left(vinkel)

oppgaveE()
