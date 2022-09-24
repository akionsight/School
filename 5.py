def check_if_number_is_valid(num) -> bool:
    if num <= 0:
        return False
    return True


num1 = int(input("Enter a number: "))
if not check_if_number_is_valid(num1): 
    print("Enter a valid number")
    exit()

num2 = int(input("Enter another number: "))

if not check_if_number_is_valid(num2):
    print("Enter a valid number")
    exit()

print(f"The sum of the numbers is {num1 + num2}")

"""
Enter a number: -20
Enter a valid number 

------------------

Enter a number: 40
Enter another number = -233
Enter a valid number

---------------

Enter a number: 40
Enter another number: 50
The Sum of the numbers is 90



"""