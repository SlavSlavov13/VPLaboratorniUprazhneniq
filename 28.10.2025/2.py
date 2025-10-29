import string

text = input().lower()
dictionary = {}

for symbol in string.punctuation:
	text = text.replace(symbol, '')

for word in text.split():
	if word not in dictionary.keys():
		dictionary[word] = 1
	else:
		dictionary[word] += 1

print(dictionary)
