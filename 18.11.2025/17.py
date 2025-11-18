import math


class Shape:
	def area(self):
		raise NotImplementedError("Method not implemented")

class Square(Shape):
	def __init__(self, side):
		self.side = side

	def area(self):
		return self.side * self.side

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return math.pi * self.radius * self.radius

def total_area(shapes):
	total = 0
	for s in shapes:
		total += s.area()
	return total

shapes = [Square(2), Circle(1)]
print(total_area(shapes))