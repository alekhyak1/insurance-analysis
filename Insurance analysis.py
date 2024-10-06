import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from an online source
url = 'https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv'
df = pd.read_csv(url)

# Displaying the first few rows of the dataset and summary statistics
print("Dataset Head:\n", df.head())
print("\nSummary Statistics:\n", df.describe())

# Checking for missing values
print("\nMissing values in the dataset:\n", df.isnull().sum())

# Data Analysis - Average insurance charges per smoking status
average_charges_smoker = df.groupby('smoker')['charges'].mean().reset_index()
print("\nAverage Insurance Charges by Smoking Status:\n", average_charges_smoker)

# Data Analysis - Correlation between age, BMI, and charges
correlation_matrix = df[['age', 'bmi', 'charges']].corr()
print("\nCorrelation Matrix:\n", correlation_matrix)

# Visualizing data - Distribution of insurance charges
plt.figure(figsize=(10,6))
sns.histplot(df['charges'], bins=30, color='skyblue', kde=True)
plt.title('Distribution of Insurance Charges')
plt.xlabel('Insurance Charges ($)')
plt.ylabel('Frequency')
plt.show()

# Visualizing data - Average charges by smoking status
plt.figure(figsize=(8,6))
sns.barplot(x='smoker', y='charges', data=average_charges_smoker, palette='coolwarm')
plt.title('Average Insurance Charges by Smoking Status')
plt.xlabel('Smoker')
plt.ylabel('Average Charges ($)')
plt.show()

# Visualizing data - Correlation heatmap
plt.figure(figsize=(6,4))
sns.heatmap(correlation_matrix, annot=True, cmap='YlGnBu', linewidths=0.5)
plt.title('Correlation Between Age, BMI, and Insurance Charges')
plt.show()