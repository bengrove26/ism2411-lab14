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

print("---Exercise 3---")

print("Shape before:", df.shape)

# Drop rows missing order_id or order_date because they are essential and we can't guess them.
df = df.dropna(subset=['order_id', 'order_date'])

# Fill missing quantity_sold with the mean because we can assume that the missing values are random and not related to any other variable.
df['quantity_sold'] = df['quantity_sold'].fillna(df['quantity_sold'].mean())

print("Shape after:", df.shape)
print(df.isnull().sum())

print("---Exercise 4---")

df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
print("Dates that became NaT:", df['order_date'].isna().sum())

df['unit_price'] = (
    df['unit_price']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)

df['quantity_sold'] = df['quantity_sold'].round().astype(int)

df['revenue'] = (df['unit_price'] * df['quantity_sold']).round(2)

print(df.dtypes)

print("---Exercise 5---")

print("Duplicates before:", df.duplicated().sum())
df = df.drop_duplicates()
print("Shape after:", df.shape)

print("---Exercise 6---")

print(df.describe())

# 1 One suspicious stat is the max quantity sold is 9999 which is so much higher than the 75% quantile of 7. A business explanation for this is that it is probably just a place holder value for a missing value.
# 2 Another suspicious stat is the min revenue of -3268. This could potentally be a refund or a return, but it could also be a input error. 

df = df[df['quantity_sold'] != 9999]
print("Shape after dropping 9999s:", df.shape)
print(df.describe())

# I am dropping this row because it is only one row and most likely an input error or place holder value. 

print("---Exercise 7---")

df.to_csv('data/clean_sales.csv', index=False)

check = pd.read_csv('data/clean_sales.csv')
check.info()

check = pd.read_csv('data/clean_sales.csv', parse_dates=['order_date'])
check.info()