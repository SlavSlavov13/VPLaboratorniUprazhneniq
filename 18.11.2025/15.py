class Author:
	def __init__(self, name):
		self.name = name

class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author

def search_books(books, author_name):
	found_books = []
	for book in books:
		if book.author.name == author_name:
			found_books.append(book.title)
	return found_books

a1 = Author("Stephen King")
a2 = Author("Isaac Asimov")
b1 = Book("It", a1)
b2 = Book("Foundation", a2)
b3 = Book("The Shining", a1)

print(search_books([b1, b2, b3], "Stephen King"))