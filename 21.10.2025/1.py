number = input("Number: ")

straight = tuple(int(digit) for digit in number)
backward = straight[::-1]

print(straight)
print(backward)
