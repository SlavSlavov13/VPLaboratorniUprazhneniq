n = int(input('n = '))

# max_num = float('-inf')
#
# for i in range(n):
# 	x = int(input('num = '))
# 	if x > max_num:
# 		max_num = x
#
# print(max_num)

list_of_nums = []
for i in range(n):
	list_of_nums.append(int(input()))

print(max(list_of_nums))