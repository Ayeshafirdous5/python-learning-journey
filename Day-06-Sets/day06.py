#SETS 
#PART 01  Set Fundamentals
#Exercise 1 — Create a Set
subjects = {"Python", "SQL", "Excel", "Power BI", "Tableau"}
print(subjects)

#Exercise 2 — Duplicate Values
numbers = {10, 20, 10, 30, 20, 40, 10}
print(numbers)

#Exercise 3 — Skills
skills = {"Python", "SQL", "Tableau", "Power BI", "Python"}
print(skills)

#Exercise 4 — Length
cities = {"Hyderabad", "Mumbai", "Delhi", "Bangalore"}
print(len(cities))

#Exercise 5 — Empty Set
students = set()
print(students)

#Exercise 6
data_tools = {"Python", "SQL",  "Power BI", "Tableau", "Python", "SQL"}
print(data_tools)

#Exercise 7 — Set vs List
numbers_list = [10, 20, 30]
numbers_set = {10, 20, 30}
print(numbers_list[0])
#print(numbers_set[0]) It gives error because sets does not support indexing

#Exercise 8 — Unique Employees
employees = {"Ayesha", "Sara", "Ali", "Ayesha", "Sara", "Fatima"}
print(employees)
print(len(employees))

#Exercise 9 — Check the Type
skills = {"Python", "SQL", "Excel"}
print(type(skills))

#Exercise 10 — Real-World Data
technologies = {
    "Python",
    "SQL",
    "Excel",
    "Python",
    "Power BI",
    "SQL",
    "Tableau"
}
print(technologies)
print(len(technologies))