binary_file_read = open("document.bin", "rb")

data = binary_file_read.read(4)

print("Първите 4 байта:")
print(data)

binary_file_read.close()