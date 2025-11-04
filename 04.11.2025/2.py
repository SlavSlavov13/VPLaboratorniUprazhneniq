def is_palindrome(number: int) -> int:
	number = str(number)
	number = number.replace("-", "")
	return 1 if number == number[::-1] else 0
