class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Employee(Person):
	def __init__(self, name, age, salary):
		super().__init__(name, age)
		self.salary = salary

def find_highest_salary(employees):
	if not employees:
		return None
	highest = employees[0]
	for emp in employees:
		if emp.salary > highest.salary:
			highest = emp
	return highest

emps = [Employee("A", 30, 1000), Employee("B", 40, 2000), Employee("C", 35, 1500)]
rich = find_highest_salary(emps)
print(rich.name)