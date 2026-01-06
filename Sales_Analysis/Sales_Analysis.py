# import python libraries

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
import seaborn as sns


# Import the sales CSV into a pandas DataFrame
df = pd.read_csv('Sales Data.csv', encoding= 'unicode_escape')


# Display the shape of the DataFrame (rows, columns)
df.shape


# Display the first few rows of the DataFrame
df.head()


# Show information about the DataFrame (column types, non-null counts)
df.info()


# Drop unrelated or blank columns from the DataFrame
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# Check for missing/null values in each column
pd.isnull(df).sum()


# Drop rows that contain any null values
df.dropna(inplace=True)


# Convert the 'Amount' column to integer datatype
df['Amount'] = df['Amount'].astype('int')


# Display the datatype of the 'Amount' column
df['Amount'].dtypes


# List all column names in the DataFrame
df.columns


#rename column
df.rename(columns= {'Marital_Status':'Shaadi'})


# Show summary statistics (count, mean, std, etc.) for numeric columns
df.describe()


# Summary statistics for selected columns: Age, Orders, Amount

df[['Age', 'Orders', 'Amount']].describe()


# Plot the count of records by Gender as a bar chart

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# Plot total sales amount grouped by Gender

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# Plot count of records by Age Group, separated by Gender
ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# Plot total sales amount by Age Group

sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# Show top 10 states by total number of orders and plot them


sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# Show top 10 states by total sales amount and plot them

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# Plot counts for each Marital Status category
ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# Plot sales amount by Marital Status split by Gender
sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# Plot counts of records for each Occupation category
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# Plot total sales amount grouped by Occupation
sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# Plot counts for each Product Category
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# Top 10 product categories by sales amount and plot them
sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# Top 10 products by number of orders and plot them
sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# Plot the top 10 most sold products by orders as a bar chart


fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')

