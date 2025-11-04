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

def int_calculator(a: int, b: int, operator: str) -> float:
	if operator == "+":
		return add(a, b)
	elif operator == "-":
		return subtract(a, b)
	elif operator == "*":
		return multiply(a, b)
	elif operator == "/":
		return divide(a, b)
	else:
		raise ValueError("Unknown operator")
