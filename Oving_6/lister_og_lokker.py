from functools import reduce

number_list = [num for num in range(100)]
print(number_list)

new_list = list(filter(lambda x: x%3 == 0 or x%10 == 0, number_list))
sum_list = reduce(lambda x, y: x+y, new_list)
print(sum_list)

swapped_list = []
for num in number_list:
    if num%2 != 0:
        swapped_list.append(num-1)
    else:
        swapped_list.append(num+1)
print(swapped_list)

reversed_list = []
for num in swapped_list:
    reversed_list.append(swapped_list[99]-(num-1))
print(reversed_list)
