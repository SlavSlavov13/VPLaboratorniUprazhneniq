class Car:
	def __init__(self, model, year):
		self.model = model
		self.year = year

	def __str__(self):
		return f"Car Model: {self.model}, Year: {self.year}"

def print_car(car):
	print(car)

my_car = Car("Tesla Model S", 2022)
print_car(my_car)