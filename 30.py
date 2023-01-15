import pandas as pd 

unsorted_info = {
    'Name': ['Anil', 'Bhavna', 'Chirag','Dhara', 'Giri'],
    'Score': [25, 20, 22, 23, 21],
    'Attempts': [1, 2, 2, 1, 1],
    'Qualified': [True, False, True, True, False]
}

dataframe = pd.DataFrame(unsorted_info, index=['C001', 'C002', 'C003', 'C004', 'C005'])

print(dataframe)
