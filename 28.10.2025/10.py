import statistics

number_of_subjects = int(input("Number of dicts in list: "))
list_of_subjects = []

for i in range(number_of_subjects):
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

	list_of_subjects.append(
		{
			"subject_name": name,
			"grades": grades,
			"average_of_grades": average_of_grades
		}
	)

sorted_list_of_students = sorted(list_of_subjects, key=lambda item: item['average_of_grades'], reverse=True)

print("\n--- Best Average Result ---")
best_subject = sorted_list_of_students[0]
print(f"{best_subject['subject_name']} -> {best_subject['average_of_grades']:.2f}")
