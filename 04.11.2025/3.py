def add(a: int, b: int) -> int:
	return a + b

def subtract(a: int, b: int) -> int:
	return a - b

def multiply(a: int, b: int) -> int:
	return a * b

def divide(a: int, b: int) -> int:
	if b == 0:
		raise ValueError("Division by zero is not allowed.")
	return a // b

def int_calculator(a: int, b: int, operator: str) -> None:
	if operator == "+":
		print(add(a, b))
	elif operator == "-":
		print(subtract(a, b))
	elif operator == "*":
		print(multiply(a, b))
	elif operator == "/":
		print(divide(a, b))
	else:
		raise ValueError("Unknown operator")
