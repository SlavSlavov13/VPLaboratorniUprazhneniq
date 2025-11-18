class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height

def is_bigger(rect1, rect2):
	if rect1.area() > rect2.area():
		return rect1
	return rect2

r1 = Rectangle(10, 5)
r2 = Rectangle(4, 4)
bigger = is_bigger(r1, r2)
print(bigger.area())