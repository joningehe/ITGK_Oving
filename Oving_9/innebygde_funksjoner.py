    #Oppgave A
scores = {'Amanda': [88, 92, 100], 'Kennet': [30, 45, 50], 'Einstein': [100,100,100]}
print(scores['Amanda']) #Det printes '[88, 92, 100]'
print(scores['Amanda'][2]) #Det printes '100'


    #Oppgave B
fruit = {}
for frukt in range(3):
    frukt_type = input('Hvilken frukt liker du å spise? ')
    fruit[frukt_type] = int(input('Hvor mange spiser du hver dag? '))
print(fruit)

    #Oppgave C
#kan bare legge på fruit.clear()
for frukt in range(2):
    frukt_type = input('Hvilken frukt misliker du å spise? ')
    fruit[frukt_type] = int(input('Hvor mange spiser du hver dag? '))

for key, value in sorted(fruit.items(), key=lambda item: item[1])[:3]:
    del fruit[key]

print(fruit)

    #Oppgave D
for key, value in fruit.items():
    print(value)

    #Oppgave E
print(fruit)
if 'bananer' in fruit:
    del fruit['bananer']
print(fruit)

    #Oppgave F
fruit['jordbær'] = int(input('Hvor mange jordbær spiser du? '))
fruit['blåbær'] = int(input('Hvor mange blåbær spiser du? '))

for key, value in fruit.items():
    print(key, value)
