n = int(input('n = '))

for number in range(1, n + 1):
	sum_of_digits = 0
	for digit in str(number):
		sum_of_digits += int(digit)
	if sum_of_digits in (5, 7 ,11):
		print(f'{number} -> True')
	else:
		print(f'{number} -> False')
