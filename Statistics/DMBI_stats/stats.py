import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Load your University Data
df = pd.read_csv('Fact_Enrollment.csv')

# 1. Histogram (Frequency of Fees Paid)
plt.figure(figsize=(8, 4))
plt.hist(df['Fees_Paid'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram of Fees Paid')
plt.xlabel('Fees')
plt.ylabel('Frequency')
plt.show()

# 2. Box Plot (Attendance Analysis)
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['Attendance_Percentage'], color='lightgreen')
plt.title('Box Plot of Student Attendance')
plt.show()

# 3. Scatter Plot (Correlation: Attendance vs Fees)
plt.figure(figsize=(8, 4))
plt.scatter(df['Attendance_Percentage'], df['Fees_Paid'], color='red')
plt.title('Scatter Plot: Attendance vs Fees Paid')
plt.xlabel('Attendance %')
plt.ylabel('Fees Paid')
plt.show()

# 4. Quantile Plot (Probability Plot)
plt.figure(figsize=(8, 4))
sm.qqplot(df['Attendance_Percentage'], line='45')
plt.title('Quantile Plot (Q-Q Plot) for Attendance')
plt.show()