set1 = set()
for i in range (20):
    if ((i % 2) != 0):
        set1.add(i)

set2 = set()
for i in range(10):
    if ((i % 2) != 0):
        set2.add(i)

set3 = set1.difference(set2)
set3 = set1-set2

set4 = set1.intersection(set2)
set4 = set2.intersection(set1)
set4 = set1&set2

def allUnique(lst):
    return len(lst) == len(set(lst)):

def removeDuplicates(lst):
    lst = set(lst)
    return list(lst)


print(set1)
print(set2)
print(set3)
print(set4)
print(allUnique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(removeDuplicates([1, 3, 5, 2, 3, 7]))
