class MathTools:
	def factorial(self, n):
		if n == 0 or n == 1:
			return 1
		return n * self.factorial(n - 1)

def calculate_factorials(numbers):
	tools = MathTools()
	results = []
	for num in numbers:
		results.append(tools.factorial(num))
	return results

print(calculate_factorials([3, 4, 5]))