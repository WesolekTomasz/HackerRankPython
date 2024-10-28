from collections import Counter

number_of_pairs = input("pairs number: ")
shoes_numbers = input("shoes numbers: ")
i = 0
clients = int(input("clients: "))

while i < clients:
    pay_list = list(map(int, input("shoes number, cost ").split()))
    i =+ 1

shoes_numbers = list(map(int, shoes_numbers.split()))

salary = 0

print(Counter(shoes_numbers))
print(pay_list)