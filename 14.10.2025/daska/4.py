number_to_check = int(input('num = '))

for i in range(2, number_to_check):
	if number_to_check % i == 0:
		print('Slojno')
		exit()
if not number_to_check in (0, 1):
	print('Prosto')
else:
	print('Ne moje')
