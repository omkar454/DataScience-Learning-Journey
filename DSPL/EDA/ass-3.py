# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv('loan.csv')
print("Dataset Loaded Successfully. Shape:", df.shape)

# ---------------------------------------------------------
# Q1: Identify the most frequent values for all categorical features
# ---------------------------------------------------------
print("\n--- Q1: Most Frequent Values for Categorical Features ---")
categorical_cols = df.select_dtypes(include=['object']).columns
most_frequent = df[categorical_cols].mode().iloc[0]
print(most_frequent)

# ---------------------------------------------------------
# Q2: Give descriptive statistics of numerical features in the dataset.
# ---------------------------------------------------------
print("\n--- Q2: Descriptive Statistics (Before Imputation) ---")
print(df.describe())
# Comment: The distribution of 'ApplicantIncome' and 'CoapplicantIncome' shows a high 
# standard deviation and a massive difference between the 75th percentile and the max value, 
# indicating a heavy right skew and the presence of significant outliers.

# ---------------------------------------------------------
# Q3: Replace the missing values in categorical features using appropriate techniques.
# ---------------------------------------------------------
# Replacing missing categorical values with the mode (Pandas 3.0 Safe Method)
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])
print("\n--- Q3: Missing values in categorical features filled with Mode ---")

# ---------------------------------------------------------
# Q4: Demonstrate various encoding techniques for categorical features.
# ---------------------------------------------------------
# Technique 1: Label Encoding (for binary/ordinal categories)
le = LabelEncoder()
df['Gender_Encoded'] = le.fit_transform(df['Gender'])
df['Married_Encoded'] = le.fit_transform(df['Married'])
df['Education_Encoded'] = le.fit_transform(df['Education'])

# Technique 2: One-Hot Encoding (for nominal categories > 2 distinct values)
# Applying get_dummies replaces the original 'Property_Area' column with binary columns
df = pd.get_dummies(df, columns=['Property_Area'], drop_first=True)

print("\n--- Q4: Encoding Applied (Label Encoding & One-Hot Encoding) ---")
print("1. Label Encoding Results (Gender & Education):")
print(df[['Gender', 'Gender_Encoded', 'Education', 'Education_Encoded']].head(3))

print("\n2. One-Hot Encoding Results (Property_Area):")
# We use df.filter to automatically grab and print the newly created OHE columns
print(df.filter(regex='Property_Area').head(3))

# ---------------------------------------------------------
# Q5: For numerical features, replace missing values
# ---------------------------------------------------------
# a. Using simple imputer (Pandas 3.0 Safe Method)
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())

# b. Using random sample imputation (Applying to Loan_Amount_Term using .loc)
random_sample = df['Loan_Amount_Term'].dropna().sample(df['Loan_Amount_Term'].isnull().sum(), random_state=0)
random_sample.index = df[df['Loan_Amount_Term'].isnull()].index # Match indices
df.loc[df['Loan_Amount_Term'].isnull(), 'Loan_Amount_Term'] = random_sample

# Simple imputer for Credit_History (Pandas 3.0 Safe Method)
df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])

print("\n--- Q5: Missing numerical values imputed successfully ---")

# ---------------------------------------------------------
# Q6: Give descriptive statistics of numerical features after handling missing values.
# ---------------------------------------------------------
print("\n--- Q6: Descriptive Statistics (After Imputation) ---")
print(df.describe())
# Comment: After imputation, the count for all numerical columns is uniform. The median 
# of LoanAmount remains stable, proving median imputation is robust to outliers.

# ---------------------------------------------------------
# Q7: Data Visualizations
# ---------------------------------------------------------
sns.set_style("whitegrid")

# a & b. Plot histogram for Loan Amount
plt.figure(figsize=(8, 4))
sns.histplot(df['LoanAmount'], bins=30, kde=True, color='blue')
plt.title('Histogram of Loan Amount Distribution')
plt.xlabel('Loan Amount (in thousands)')
plt.ylabel('Frequency')
plt.show()
# Observation: The Loan Amount is right-skewed, with most loans clustering between 
# 100 and 150. A long tail extends to the right due to a few very large loans.

# c. Bar graph showing income for graduate and non-graduate applicant
plt.figure(figsize=(8, 4))
sns.barplot(x='Education', y='ApplicantIncome', data=df, palette='Set2')
plt.title('Average Applicant Income by Education Level')
plt.xlabel('Education Level')
plt.ylabel('Average Applicant Income')
plt.show()
# Observation: Graduates significantly earn higher average incomes compared to 
# Non-Graduates, though the error bars indicate higher variance in Graduate incomes.

# d. Plot the boxplot for Loan amount & Five-number summary
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['LoanAmount'], color='lightgreen')
plt.title('Boxplot of Loan Amount')
plt.xlabel('Loan Amount (in thousands)')
plt.show()

print("\n--- Q7d: Five-Number Summary for Loan Amount ---")
five_num = df['LoanAmount'].describe()[['min', '25%', '50%', '75%', 'max']]
print(five_num)

# e. Comment on the correlation between Applicant's income and Loan amount
plt.figure(figsize=(8, 4))
sns.scatterplot(x='ApplicantIncome', y='LoanAmount', data=df, alpha=0.6, color='purple')
plt.title('Correlation: Applicant Income vs Loan Amount')
plt.xlabel('Applicant Income')
plt.ylabel('Loan Amount')
plt.show()
# Observation: There is a positive correlation; as Applicant Income increases, the 
# requested Loan Amount generally increases. However, the data points are densely 
# concentrated at lower income levels.

# f. Descriptive statistics (Correlation Matrix for Numerical Features)
plt.figure(figsize=(8, 6))
numerical_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']
sns.heatmap(df[numerical_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Numerical Features')
plt.show()
# Comment: The highest numerical correlation exists between ApplicantIncome and LoanAmount. 
# Credit History shows virtually no correlation with the income metrics.