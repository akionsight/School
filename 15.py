vowels = ['a', 'e', 'i', 'o', 'u']
vowel_counter = 0

sentence = input('Enter a sentence: ')

for charecter in [*sentence]:
    if charecter in vowels:
        vowel_counter += 1
    
print(f"The total number of vowels in that sentence is {vowel_counter}")
