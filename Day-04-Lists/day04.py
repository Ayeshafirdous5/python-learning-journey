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