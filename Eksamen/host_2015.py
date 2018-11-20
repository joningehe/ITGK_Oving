    #Oppgave 3
    #a)
def readTime():
    hours = int(input('Enter hours: '))
    while not hours < 24:
        print('Error: Hour must be between 0 and 23!')
        hours = input('Enter hours: ')

    minutes = int(input('Enter minutes: '))
    while not minutes < 60:
        print('Error: Minute must be between 0 and 59!')
        minutes = input('Enter minutes: ')

    seconds = int(input('Enter seconds: '))
    while not seconds < 60:
        print('Error: Second must be between 0 and 59!')
        seconds = input('Enter seconds: ')
    print([hours, minutes, seconds])

    #b)
def convertTime(time, mode):
    if str.lower(mode) == 'time':
        return [(time//3600), (time//60%60), (time%60)]
    elif str.lower(mode) == 'sec':
        return (time[0]*60*60) + (time[1]*60) + (time[2])
    else:
        return 'Wrong inputs'

print(convertTime(876543, 'time'))

    #3c)
def timeCalculator():
    hours = int(input('Enter hours: '))
    while not hours < 24:
        print('Error: Hour must be between 0 and 23!')
        hours = input('Enter hours: ')

    minutes = int(input('Enter minutes: '))
    while not minutes < 60:
        print('Error: Minute must be between 0 and 59!')
        minutes = input('Enter minutes: ')

    seconds = int(input('Enter seconds: '))
    while not seconds < 60:
        print('Error: Second must be between 0 and 59!')
        seconds = input('Enter seconds: ')
    return ((hours*3600) + (minutes*60) +(seconds*60))

def travelTime():
    print('Give departure time in hour, minute and second:')
    departure = timeCalculator()
    print('Give arrival time in hour, minute and second:')
    arrival = timeCalculator()
    while arrival < departure:
        print('Error: Arrival time must be later than Departure time.')
        arrival = timeCalculator()
    difference = arrival-departure
    difference_hours = difference//3600
    difference_minutes = difference//60%60
    difference_seconds = difference%60
    print('Traveltime: ', difference_hours, difference_minutes, difference_seconds )

travelTime()

    #3d)
def analyzeBusRoutes(BusTables):
