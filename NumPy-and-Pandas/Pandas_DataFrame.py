import pandas as pd
import numpy as np

transactions={ "transactions_id" : [101, 102, 103, 104, 105,106,107,108,109,110],
               "productCategory" : ['Electronics', 'Clothing', 'Electronics', 'Furniture',
                                    'Clothing', 'Electronics', 'Furniture', 'Clothing', 'Furniture', 'Electronics'],
               "Region" : ['North', 'South', 'North', 'East', 'West', 'North', 'East', 'West',
'South', 'North'],
          "Amount" : [ 200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
              }
print("Transactions Data:\n", transactions)
print("-------")
df = pd.DataFrame(transactions)
# 2. Data Exploration:
df.info()

print("Head of the data frame ",df.head())
print("Tail of the data frame ",df.tail())
print("Shape of the data frame ",df.shape)
print("Columns of the data frame ",df.columns)
print("data types of the data frame ",df.dtypes)
print()
display=df[['productCategory', 'Amount']]
print("Total Amount by Product Category:\n", display)
retrieved_data_last_3_columns = df.iloc[:, -3:]
print("Retrieved Data (Last 3 Columns):\n", retrieved_data_last_3_columns)
filtered_data = df[(df['Region'] == 'North') & (df['Amount'] > 200)]
print("Filtered Data (Region: North, Amount > 200):\n", filtered_data)
count_values = df['productCategory'].value_counts()
print("Count of each Product Category:\n", count_values)
unique_values = df['Region'].unique()
print("Unique Regions:\n", unique_values)
mean_amount_by_region = df.groupby('Region')['Amount'].mean()
print("mean Amount by Region:\n", mean_amount_by_region)
# 3. Manipulating the DataFrame: 
df.loc[df['transactions_id'] == 102, 'Amount'] = 165
print("Updated Amount for Transaction ID 102:\n", df)
df['Discount'] = df['Amount'] * 0.10
print("DataFrame with Discount Column:\n", df)
df = df[df['transactions_id'] != 109].copy()    
print("DataFrame after removing Transaction ID 109:\n", df)
df.drop('Discount', axis=1, inplace=True)
print("DataFrame after dropping the Discount column:\n", df)
print()
print("final DataFrame:\n", df)
