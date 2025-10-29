list_of_items = input().split(', ')
k = int(input('k = '))
k = k % len(list_of_items)
if k != 0:
	left = list_of_items[-k:]
	right = list_of_items[:len(list_of_items) - k]
	print(left + right)
else:
	print(list_of_items)