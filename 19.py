unprocessed_list = input("Enter a list seperated by semicolons (;): ")

user_list = unprocessed_list.split(';')

done = False

while not done:
    try:
        print("Press Ctrl + C to exit\n")
        new_insertion_value = input("Enter a new value to insert into the list: ")
        new_insertion_index = int(input("Enter the index at which you want this value to be inserted: "))

        user_list.insert(new_insertion_index, new_insertion_value)

        print(f'The new list is {user_list}')

    except KeyboardInterrupt:
        print(f"\nThe final list is {user_list}")
        exit()

