# Step 1: Install Matplotlib (uncomment below if needed)
# !pip install matplotlib

# Step 2: Import Matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 1. Line Plot
x = [1, 2, 3, 4, 5]
y = [10, 15, 25, 30, 50]

# a. Plot the data
plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', linestyle='-', color='blue')

# b. Customize
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# 2. Bar Graph
students = ['John', 'Jane', 'Alice', 'Bob']
marks = [75, 85, 60, 90]

# a. Bar graph
plt.figure(figsize=(6, 4))
plt.bar(students, marks, color=['skyblue', 'orange', 'green', 'purple'])

# b. Customize
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Pie Chart
regions = ['North America', 'Europe', 'Asia', 'Others']
revenue = [45, 25, 20, 10]

# a. Pie chart
explode = [0.1 if rev == max(revenue) else 0 for rev in revenue]  # Highlight the max region

plt.figure(figsize=(6, 6))
plt.pie(revenue, labels=regions, explode=explode, autopct='%1.1f%%', startangle=140, shadow=True)
plt.title("Revenue Distribution by Region")
plt.show()

# 4. Histogram
# Generate 1000 random integers between 1 and 100
random_data = np.random.randint(1, 101, size=1000)

plt.figure(figsize=(6, 4))
plt.hist(random_data, bins=10, color='steelblue', edgecolor='black')
plt.title("Frequency Distribution of Random Integers (1-100)")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

