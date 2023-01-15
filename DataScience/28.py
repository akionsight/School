import numpy as np 

raw_data = input("Enter a semicolon seperated list of values (;): ")

values = raw_data.split(';')

np_arr = np.array(values)

print(f"The array is \n{np_arr}")
