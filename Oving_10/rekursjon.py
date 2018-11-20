def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + (recursive_sum(n-1))

print(recursive_sum(53))

def fakultet(n):
    if n == 1:
        return 1
    else:
        return n *(fakultet(n-1))

print(fakultet(5))

def find_smallest_element(numbers):
    if len(numbers) == 1:
        return numbers[0]

    if numbers[0] < find_smallest_element(numbers[1:]):
        return numbers[0]
    else:
        return find_smallest_element(numbers[1:])

print(find_smallest_element([5,3,2,6]))


def binary_search(numbers, element):
    
    if numbers[0] == element:
        return 0
    else:
        binary_serch(numbers)

    else:
        return -float('inf')


print(binary_search([1,4,6,9,13,34,45,53,65,78],53))
