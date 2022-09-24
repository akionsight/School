unprocessed_list = input("Enter a semicolon (;) seperated list: ")

user_list = unprocessed_list.split(';')

deduplicated_list = set(user_list) # A set cannot contain repeted 

print(list(deduplicated_list))