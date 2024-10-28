from itertools import product

input_list_a = input("Enter number of list A separated by space: ")
input_list_b = input("Enter number of list B separated by space: ")

list_a = list(map(int, input_list_a.split()))
list_b = list(map(int, input_list_b.split()))

list_a.sort()
list_b.sort()

final_list = (list(product(list_a, list_b)))

print(*final_list)
