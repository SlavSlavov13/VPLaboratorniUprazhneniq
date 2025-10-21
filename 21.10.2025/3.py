text = input("Text: ")
elements_dict = {}

for char in text:
	if char in elements_dict.keys():
		elements_dict[char] += 1
	else:
		elements_dict[char] = 1

for key, value in elements_dict.items():
	print(f"'{key}': {value}")
