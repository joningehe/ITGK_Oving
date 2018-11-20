fasit = ['A', 'C', 'B', 'D', 'A', 'A', 'B', 'A', 'C', 'A', 'D', 'A', 'C', 'C', 'B', 'A', 'B', 'A', 'C', 'D']
def sjekk_svar(studentens_svar, fasit):
    korrekt = 0
    for i in range(len(studentens_svar)):
        if studentens_svar[i] == fasit[i]:
            korrekt += 1
    return ((korrekt/20) * 100)

print(sjekk_svar(fasit, fasit))
