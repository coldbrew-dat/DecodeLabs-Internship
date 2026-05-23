import pandas as pd 
df = pd.read_excel('C:\\Users\\K\\Downloads\\DataCleaning_Project\\Dataset for Data Analytics.xlsx')
print(df.info())

# Check for missing values
print("--Missing Values--")
print(df.isnull().sum())

#Filling missing Values 
df['CouponCode'] = df['CouponCode'].fillna('No Coupon').str.title()


#Check for duplicates
print("--Duplicate Values--")
print(df.duplicated().sum())

#Dropping/Removing Duplicates 
df = df.drop_duplicates()

#DateTime Formatting
df['Date'] = pd.to_datetime(df['Date']).dt.date

#Numeric Data Data Type Conversion
df['Quantity'] = df['Quantity'].astype(int)
df['UnitPrice'] = df['UnitPrice'].astype(float)
df['TotalPrice'] = df['TotalPrice'].astype(float)

#Clean text columns
df['Product'] = df['Product'].str.strip()
df['PaymentMethod'] = df['PaymentMethod'].str.strip()
df['OrderStatus'] = df['OrderStatus'].str.strip()

#Saved the cleaned dataset to a new Excel file
df.to_excel('Cleaned_Dataset.xlsx', index=False)
print("Data cleaning completed.")
 
#Checking the count of missing values after cleaning
print("--Missing Values After Cleaning--")
print(df.isnull().sum())
