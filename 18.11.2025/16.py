class Student:
	def __init__(self, name, grade):
		self.name = name
		self.__grade = grade

	@property
	def grade(self):
		return self.__grade

	@grade.setter
	def grade(self, value):
		if 2 <= value <= 6:
			self.__grade = value
		else:
			print("Error")

def update_grades(students, new_grade):
	for s in students:
		s.grade = new_grade

s_list = [Student("Ivan", 3), Student("Ana", 4)]
update_grades(s_list, 6)
print(s_list[0].grade)