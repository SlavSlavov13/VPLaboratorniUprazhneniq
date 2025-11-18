class Calculator:
	def sum_all(self, *args):
		return sum(args)

def calculate_sum(calc, *numbers):
	return calc.sum_all(*numbers)

my_calc = Calculator()
print(calculate_sum(my_calc, 1, 2, 3, 4, 5))