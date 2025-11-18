class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def display_info(self):
		print(f"Name: {self.name}, Age: {self.age}")

def create_person(name, age):
	return Person(name, age)

person = create_person("Ivan", 25)
person.display_info()