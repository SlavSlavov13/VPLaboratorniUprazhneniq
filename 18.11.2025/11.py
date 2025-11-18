class Animal:
	def sound(self):
		pass

class Dog(Animal):
	def sound(self):
		print("Bark")

class Cat(Animal):
	def sound(self):
		print("Meow")

class Cow(Animal):
	def sound(self):
		print("Moo")

def make_all_sounds(animals):
	for animal in animals:
		animal.sound()

zoo = [Dog(), Cat(), Cow()]
make_all_sounds(zoo)