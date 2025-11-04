# 1
def hello():
	return "Hello, Python!"

# 2
def add(a, b):
	return a + b

# 3
def area_square(side):
	return side * side

# 4
def greet(name):
	return f"Здравей, {name}!"

# 5
def is_even(number):
	return number % 2 == 0

# 6
def greet_with_default(name="Python"):
	return f"Здравей, {name}!"

# 7
def max_num(a, b):
	return a if a >= b else b

# 8
def absolute(x):
	return abs(x)

# 9
def area_rectangle(a, b):
	return a * b

# 10
def is_empty(s):
	return s == "" or s is None

# 11
def average(*args):
	if not args:
		return None
	return sum(args) / len(args)

# 12
def repeat_word(word, n):
	if n <= 0:
		return ""
	return " ".join([str(word)] * n)

# 13
def square(x):
	return x ** 2

# 14
def is_positive(x):
	return x > 0

# 15
def length(s):
	count = 0
	for _ in s:
		count += 1
	return count

# 16
def sub(a, b):
	return a - b

def mul(a, b):
	return a * b

def div(a, b):
	if b == 0:
		raise ZeroDivisionError("division by zero")
	return a / b

def perform_operation(op, a, b):
	ops = {
		"add": add,
		"sub": sub,
		"mul": mul,
		"div": div,
	}
	if op not in ops:
		raise ValueError(f"unknown operation: {op}")
	return ops[op](a, b)

# 17
def is_palindrome(n):
	s = str(n)
	if s.startswith("-"):
		s = s[1:]
	return s == s[::-1]

# 18
def area_triangle(a, h):
	return (a * h) / 2

# 19
def find_min(lst):
	if not lst:
		return None
	minimum = lst[0]
	for v in lst:
		if v < minimum:
			minimum = v
	return minimum

# 20
def count_vowels(s):
	vowels = set("aeiouAEIOUаеиоуяюъАЕИОУЯЮЪ")
	count = 0
	for ch in s:
		if ch in vowels:
			count += 1
	return count

# 21
def factorial(n):
	if n < 0:
		raise ValueError("factorial not defined for negative numbers")
	result = 1
	for i in range(2, n+1):
		result *= i
	return result

# 22
def squares(n):
	if n <= 0:
		return []
	return [i * i for i in range(1, n+1)]

# 23
def is_anagram(a, b):
	clean_a = ''.join(sorted([c.lower() for c in a if c.isalpha()]))
	clean_b = ''.join(sorted([c.lower() for c in b if c.isalpha()]))
	return clean_a == clean_b

# 24
def power(base, exp=2):
	return base ** exp

# 25
def sum_all(*args):
	return sum(args)

# 26
def average_list(lst):
	if not lst:
		return None
	return sum(lst) / len(lst)

# 27
square_lambda = lambda x: x * x

# 28
def contains(lst, x):
	for item in lst:
		if item == x:
			return True
	return False

# 29
counter = 0

def increment_counter():
	global counter
	counter += 1
	return counter

# 30
def reverse_str(s):
	return s[::-1]

# 31
def sequence(a, b, step):
	if step == 0:
		raise ValueError("step must be non-zero")
	result = []
	if step > 0:
		current = a
		while current <= b:
			result.append(current)
			current += step
	else:
		current = a
		while current >= b:
			result.append(current)
			current += step
	return result

# 32
def gcd(a, b):
	a, b = abs(a), abs(b)
	while b:
		a, b = b, a % b
	return a

# 33
def table(n):
	for i in range(1, n+1):
		row = []
		for j in range(1, n+1):
			row.append(str(i * j))
		print("\t".join(row))

# 34
def is_prime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0:
		return False
	i = 3
	while i * i <= n:
		if n % i == 0:
			return False
		i += 2
	return True

# 35
def outer():
	msg = "from outer"
	def inner():
		return f"inner sees: {msg}"
	return inner()

# 36
def filter_even(lst):
	return list(filter(lambda x: x % 2 == 0, lst))

# 37
def sort_by_len(lst):
	return sorted(lst, key=len)

# 38
def describe_person(name, **info):
	result = {"name": name}
	result.update(info)
	return result

# 39
def rec_sum(n):
	if n <= 0:
		return 0
	return n + rec_sum(n-1)

# 40
def rec_reverse(s):
	if s == "":
		return ""
	return rec_reverse(s[1:]) + s[0]

# 41
def map_squares(lst):
	return list(map(lambda x: x * x, lst))

# 42
def all_positive(lst):
	return all(x > 0 for x in lst)

# 43
def letter_counts(text):
	counts = {}
	for ch in text:
		if ch.isalpha():
			key = ch.lower()
			counts[key] = counts.get(key, 0) + 1
	return counts

# 44
def fibonacci_recursive(n):
	if n < 0:
		raise ValueError("negative index not allowed")
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# 45
def calc(a, b):
	quot = None
	if b != 0:
		quot = a / b
	return a + b, a - b, a * b, quot
