num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operator = input("Enter an operator: ")

if operator not in ['+', "-", "*", "/"]:
    print("Invalid operator")
    

else:
    if operator == "+":
        print(f"The sum is {num1 + num2}")

    elif operator == "-":
        print(f"The difference is {num1 - num2}")

    elif operator == "*":
        print(f"The product is {num1 * num2}")

    elif operator == "/":
        print(f"The quotient is {num1 / num2}")

"""
Enter a number: 20
Enter another number: 45
Enter an operator: #
Invalid Operator

----------------------

Enter a number: 20
Enter another number: 45
Enter an operator: +
The sum is 65

-------------------
Enter a number: 20
Enter another number: 45
Enter an operator: -
The difference is -25
-------------------
Enter a number: 20
Enter another number: 45
Enter an operator: *
The product is 900
------------------------
Enter a number: 20
Enter another number: 45
Enter an operator: /
The sum is 0.444444

"""