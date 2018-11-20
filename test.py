x = '1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6'
f = (x.split(', '))
print(f[1]+f[2])
print(int(f[1])+int(f[2]))

x = ['1, 2, 3', '1, 2, 3']

y= [item.split(',') for item in x if len(item) ==  7]
print(y)
b = [int(i) for i in y[0] and y[1]]
print(b)
print(sum(b))
z = [1,2,3]
print(sum(z))


#https://www.codewars.com/kata/the-supermarket-queue/train/python
def queue_time(customers, n):
    pass
    if len(customers) == 0:
        return 0

    total_time = 0
    tiles = [0]*n
    for i in range(len(customers)):
        while 0 not in tiles:
            total_time += 1
            tiles[:] = [x - 1 for x in tiles]
        for j in range(len(tiles)):
            if tiles[j] == 0:
                tiles[j] = customers[i]
                total_time += customers[i]
                break
    print(total_time)
    return total_time

a = ['aabb', 'abcd', 'bbaa', 'dada']
result = [i.split(',') for i in a]
result2 = [print(i) for i in result]
print(result)
print(result2)

g = 'Hello'
g_list = [ch for ch in g]
print(g_list)


from datetime import timedelta
year = timedelta(days = 365)
print(year.total_seconds())


list1 = [1, 2, 3, 4, 5]
print(list1)

cool = list(map(lambda x: x*x, list1))
cool = list(map(lambda x: x < 3, list1))
print(cool)
cool = list(filter(lambda x: x < 3, list1))
print(cool)

list2 = ['hei', 'på', 'deg', 1, '.']
cool2 = list(map(lambda y: str(y), list2))
print(cool2)

from functools import reduce
list3 = [1, 5, 6, 3, 9]
cool3 = [reduce(lambda x, y: x+y, list3)]
print(cool3)
