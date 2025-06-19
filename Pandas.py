# Step 1: Install Pandas (if not already installed)
# !pip install pandas

# Step 2: Import Pandas
import pandas as pd

# 1. Create the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'HR'],
    'Salary': [45000, 54000, 50000, 62000, 47000]
}

df = pd.DataFrame(data)

# a. Print the first five rows
print("1.a First five rows:")
print(df)

# b. Summary statistics of 'Age' and 'Salary'
print("\n1.b Summary statistics of Age and Salary:")
print(df[['Age', 'Salary']].describe())

# c. Average salary of employees in 'HR' department
avg_salary_hr = df[df['Department'] == 'HR']['Salary'].mean()
print("\n1.c Average salary in HR Department:", avg_salary_hr)

# 2. Add a new column 'Bonus' which is 10% of salary
df['Bonus'] = df['Salary'] * 0.10
print("\n2. DataFrame with Bonus column added:")
print(df)

# 3. Filter employees aged between 25 and 30
filtered_df = df[(df['Age'] >= 25) & (df['Age'] <= 30)]
print("\n3. Employees aged between 25 and 30:")
print(filtered_df)

# 4. Group by 'Department' and calculate average salary
avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
print("\n4. Average salary by Department:")
print(avg_salary_by_dept)

# 5. Sort by 'Salary' in ascending order and save to CSV
sorted_df = df.sort_values(by='Salary', ascending=True)
print("\n5. DataFrame sorted by Salary (ascending):")
print(sorted_df)

# Save to CSV
sorted_df.to_csv("sorted_employees.csv", index=False)
