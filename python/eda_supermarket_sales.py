import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid')

df=pd.read_excel(r"C:\Users\sheik\supermarket-sales-analysis\excel\cleaned_supermarket_sales.xlsx")

df.shape
df.columns
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.columns=df.columns.str.strip()
print(df.columns)

# top and low performing products
top_products = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
top_products.plot(kind='bar', figsize=(10,5), title='Total Profit by Category')
plt.ylabel("Total Profit")
plt.show()
print("Top 5 Products:\n", top_products.head())
print("\nBottom 5 Products:\n", top_products.tail())

# city wise sales analysis
city_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False)
city_sales.plot(kind='bar', figsize=(10,5), color='coral', title='Total Sales by City')
plt.ylabel("Sales")
plt.xlabel("City")
plt.xticks(rotation=45)
plt.show()

# Region wise sales analysis
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
region_sales.plot(kind='bar', color='skyblue', figsize=(8,5), title='Total Sales by Region')
plt.ylabel("Sales")
plt.xlabel("Region")
plt.xticks(rotation=45)
plt.show()

# Date wise sales Trend
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
daily_sales = df.groupby('Order_Date')['Sales'].sum()
daily_sales.plot(figsize=(12,5), title='Sales Trend Over Time', color='green')
plt.ylabel("Sales")
plt.xlabel("Date")
plt.show()

# Sales by sub_category
subcategory_sales = df.groupby('Sub_Category')['Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,5))
subcategory_sales.plot(kind='bar', color='violet')
plt.title('Sales by Product Sub-Category')
plt.xlabel('Sub-Category')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()