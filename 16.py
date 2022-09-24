import string

upper_count = 0
lower_count = 0

charecters = input("Enter a sentence: ")

for charecter in [*charecters]:
    if charecter in string.ascii_lowercase:
        lower_count += 1
    
    elif charecter in string.ascii_uppercase:
        upper_count += 1

print(f"The number of uppercase charecters in the sentence is {upper_count} and the number of lowercase charecters is {lower_count}")
