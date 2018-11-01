import random
import math
def make_vec():
    oppgave_liste = []
    for i in range(3):
        tilfeldig_tall = random.randint(-10, 10)
        oppgave_liste.append(tilfeldig_tall)
    return oppgave_liste

def vector_print(vec1):
    vec1.sort()
    return vec1

def liste(vec1, skalar):
    vec1.sort()
    vec1 = [i * skalar for i in vec1]
    return vec1

def vec_len(vec1):
    vec1 = [i * 2 for i in vec1]
    vec_sum = math.sqrt(sum(vec1))
    return vec_sum

def vec_len2(vec2):
    vec1 = [i * 2 for i in vec2]
    vec_sum = math.sqrt(sum(vec2))
    return vec_sum

def vector_dot_product(vec1, vec2):
    vec1.sort()
    vec2.sort()
    vec_sum = [vec1[i] * vec2[i] for i in range(3)]
    return sum(vec_sum)

def main():
    vec1 = make_vec()
    vec1.sort()
    skalar = float(input('Skalar: '))
    vec1_lengde = vec_len(vec1)
    print(vec1_lengde)
    vec2 = liste(vec1, skalar)
    skalar_lengde = vec_len2(vec2)
    print(skalar_lengde)
    print(skalar_lengde - vec1_lengde)
    print(vector_dot_product(vec1, vec2))


vec1 = make_vec()
vec2 = make_vec()

print(vector_print(vec1), 'vec1')
print(liste(vec1, skalar = random.randint(1, 10)))
print(vec_len(vec1))
print('Prikkproduktet av', vec1, 'og', vec2, 'er:', format(vector_dot_product(vec1, vec2),'.3f'))
main()  #main funker så lenge den ikke krasjær pga ugyldig vektor
