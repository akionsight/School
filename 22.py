unprocessed_list = input('Enter a semicolon (;) seperated list: ')

user_list = unprocessed_list.split(';')
print(f"The current list is {user_list}")
done = False

while not done:
    try: 
        item_to_append = input("Enter a value to append to the list (press Ctrl + C to end the program): ")
        user_list.append(item_to_append)
        print(f"The updated list is {user_list}")
    
    except KeyboardInterrupt:
        print(f"\n\nThe final list is \n")
        print(user_list)
        exit()