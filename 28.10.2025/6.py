text = input("Text: ")

dictionary = {
	"letters": 0,
	"digits": 0,
	"symbols": 0
}

for char in text:
	if char.isalpha():
		dictionary['letters'] += 1
	elif char.isdigit():
		dictionary['digits'] += 1
	elif not char.isspace():
		dictionary['symbols'] += 1

print(dictionary)