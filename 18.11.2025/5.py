import math

def calculate_area(r):
	return math.pi * r * r

class Circle:
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return calculate_area(self.radius)

c = Circle(5)
print(c.area())