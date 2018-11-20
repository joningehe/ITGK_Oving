list1 = [[1 for i in range(5)] for i in range(92)]
list2 = [[5 for i in range(5)] for j in range(92)]
list3 = [[10 for i in range(5)] for j in range(92)]

sumlist = [[sum(x) for x in zip(list1[i], list3[i], list2[i])] for i in range(len(list1))]

#total = [0, 0, 0, 0, 0]
#for i in range(len(list1)):
#    for j in range(len(total)):
#        list2[i][j] += list1[i][j]
#print(list2)

total1 = list(map(lambda x: x+1, list1[0]))
print(total1)


for i in range(len(list1)):
    list3[i] = list(map(lambda x,y: x+y, list1[i], list2[i]))
print(list3)

whatnow = list(map(lambda x: [x+10 for x in range(len(list1[0]))], list1))
print(whatnow)


a = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x+1, a[3:])))

b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c = [10, 10, 10, 10, 10, 10, 10, 10, 10]
sum = sum(b[i]*c[i] for i in range(len(b)))/100
