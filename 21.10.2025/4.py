number = int(input("Number: "))
list_of_nums_for_key = []
dictionary = {}

for num in range(1, number + 1):
	list_of_nums_for_key.append(num)

list_of_nums_for_value = list(reversed(list_of_nums_for_key))

for i in range(len(list_of_nums_for_key)):
	dictionary[list_of_nums_for_key[i]] = list_of_nums_for_value[i]

for key, value in dictionary.items():
	print(f'{key}: {value}')
