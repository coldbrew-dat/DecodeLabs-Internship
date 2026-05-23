import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("C:\\Users\\K\\Downloads\\DataCleaning_Project\\Cleaned_Dataset.xlsx")
#Ensures the data is clean and ready for analysis
print(df)

#Descriptive statistics
print(df.describe(include='number'))

#Mean 
print("--Mean--")
mean = df.mean(numeric_only=True)
print(mean)

#Median
print("--Median--")
median = df.median(numeric_only=True)
print(median)

#Count non-null values
print("--Count--")
count = df.count()
print(count)

#Standard Deviation
print("--Standard Deviation--")
standard_deviation = df.std(numeric_only=True)
print(standard_deviation)

#Trend Analysis
# Azalyzing trends in sales over time using TotalPrice and Date columns
print("--Trend Analysis--")
df['Date'] = pd.to_datetime(df['Date'])
monthly_sales = df.groupby(df['Date'].dt.month)['TotalPrice'].sum()
print(monthly_sales)


#Checking for outliers using IQR method
print("--Outliers--")
Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['TotalPrice'] < lower_bound) | (df['TotalPrice'] > upper_bound)]
print(outliers)

#Correlation Analysis
print("--Correlation Analysis--")
correlation_matrix = df.corr(numeric_only=True)
print(correlation_matrix)

#Graphical Representation (Use of matplotlib)
#Line graph for monthly sales trend
monthly_sales.plot(kind='line',color = 'green')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

#Histogram for TotalPrice distribution
plt.hist(df['TotalPrice'].dropna(), bins=20, edgecolor='black', facecolor='green')
plt.title('Distribution of Total Price')
plt.xlabel('Total Price')   
plt.ylabel('Frequency')
plt.show()

#Dectecting outliers using box plot
plt.boxplot(df['TotalPrice'])
plt.title('Box Plot of Total Price')
plt.ylabel('Total Price')
plt.show()

#Skewness Analysis
print("--Skewness--")
print(df.skew(numeric_only=True))

# Heatmap for Correlation Matrix
correlation_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='Greens', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()