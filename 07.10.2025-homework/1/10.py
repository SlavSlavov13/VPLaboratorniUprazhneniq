n = int(input())
a = None
b = None
sum = 0

for i in range(2 * n):
	if i % 2 == 0:
		a = int(input())
	else:
		b = int(input())
		sum += (a%b)

print(sum)