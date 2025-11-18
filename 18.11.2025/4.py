class Student:
	def __init__(self, name, major="CS"):
		self.name = name
		self.major = major

	def info(self):
		print(f"Student: {self.name}, Major: {self.major}")

def create_student(name):
	return Student(name)

s1 = create_student("Maria")
s1.info()