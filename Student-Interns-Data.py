# Data Loading and Preprocessing
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "Data analyst Data.xlsx"
data = pd.read_excel(file_path)

# Display the first few rows of the data
data.head()


# Basic Questions

# 1. How many unique students are included in the dataset?
# Number of unique students
unique_students = data["Email ID"].nunique()
print(f"Number of unique students: {unique_students}")
# Answer: Number of unique students: 41

# 2. What is the average GPA of the students?
# Average GPA
average_gpa = data["CGPA"].mean()
print(f"Average GPA of students: {average_gpa:.2f}")
# Answer: Average GPA of students: 7.59

# 3. What is the distribution of students across different graduation years?
# Distribution of students across graduation years
graduation_year_distribution = data["Year of Graduation"].value_counts()
print(
    "Distribution of students across different graduation years:\n",
    graduation_year_distribution,
)
# Answer:
# Distribution of students across different graduation years:
# 2024    26
# 2025     9
# 2023     6
# Name: Year of Graduation, dtype: int64

# 4. What is the distribution of students' experience with Python programming?
# Distribution of student's experience with python programming
python_experience_distribution = (
    data["Experience with python (Months)"].value_counts().sort_index()
)
print(
    "Distribution of students' experience with Python programming:\n",
    python_experience_distribution,
)
# Answer:
# Distribution of students' experience with Python programming:
# 1     1
# 2     5
# 3     7
# 4     4
# 5     5
# 6     7
# 7    12
# Name: Experience with python (Months), dtype: int64

# 5. What is the average family income of the students?
# Mapping for family income categories to numeric values
income_mapping = {"0-2 Lakh": 1, "2-5 Lakh": 3.5, "5-7 Lakh": 6, "7 Lakh+": 7.5}

# Applying the mapping
data["Family Income Numeric"] = data["Family Income"].map(income_mapping)

# Calculating average family income
average_family_income = data["Family Income Numeric"].mean()
print(f"Average family income of the students (in Lakhs): {average_family_income:.2f}")
# Answer: Average family income of the students (in Lakhs): 4.63

# 6. How does the GPA vary among different colleges? (Show top 5 results only)
# GPA variation among different colleges
gpa_by_college = (
    data.groupby("College Name")["CGPA"].mean().sort_values(ascending=False).head(5)
)
print("Top 5 colleges by average GPA:\n", gpa_by_college)
# Answer:
# Top 5 colleges by average GPA:
# College Name
# St Xavier's College                                        9.100000
# Pillai College of Engineering New Panvel                   8.700000
# Thakur College of Engineering and Technology Kandivali     8.650000
# Tata Institute of Social Sciences                          8.500000
# AP SHAH INSTITUTE OF TECHNOLOGY                            8.200000
# Name: CGPA, dtype: float64

# 7. Are there any outliers in the quantity (number of courses completed) attribute?
# Checking for outliers in the 'Quantity' column
Q1 = data["Quantity"].quantile(0.25)
Q3 = data["Quantity"].quantile(0.75)
IQR = Q3 - Q1

# Outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Detecting outliers
outliers = data[(data["Quantity"] < lower_bound) | (data["Quantity"] > upper_bound)]
print(f"Number of outliers in Quantity: {outliers.shape[0]}")
outliers
# Answer: Number of outliers in Quantity: 0 (No outliers)

# 8. What is the average GPA for students from each city?
# Average GPA by city
gpa_by_city = data.groupby("City")["CGPA"].mean().sort_values(ascending=False)
print("Average GPA for students from each city:\n", gpa_by_city)
# Answer:
# Average GPA for students from each city:
# City
# Patna         9.100000
# Tirupati      8.700000
# Pune          8.650000
# Ahmedabad     8.500000
# Bengaluru     8.200000
# Amravati      8.000000
# Hyderabad     7.900000
# Ludhiana      7.800000
# Mumbai        7.700000
# Gurgaon       7.500000
# Indore        7.300000
# Lucknow       7.000000
# Kanpur        7.000000
# Surat         7.000000
# Jaipur        6.700000
# Jodhpur       6.700000
# Delhi         6.700000
# Meerut        6.500000
# Nagpur        6.500000
# Noida         6.500000
# Chennai       6.500000
# Visakhapatnam 6.500000
# Vijaywada     6.500000
# Name: CGPA, dtype: float64

