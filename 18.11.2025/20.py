class Person:
	def __init__(self, name):
		self.name = name

class Employee(Person):
	def __init__(self, name, emp_id):
		super().__init__(name)
		self.emp_id = emp_id

class Manager(Employee):
	def __init__(self, name, emp_id, department):
		super().__init__(name, emp_id)
		self.department = department

def print_full_info(obj):
	print(f"Name: {obj.name}")
	if hasattr(obj, 'emp_id'):
		print(f"ID: {obj.emp_id}")
	if hasattr(obj, 'department'):
		print(f"Dept: {obj.department}")

m = Manager("Alice", 101, "HR")
print_full_info(m)