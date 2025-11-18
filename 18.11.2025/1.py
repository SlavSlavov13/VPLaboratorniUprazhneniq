class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author

def print_book_info(book):
	print(f"Title: {book.title}, Author: {book.author}")

book1 = Book("1984", "George Orwell")
book2 = Book("Harry Potter", "J.K. Rowling")

print_book_info(book1)
print_book_info(book2)