import time
from turtle import *

pensize(2)              #setter pennen 2 piksler tykk
pencolor("purple")      #setter pennefargen til lilla
bgcolor("yellow")       #setter bakgrunnsfargen til gul
hideturtle()            #skjuler pila

def halfPetal():        #lager et halvt blomsterblad
    forward(50)
    left(30)
    forward(75)
    left(30)
    forward(50)
    left(120)

def petal():            #lager et helt blomsterblad
    for i in range(2):
        halfPetal()

def simpleFlower(blad):
    i = 0
    for i in range(blad):
        petal()
        left(360/blad)
        i += i

for i in range(4):
    simpleFlower(blad = int(input('Hvor mange blad vil du ha? ')))
    left(45)

time.sleep(10)
