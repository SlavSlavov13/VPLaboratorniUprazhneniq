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
		result = add(a, b)
	elif operator == "-":
		result = subtract(a, b)
	elif operator == "*":
		result = multiply(a, b)
	elif operator == "/":
		result = divide(a, b)
	else:
		raise ValueError("Unknown operator")

	print(result)
