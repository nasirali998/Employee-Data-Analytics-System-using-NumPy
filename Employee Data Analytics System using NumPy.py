import numpy as np

# ==========================================
# EMPLOYEE DATA ANALYTICS SYSTEM USING NUMPY
# ==========================================

print("=" * 50)
print("      EMPLOYEE DATA ANALYTICS SYSTEM")
print("=" * 50)

# Employee Names
employees = np.array(["Ali", "Ahmed", "Sara", "Ayesha", "Zain"])

# Employee Data
# Columns:
# Salary | Performance | Experience

employee_data = np.array([
    [50000, 85, 2],
    [65000, 90, 4],
    [80000, 95, 6],
    [45000, 75, 1],
    [70000, 88, 4]
])

print("\nEmployee Dataset:\n")
print(employee_data)

print("\nEmployee Names:")
print(employees)

# Basic Information
print("\n========== DATA INFORMATION ==========")

print("Shape        :", employee_data.shape)
print("Dimension    :", employee_data.ndim)
print("Total Elements :", employee_data.size)
print("Data Type    :", employee_data.dtype)
# ==========================================
# SALARY ANALYSIS
# ==========================================

# Salary Column
salary = employee_data[:, 0]

print("\n========== SALARY ANALYSIS ==========")

print("All Salaries :", salary)

# Total Salary
total_salary = np.sum(salary)
print("Total Salary :", total_salary)

# Average Salary
average_salary = np.mean(salary)
print(f"Average Salary : {average_salary:.2f}")

# Highest Salary
highest_salary = np.max(salary)
print("Highest Salary :", highest_salary)

# Lowest Salary
lowest_salary = np.min(salary)
print("Lowest Salary :", lowest_salary)

# Highest Paid Employee
highest_index = np.argmax(salary)

print("\nHighest Paid Employee")
print("Name   :", employees[highest_index])
print("Salary :", salary[highest_index])

# Lowest Paid Employee
lowest_index = np.argmin(salary)

print("\nLowest Paid Employee")
print("Name   :", employees[lowest_index])
print("Salary :", salary[lowest_index])

# Salaries in Ascending Order
print("\nAscending Salaries :")
print(np.sort(salary))

# Salaries in Descending Order
print("\nDescending Salaries :")
print(np.sort(salary)[::-1])
# ==========================================
# PERFORMANCE ANALYSIS
# ==========================================

# Performance Column
performance = employee_data[:, 1]

print("\n========== PERFORMANCE ANALYSIS ==========")

print("Performance Scores :", performance)

# Average Performance
average_performance = np.mean(performance)
print(f"Average Performance : {average_performance:.2f}")

# Highest Performance
highest_performance = np.max(performance)
print("Highest Performance :", highest_performance)

# Lowest Performance
lowest_performance = np.min(performance)
print("Lowest Performance :", lowest_performance)

# Best Performer
best_index = np.argmax(performance)

print("\nBest Performer")
print("Name  :", employees[best_index])
print("Score :", performance[best_index])

# Lowest Performer
lowest_index = np.argmin(performance)

print("\nLowest Performer")
print("Name  :", employees[lowest_index])
print("Score :", performance[lowest_index])

# Performance Scores in Ascending Order
print("\nAscending Performance Scores :")
print(np.sort(performance))

# Performance Scores in Descending Order
print("\nDescending Performance Scores :")
print(np.sort(performance)[::-1])
# ==========================================
# EMPLOYEE FILTERING & CLASSIFICATION
# ==========================================

# Experience Column
experience = employee_data[:, 2]

print("\n========== EMPLOYEE FILTERING ==========")

# High Salary Employees (> 60000)
print("\nEmployees with Salary > 60000")
print(salary[salary > 60000])

# High Performance Employees (>= 90)
print("\nPerformance >= 90")
print(performance[performance >= 90])

# Experienced Employees (>= 3 Years)
print("\nExperience >= 3 Years")
print(experience[experience >= 3])

# Salary Between 50000 and 70000
print("\nSalary Between 50000 and 70000")
print(salary[(salary >= 50000) & (salary <= 70000)])

# Salary < 50000 OR Performance >= 90
print("\nSalary < 50000 OR Performance >= 90")
print(employee_data[(salary < 50000) | (performance >= 90)])

# ==========================================
# EMPLOYEE CLASSIFICATION
# ==========================================

print("\n========== EMPLOYEE CLASSIFICATION ==========")

salary_status = np.where(
    salary >= 70000,
    "High Salary",
    "Normal Salary"
)

print("Salary Category:")
for name, status in zip(employees, salary_status):
    print(f"{name:<10} : {status}")

# ==========================================
# UNIQUE EXPERIENCE
# ==========================================

print("\n========== UNIQUE EXPERIENCE ==========")

print("Experience Years:")
print(np.unique(experience))
# ==========================================
# PROFESSIONAL EMPLOYEE REPORT
# ==========================================

print("\n")
print("=" * 50)
print("        PROFESSIONAL EMPLOYEE REPORT")
print("=" * 50)

print(f"{'Employee':<10} {'Salary':<10} {'Performance':<12} {'Experience'}")
print("-" * 50)

for i in range(len(employees)):
    print(f"{employees[i]:<10} {salary[i]:<10} {performance[i]:<12} {experience[i]}")

print("-" * 50)