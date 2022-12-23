total_marks = []

no_of_subjects = int(input("Number of subjects: "))

for subject in range(no_of_subjects):
    try:
        marks = int(input("Enter Marks: "))
    except ValueError:
        print("\n value not valid, not counting that one... \n")
        continue

    total_marks.append(marks)


print(f"The highest obtained marks is {max(total_marks)}")    
