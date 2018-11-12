data = 'Hello World!'
filename = 'my_file.txt'

def write_to_file(data):
    f = open('my_file.txt', 'w')
    f.write(data)
    f.close()

def read_from_file(filename):
    f = open(filename, 'r')
    innhold = f.read()
    print(innhold)
    f.close()

def main():
    while True:
        skriv = input('Vil du skrive til eller lese fra fil (write/read)? ')
        if skriv == 'write':
            write_to_file(data = input('Write: '))
        elif skriv == 'read':
            read_from_file(filename)
        elif skriv == 'done':
            break

write_to_file(data)
read_from_file(filename)
main()
