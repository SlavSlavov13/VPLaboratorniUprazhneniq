class Robot:
	count = 0

	def __init__(self):
		Robot.count += 1

def create_robots(n):
	for _ in range(n):
		Robot()
	return Robot.count

total = create_robots(5)
print(total)