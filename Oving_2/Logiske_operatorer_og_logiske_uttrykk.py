#Logiske uttrykk, 'or' krever kun at 1 av tilfellene er tilstede for å uttrykkes
#'and' krever at begge er tilstede, 'not' blir (uttrykt) true om betingelsen er false
#kan bruke disse istedenfor flere elif eller nøstede if/else

#Presedensregler: not har større presedens enn and, som har større enn or.
#Presedens de som leses først?
def oppgaveA():
    #1. sann, z er større enn -5 og mindre enn 5
    #2. sann, y=8 men resten er ikke
    #3. sann, y=8 og x trenger dermed ikke være det
    #4. usann, x er like stor som 3
    #5. #usann, x+y er lik y-z

def oppgaveB():
    print("Gi inn a og b, begge heltall i intervall <40,50> eller <70,90>:" )
    a = int(input("Verdi for a: "))
    b = int(input("Verdi for b: "))

    if ((b>=70 or b<=90) and (a>=40 and not a>50)) or ((70<=b<=90) and (a>=40 and a<=50)):
        print("Tallene er begge i gyldige intervall ^u^")
    else:
        print("Minst ett av tallene er utenfor et gyldig intervall :(")

def oppgaveC():
    print("Hei! Jeg har 10 pannekaker jeg ønsker å dele med deg ^u^")
    p = int(input("Hvor mange pannekaker ønsker du? "))
    if p>10 or p<0:
        print("Beklager, men det er nok ikke mulig")
    else:
        r = 10-p
        print("Da blir det", p, "på deg og", r, "på med :D")

def oppgaveD():
    print("Hei! Jeg har 10 pannekaker jeg ønsker å dele med deg ^u^")
    p = int(input("Hvor mange pannekaker ønsker du?"))
    s = input("Er du glad i pannekaker? (J/N) ")

    if s == 'J':
        elsker_pannekaker = True
    else:
        elsker_pannekaker = False

    if elsker_pannekaker and (p<=10 or p>= 0):
        r = 10-p
        print("Da blir det", p, "på deg og", r, "på med :D")
    else:
        print("Beklager, men det er nok ikke mulig")
#NOTE fucka opp med å ikke innse raskt nok at elsker_pannekaker blir en ny variabel
#NOTE om jeg har forstått riktig vil variabelen elkser_pannekaker kun aktiveres om True

oppgaveB()
oppgaveC()
oppgaveD()
