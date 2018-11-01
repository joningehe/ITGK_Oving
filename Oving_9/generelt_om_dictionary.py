my_family = {}
name_list_bror = []
name_list_soster = []

def add_family_member(role, name):
    global name_list
    if role == 'bror':
        name_list_bror.append(name)
        my_family[role] = name_list_bror
        return my_family
    elif role == 'søster':
        name_list_soster.append(name)
        my_family[role] = name_list_soster
        return my_family
    else:
        my_family[role] = name
        return my_family

for i in range(int(input('Skriv inn antall familiemedlemmer: '))):
    add_family_member(role = input('Skriv inn familierolle: '), name = input('Skriv inn navn på familiemedlem: '))

print(my_family)

#Stygg måte å skrive det på, kan prøve å bruke 'if key in dict', må derimot legge alt til i lister i såfall og ikke bare bror og søster, se mer på denne
