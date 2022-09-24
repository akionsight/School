statement = input("Enter your expression: ")
statement = statement.split(' ')

operator = statement[1]

if operator == "+":
    print(f"The sum is {int(statement[0]) + int(statement[2])}")

elif operator == "-":
    print(f"The difference is {int(statement[0]) - int(statement[2])}")

elif operator == "*":
    print(f"The product is {int(statement[0]) * int(statement[2])}")

elif operator == "/":
    print(f"The quotient is {int(statement[0]) / int(statement[2])}")

else:
    print("unrecognized operator")

"""
Enter your expression: 3 + 4
The sum is 7
------------------
Enter your expression: 15 - 10
The difference is 5
-------------------
Enter your expression: 20 * 15
The product is 300
-------------------
Enter your expression 50 / 10
The quotient is 5




"""

