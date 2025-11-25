import math

def calculate_sqrt():
	try:
		user_input = input("Въведете цяло положително число: ")
		number = int(user_input)

		if number < 0:
			raise ValueError("Negative number")

		result = math.sqrt(number)
		print(f"Корен квадратен: {result}")

	except ValueError:
		print("Invalid Number")
	finally:
		print("Good Bye")

calculate_sqrt()