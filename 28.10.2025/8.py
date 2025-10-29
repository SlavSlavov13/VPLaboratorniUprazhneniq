import string

text = input("Text: ")
for symbol in string.punctuation:
	text = text.replace(symbol, '')

list_of_words = text.split()

dictionary = {}

for word in list_of_words:
	length = len(word)

	if length not in dictionary.keys():
		dictionary[length] = [word]
	else:
		dictionary[length].append(word)

print(dictionary)
