import pandas as pd

print("---Exercise 1---")

df = pd.read_csv('data/messy_sales.csv')

df.info()
print(df.isnull().sum())

# 1 - Unit price is a string when it should be a float.
# 2 - Customer ID is missing 7.5% of the values.
# 3 - Order date is a string when it should be a datetime.

print("---Exercise 2---")

df.columns = df.columns.str.lower().str.replace(' ', '_')

print(df.columns.tolist()) 