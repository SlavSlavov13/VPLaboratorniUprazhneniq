number_of_items = int(input("Number of items: "))
list_of_items = []
dictionary = {}

for i in range(number_of_items):
	item = input("Name: ")
	price = float(input("Price: "))

	list_of_items.append((item, price))

for tup in list_of_items:
	name, price = tup

	if name not in dictionary.keys():
		dictionary[name] = price
	else:
		dictionary[name] += price

print(dictionary)
