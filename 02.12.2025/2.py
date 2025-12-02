with open("test_read.txt", "w", encoding="utf-8") as f:
	f.write("Ред 1: Здравей\n")
	f.write("Ред 2: Това е тест\n")
	f.write("Ред 3: Python програмиране\n")

my_file = open("test_read.txt", "r", encoding="utf-8")

print("Съдържание на файла:")
for line in my_file:
	print(line.strip())

my_file.close()