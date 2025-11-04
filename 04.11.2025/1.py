def area(shape: str) -> float:
	if shape == "квадрат":
		a = float(input("Length a: "))
		b = float(input("Length b: "))
		return a * b
	elif shape == "кръг":
		r = float(input("Radius r: "))
		return 3.14159 * r * r
	elif shape == "прав триъгълник":
		base = float(input("Base: "))
		height = float(input("Height: "))
		return 0.5 * base * height
	else:
		raise ValueError("Unknown shape")