# DAY 04 - LISTS
# PART 1 - LIST FUNDAMENTALS

# Exercise 1 Create a list
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits)

# Exercise 2 Different types
student_information = ["Ayesha", "20", "Hyderabad","8.67"]
print(student_information)

#Exercise 3 — Access items
cities = ["Hyderabad", "Mumbai", "Delhi", "Chennai"]
print(cities[0])
print(cities[1])
print(cities[3])

#Exercise 4 — Change an item
marks = [85, 90, 78, 92, 88]
marks[2] = 80
print(marks)

#Exercise 5 - Length
employees = ["Ayesha", "Sara", "Ali", "Fatima", "Ahmed"]
print(len(employees))

#Exercise 6 
sales = [12000, 15000, 18000, 11000, 22000]
print(f"Sales data: {sales}")
print(len(sales))


# PART 2 - LIST METHODS
#Exercise 7 — append
fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
print(fruits)

#Exercise 9 — extend
numbers = [1, 2, 3]
numbers.extend([4,5,6])
print(numbers)

#Exercise 10 — remove
employees = ["Ayesha", "Sara", "Ali", "Fatima"]
employees.remove("Ali")
print(employees)

#Exercise 11 — pop
marks = [85, 90, 78, 92, 88]
marks.pop(2)
print(marks)

#Exercise 12 — sort
sales = [12000, 45000, 18000, 30000, 15000]
sales.sort()
print(sales)
sales.sort(reverse=True)
print(sales)

#Exercise 13 — count + index
numbers = [10, 20, 10, 30, 10, 40]
print(numbers.count(10))
print(numbers.index(30))


# -----------------------------
# PART 3 - LIST SLICING & OPERATIONS
# -----------------------------
# Exercise 14 - Basic slicing
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print(fruits[0:3])

# Exercise 15 - Start omitted
print(fruits[:3])

# Exercise 16 - End omitted
print(fruits[2:])

# Exercise 17 - Negative slicing
print(fruits[-3:])

# Exercise 18 - Step
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[0:6:2])

# Exercise 19 - Reverse using slicing
print(numbers[::-1])

# Exercise 20 - Copy
sales = [10000, 20000, 30000]
sales_copy = sales.copy()
print(sales_copy)

# Exercise 21 - Membership
employees = ["Ayesha", "Sara", "Ali", "Fatima"]
print("Ayesha" in employees)
print("Rahul" in employees)
print("Rahul" not in employees)

#PART 4
#Exercise 22 — nested list
students = [
    ["Ayesha", 21],
    ["Sara", 22],
    ["Ali", 20]
]
print(students)

#Exercise 23 — Access inner lists
print(students[0][0])
print(students[0][1])
print(students[1][0])
print(students[1][1])
print(students[2][0])
print(students[2][1])

#Exercise 24 — Access individual values
print(students[0][0])
print(students[0][1])
print(students[1][0])
print(students[2][1])

#Exercise 25 — Modify nested data
students = [
    ["Ayesha", 21],
    ["Sara", 22],
    ["Ali", 20]
]
students[1][1] = 23
print(students)

#Exercise 26 — Sales data 
sales = [
    ["January", 45000],
    ["February", 52000],
    ["March", 48000],
    ["April", 60000]
]
print(sales[0][1])
print(sales[2][1])
print(sales[3][1])

#Exercise 27 — Employee data
employees = [
    ["Ayesha", "Data Analyst", 50000],
    ["Sara", "Developer", 60000],
    ["Ali", "Tester", 45000]
]
print(employees[0][1])
print(employees[1][2])
print(employees[2][0])

#Exercise 28 — Length
print(len(employees))
print(len(employees[0]))
print(len(employees[1]))
print(len(employees[2]))