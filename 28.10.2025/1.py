import statistics

number_of_students = int(input("Number of dicts in list: "))
list_of_students = []

for i in range(number_of_students):
	name = input("Name: ")
	number_of_grades = int(input("Number of grades: "))
	grades = []

	for j in range(number_of_grades):
		grade = float(input("grade: "))
		if grade < 2 or grade > 6:
			raise ValueError("Grade is not possible.")
		else:
			grades.append(grade)

	average_of_grades = statistics.mean(grades)

	list_of_students.append(
		{
			"name": name,
			"grades": grades,
			"average_of_grades": average_of_grades
		}
	)

sorted_list_of_students = sorted(list_of_students, key=lambda item: item['average_of_grades'], reverse=True)

print("\n--- Students Results ---")
for student in sorted_list_of_students:
	print(f"{student['name']} -> {student['average_of_grades']:.2f}")