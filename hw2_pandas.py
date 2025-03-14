import pandas as pd
import numpy as np
# 1.⁠ ⁠From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

filtered_df = df.iloc[::20][['Manufacturer', 'Model', 'Type']]

print(filtered_df)

# 2.⁠ ⁠Replace missing values in Min.Price and Max.Price columns with their respective mean.
# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

df['Min.Price'] = pd.to_numeric(df['Min.Price'])
df['Max.Price'] = pd.to_numeric(df['Max.Price'])

df['Min.Price'] = df['Min.Price'].fillna(df['Min.Price'].mean())
df['Max.Price'] = df['Max.Price'].fillna(df['Max.Price'].mean())

print(df[['Min.Price', 'Max.Price']].head())


# 3.⁠ ⁠How to get the rows of a dataframe with row sum > 100?
# df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

filtered_rows = df[df.sum(axis=1) > 100]

print(filtered_rows)