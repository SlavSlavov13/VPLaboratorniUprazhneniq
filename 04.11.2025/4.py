def replace_smaller_numbers_with_zero(numbers: list[int], number: int) -> None:
	if not numbers:
		return []

	for i, num in enumerate(numbers):
		if num > number:
			numbers[i] = 0
	return None
