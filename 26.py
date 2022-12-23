from collections import Counter

values = input("Enter a space seperated list values: ")

value_list = values.split(' ')

for index, value in enumerate(value_list): ## Input sanitisation
    try:
        value_list[index] = int(value)
    except ValueError:
        continue

count = Counter(value_list)

for key in count.keys():
    print(f'"{key}" has been used {count[key]} time(s)') ## hello