number_of_inputs = int(input("Number of inputs: "))
dictionary = {}

for i in range(number_of_inputs):
	name, phone = input("Name Phone = ").split()
	if name not in dictionary.keys():
		dictionary[name] = [phone]
	else:
		dictionary[name].append(phone)

dictionary = dict(sorted(dictionary.items()))

for key in dictionary.keys():
	print(f"{key} -> {dictionary[key]}")
