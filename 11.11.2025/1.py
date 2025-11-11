class Person:
	def __init__(self, name, family, age, nationality):
		self.name = name
		self.family = family
		self.age = age
		self.nationality = nationality

	def print(self):
		print(f'Hello, {self.name} {self.family}. You are {self.age} years old and your nationality is {self.nationality}.')

class Student(Person):
	def __init__(self, name, family, age, nationality, university, yearofstudy):
		super().__init__(name, family, age, nationality)
		self.university = university
		self.yearofstudy = yearofstudy

	def print(self):
		super().print()
		print(f'You study at {self.university} and you are in year {self.yearofstudy}.')

class Lecturer(Person):
	def __init__(self, name, family, age, nationality, university, experience):
		super().__init__(name, family, age, nationality)
		self.university = university
		self.experience = experience

	def print(self):
		super().print()
		print(f'You teach at {self.university} and you have {self.experience} years of experience.')


PersonBogi = Person("Bogomil", "Georgiev", 19, "Bulgarian")
PersonBogi.print()

print()

StudentAleks = Student("Aleksandar", "Perchinski", 19, "Bulgarian", "Technical University", 1)
StudentAleks.print()

print()

LecturerKami = Lecturer("Kameliya", "Ivanova", 65, "Bulgarian", "Technical University", 23)
LecturerKami.print()
