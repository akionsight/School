values = input("Enter a semicolon seperated list of values (;): ")

value_list = values.split(';')

items = {}

for value in value_list:
    if value in items.keys():
        items[value] += 1
    else:
        items[value]= 1

for key in items.keys():
    print(f'"{key} appeared {items[key]} time(s)"')
