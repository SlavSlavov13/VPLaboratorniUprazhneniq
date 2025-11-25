def read_file_content(filename):
	try:
		with open(filename, 'r', encoding='utf-8') as f:
			content = f.read()
			return content
	except FileNotFoundError:
		return "Грешка: Файлът не е намерен."
	except PermissionError:
		return "Грешка: Нямате права за четене на този файл."
	except Exception as e:
		return f"Възникна неочаквана грешка: {e}"

file_name = input("Въведете име на файла: ")
print(read_file_content(file_name))