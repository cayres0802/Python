import pandas as pd

i = {'Student':['David', 'Samuel', 'Terry', 'Evan'], 'Age':[27, 24, 22, 32], 'Country':['UK', 'Canada', 'China', 'USA'], 
     'Course':['Python', 'Data Structures', 'Machine Learning', 'Web Development'], 'Marks':[85, 72, 89, 76]}
df = pd.DataFrame(i)
# print(df)

# b = df[['Marks']]
# print(b)

# c = df[['Country', 'Course']]
# print(c)

df.iloc[0, 0]