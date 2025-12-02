filename = "document.bin"
text = "This is good"

binary_file = open(filename, mode="wb")

encoded_text = text.encode("ascii")
binary_file.write(encoded_text)

binary_file.close()
print(f"Файлът {filename} е записан успешно.")