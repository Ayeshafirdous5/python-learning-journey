#PART 1 TUPLES
#Exercise 1
subjects = ("Python", "SQL", "Excel", "Power BI", "Tableau")
print(subjects)

#Exercise 2 — Access values
print(subjects[0])
print(subjects[2])
print(subjects[4])

#Exercise 3 — Student tuple
student = ("Ayesha", 21, "Hyderabad")
print(student)

#Exercise 4 — Negative indexing
print(student[-1])

#Exercise 5 — Slicing
numbers = (10, 20, 30, 40, 50, 60)
print(numbers[0:3])
print(numbers[-3:])
print(numbers[1:4])

#Exercise 6 — Tuple methods
numbers = (10, 20, 10, 30, 10, 40)
print(numbers.count(10))
print(numbers.index(30))

#Exercise 7 — Immutability
#numbers = (10, 20, 30)
#numbers[0] = 100
#Error because tuple is immutable

#Exercise 8
employee = ("Ayesha", "Data Analyst", 50000, "Hyderabad")
print("Employee name:", employee[0])
print("Job role:", employee[1])
print("Salary:", employee[2])
print("Location:", employee[3])


# PART 2 - TUPLE PACKING AND UNPACKING
# Exercise 9 - Tuple Packing
employee = ("Ayesha", "Data Analyst", 50000)
print(employee)

#Exercise 10 — Tuple Unpacking
employee = ("Ayesha", "Data Analyst", 50000)
name, role, salary = employee
print(name)
print(salary)
print(role)

# Exercise 11 - Unpacking Employee Data
employee = ("Ayesha", "Data Analyst", 50000, "Hyderabad")
name, role, salary, location = employee
print(name)
print(role)
print(salary)
print(location)

# Exercise 12 - Swapping Values
a = 10
b = 20
a, b = b, a
print(a)
print(b)

# Exercise 13 - Unpacking with *
numbers = (10, 20, 30, 40, 50)
first, *remaining = numbers
print(first)
print(remaining)

## Exercise 14 - First and Last Values
data = ("Python", "SQL", "Excel", "Power BI", "Tableau")
first, *middle, last = data
print(first)
print(middle)
print(last)

# Exercise 15
sales_record = ("January", 45000, "Hyderabad")
month, sales, location = sales_record
print(f"Month: {month}")
print(f"Sales: ₹{sales}")
print(f"Location: {location}")

#PART 3 TUPLE OPERATIONS
#Exercise 16 — Length of a Tuple
tools = ("Python", "SQL", "Excel", "Power BI", "Tableau")
print(len(tools))

#Exercise 17 — Check if an Item Exists
subjects = ("Python", "SQL", "Excel", "Power BI")
print("SQL" in subjects)

#Exercise 18 — Check if an Item Does Not Exist
print("Java" not in subjects)

#Exercise 19 — Tuple Concatenation
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
result = tuple1 + tuple2
print(result)

#Exercise 20 — Tuple Repetition
data = ("Python", "SQL")
print(data * 3)

#Exercise 21 — Convert Tuple to List
numbers = (10, 20, 30, 40)
numbers_list = list(numbers)
print(numbers_list)

#Exercise 22 — Convert List to Tuple
cities = ["Hyderabad", "Mumbai", "Delhi"]
cities_tuple = tuple(cities)
print(cities_tuple)