# 9. Can we identify any relationship between family income and GPA?
# Scatter plot to show the relationship between Family Income and GPA
sns.scatterplot(data=data, x="Family Income Numeric", y="CGPA")
plt.xlabel("Family Income (in Lakhs)")
plt.ylabel("GPA")
plt.title("Relationship between Family Income and GPA")
plt.show()
# Answer: The scatter plot shows a slight positive correlation between family income and GPA.


# Moderate Questions

# 10. How many students from various cities? (Solve using a data visualization tool).
# Bar plot of number of students from various cities
city_counts = data["City"].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=city_counts.index, y=city_counts.values, palette="viridis")
plt.xticks(rotation=45)
plt.xlabel("City")
plt.ylabel("Number of Students")
plt.title("Number of Students from Various Cities")
plt.show()
# Answer: The bar plot provides a visual distribution of students across different cities.

# 11. How does the expected salary vary based on factors like 'GPA', 'Family income', 'Experience with Python (Months)'?
# Pair plot to show the relationship between GPA, Family Income, Experience with Python, and Expected Salary
sns.pairplot(
    data,
    vars=[
        "CGPA",
        "Family Income Numeric",
        "Experience with python (Months)",
        "Expected salary (Lac)",
    ],
    diag_kind="kde",
    kind="scatter",
)
plt.show()
# Answer: The pair plot shows the relationships between various factors affecting the expected salary.

# 12. Which event tends to attract more students from specific fields of study?
# Events attracting more students from specific fields of study
events_by_college = (
    data.groupby(["College Name", "Events"]).size().unstack(fill_value=0)
)
print(
    "Events attracting more students from specific fields of study:\n",
    events_by_college,
)
# Answer: The table shows the number of students from each college participating in different events.

# 13. Do students in leadership positions during their college years tend to have higher GPAs or better expected salaries?
# Comparing GPA and Expected Salary for students with and without leadership skills
leadership_gpa_salary = data.groupby("Leadership- skills")[
    ["CGPA", "Expected salary (Lac)"]
].mean()
print(
    "Comparison of GPA and Expected Salary for students with/without leadership skills:\n",
    leadership_gpa_salary,
)
# Answer:
# Comparison of GPA and Expected Salary for students with/without leadership skills:
#                   CGPA  Expected salary (Lac)
# Leadership- skills
# No                 7.40                  6.96
# Yes                7.73                  7.14

# 14. How many students are graduating by the end of 2024?
# Number of students graduating by the end of 2024
students_graduating_2024 = data[data["Year of Graduation"] <= 2024][
    "Email ID"
].nunique()
print(f"Number of students graduating by the end of 2024: {students_graduating_2024}")
# Answer: Number of students graduating by the end of 2024: 32

# 15. Which promotion channel brings in more student participation for the event?
# Promotion channel with more student participation
promotion_channel_counts = data[
    "How did you come to know about this event?"
].value_counts()
print("Promotion channel participation:\n", promotion_channel_counts)
# Answer:
# Promotion channel participation:
# College     26
# Friends      9
# Internet     6
# Name: How did you come to know about this event?, dtype: int64

# 16. Find the total number of students who attended the events related to Data Science.
# Total number of students who attended Data Science-related events
data_science_events = data[
    data["Events"].str.contains("Data Science", case=False, na=False)
]
total_data_science_students = data_science_events["Email ID"].nunique()
print(
    f"Total number of students who attended Data Science-related events: {total_data_science_students}"
)
# Answer: Total number of students who attended Data Science-related events: 16

# 17. Those who have high CGPA & more experience in language tend to have high expectations for salary (Avg)?
# High CGPA and more experience in language with high expected salary
high_cgpa_experience = data[
    (data["CGPA"] >= 8) & (data["Experience with python (Months)"] >= 6)
]
high_cgpa_experience_avg_salary = high_cgpa_experience["Expected salary (Lac)"].mean()
print(
    f"Average expected salary for students with high CGPA and more experience: {high_cgpa_experience_avg_salary:.2f}"
)
# Answer: Average expected salary for students with high CGPA and more experience: 9.63

# 18. How many students know about the event from their colleges? Which of these are the Top 5 colleges?
# Students who know about the event from their colleges
college_promotion_students = data[
    data["How did you come to know about this event?"] == "College"
]
top_5_colleges = college_promotion_students["College Name"].value_counts().head(5)
print("Top 5 colleges where students know about the event:\n", top_5_colleges)
# Answer:
# Top 5 colleges where students know about the event:
# College Name
# Amity University Noida           3
# Indian Institute of Technology   3
# Pillai College of Engineering    3
# Sathyabama Institute of Science  3
# St Xavier's College              2
# Name: College Name, dtype: int64
