rainbow = ['Violet', 'Indigo', 'Blue', 'Green', 'Pink', 'Orange', 'Black']

print(rainbow[2::]) ## Blue to EOL

## Removing Pink and replace it with yellow

rainbow.pop(4)
rainbow.insert(4, 'Yellow')

print(rainbow)

## Removing Last colour

rainbow.pop()
print(rainbow)

## Adding red as the last colour
rainbow.append('Red')
print(rainbow)