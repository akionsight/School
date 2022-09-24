def sum_and_average(*marks):

    marks_sum = sum(marks)
    if marks_sum < 500:
        marks_average = marks_sum // len(marks)
        return marks_sum, marks_average
    else:
        raise ValueError("The maximum number of marks obtainable in a subject is 100")

def determine_grade(avg):
    if avg >= 91 and avg <= 100:
        return "A+"
    elif avg >= 81 and avg <= 90:
        return "A"
    elif avg >= 71 and avg <= 80:
        return "B+"
    elif avg >= 61 and avg <= 70:
        return "B"
    elif avg >= 51 and avg <= 60:
        return "C+"
    elif avg >= 41 and avg <= 50:
        return "C"
    elif avg >= 33 and avg <= 40:
        return "D"
    else:
        return "E"


maths = int(input("Enter Math Marks: "))
science = int(input("Enter Science Marks: "))
english = int(input("Enter English Marks: "))
social = int(input("Enter marks for SST: "))
french = int(input("Enter marks for French: "))

marks_sum, marks_average = sum_and_average(maths, science, english, social, french)
grade = determine_grade(marks_average)

print(f"The sum of marks is {marks_sum}, the average mark is {marks_average} and the obtained grade is {grade}")
