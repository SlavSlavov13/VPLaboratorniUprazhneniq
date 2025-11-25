import geometry
import calculator

def main():
	print("--- ИЗБЕРЕТЕ РЕЖИМ ---")
	print("1. Геометрични фигури")
	print("2. Калкулатор")
	choice = input("Вашият избор (1 или 2): ")

	if choice == '1':
		print("\n--- ГЕОМЕТРИЯ ---")
		print("Изберете фигура: 1.Триъгълник, 2.Квадрат, 3.Правоъгълник, 4.Ромб, 5.Трапец")
		shape = input("Избор: ")

		try:
			if shape == '1':
				a = float(input("Страна: "))
				h = float(input("Височина: "))
				print(f"Лицето е: {geometry.triangle_area(a, h)}")
			elif shape == '2':
				a = float(input("Страна: "))
				print(f"Лицето е: {geometry.square_area(a)}")
			elif shape == '3':
				a = float(input("Страна A: "))
				b = float(input("Страна B: "))
				print(f"Лицето е: {geometry.rectangle_area(a, b)}")
			elif shape == '4':
				a = float(input("Страна: "))
				h = float(input("Височина: "))
				print(f"Лицето е: {geometry.rhombus_area(a, h)}")
			elif shape == '5':
				a = float(input("Основа A: "))
				b = float(input("Основа B: "))
				h = float(input("Височина: "))
				print(f"Лицето е: {geometry.trapezoid_area(a, b, h)}")
			else:
				print("Невалиден избор на фигура.")
		except ValueError:
			print("Моля, въвеждайте валидни числа.")

	elif choice == '2':
		print("\n--- КАЛКУЛАТОР ---")
		try:
			num1 = int(input("Първо число: "))
			num2 = int(input("Второ число: "))
			op = input("Операция (+, -, *, /): ")

			if op == '+':
				print(f"Резултат: {calculator.add(num1, num2)}")
			elif op == '-':
				print(f"Резултат: {calculator.subtract(num1, num2)}")
			elif op == '*':
				print(f"Резултат: {calculator.multiply(num1, num2)}")
			elif op == '/':
				print(f"Резултат: {calculator.divide(num1, num2)}")
			else:
				print("Невалидна операция.")
		except ValueError:
			print("Моля, въведете цели числа.")

	else:
		print("Невалиден избор.")

if __name__ == "__main__":
	main()