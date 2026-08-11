# Python Learning Journey - Day 02
# Topic: Variables and Operators

# -----------------------------
# 1. Variable Assignment
# -----------------------------

name = "Ayesha"
age = 21

print(name)
print(age)


# -----------------------------
# 2. Variable Reassignment
# -----------------------------

age = 20
age = 21

print(age)


# -----------------------------
# 3. Multiple Assignment
# -----------------------------

name, age, city = "Ayesha", 21, "Hyderabad"

print(name)
print(age)
print(city)


# -----------------------------
# 4. Swapping Variables
# -----------------------------

a = 5
b = 7

a, b = b, a

print(a)
print(b)


# -----------------------------
# 5. Arithmetic Operators
# -----------------------------

x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)


# -----------------------------
# 6. Comparison Operators
# -----------------------------

salary = 45000

print(salary > 40000)
print(salary < 40000)
print(salary >= 45000)
print(salary <= 45000)
print(salary == 45000)
print(salary != 30000)


# -----------------------------
# 7. Logical Operators
# -----------------------------

age = 25
salary = 50000

print(age >= 18 and salary >= 40000)
print(age >= 18 or salary >= 60000)
print(not(age >= 18))


# -----------------------------
# 8. Assignment Operators
# -----------------------------

total = 100

total += 20
print(total)

total -= 10
print(total)

total *= 2
print(total)

total /= 2
print(total)


# -----------------------------
# 9. Data Analyst Example
# -----------------------------

total_sales = 150000
total_expenses = 120000

profit = total_sales - total_expenses

print("Profit:", profit)
print("Made a profit:", profit > 0)


# -----------------------------
# 10. Monthly Savings
# -----------------------------

monthly_salary = 50000
monthly_expenses = 32000

monthly_savings = monthly_salary - monthly_expenses

print("Monthly Savings:", monthly_savings)


# -----------------------------
# 11. Simple Eligibility Check
# -----------------------------

age = 21
monthly_salary = 50000

eligible = age >= 18 and monthly_salary >= 40000

print("Eligible:", eligible)