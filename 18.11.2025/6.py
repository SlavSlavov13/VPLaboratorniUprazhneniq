class TodoList:
	def __init__(self):
		self.tasks = []

def add_task(obj, task):
	obj.tasks.append(task)

todo = TodoList()
add_task(todo, "Buy milk")
add_task(todo, "Learn Python")

for t in todo.tasks:
	print(t)