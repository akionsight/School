values = input("Enter a space seperated list of numbers ")

value_list = values.split(' ')

for index, value in enumerate(value_list): ## Input sanitisation
    try:
        value_list[index] = int(value)
    except ValueError:
        print("\n Invalid string, bailing out! \n")
        exit()


for index, value in enumerate(value_list): ## magic 
    try:
        if value % 5 != 0 and value_list[index + 1] % 5 == 0 and len(value_list) - 1 != index:
            value_list[index] = value_list[index + 1]
            value_list[index + 1] = value

        else:
            continue
    except IndexError: ## This is the best and the worst fix ive ever made 
        continue

print(value_list)