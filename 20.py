unprocessed_list = input("Enter a semicolon (;) seperated list: ")

user_list = unprocessed_list.split(';')

deduplicated_list = set(user_list) # Remember, elements in a set cannot contain repeated 

print(list(deduplicated_list))
