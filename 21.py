unprocessed_list = input("Enter a list seperated by semicolons (;): ")

user_list = unprocessed_list.split(';')

if any(user_list):
    print('The list is not empty')
else:
    print("The list is empty")