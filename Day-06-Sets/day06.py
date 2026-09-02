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


#Part 2: Set Methods
#Exercise 11 — add()
skills = {"Python", "SQL", "Excel"}
skills.add("Power BI")
print(skills)

#Exercise 12 — update()
skills = {"Python", "SQL"}
skills.update(["Excel", "Tableau", "Power BI"])
print(skills)

#Exercise 13 — remove()
subjects = {"Python", "SQL", "Excel", "Tableau"}
subjects.remove("SQL")
print(subjects)

#Exercise 14 — discard()
tools = {"Python", "Excel", "Power BI"}
tools.discard("Tableau")
print(tools)

#Exercise 15 — remove() vs discard()
skills = {"Python", "SQL", "Excel"}
skills.remove("SQL")
skills.discard("Java")
print(skills)

#Exercise 16 — pop()
numbers = {10, 20, 30, 40, 50}
numbers.pop()
print(numbers)

#Exercise 17 — clear()
employees = {"Ayesha", "Sara", "Ali"}
employees.clear()
print(employees)

#Exercise 18 — copy()
skills = {"Python", "SQL", "Excel"}
backup_skills = skills.copy()
print(skills)
print(backup_skills)

#Exercise 19 — Employee Skills
employee_skills = {"Python", "SQL"}
employee_skills.update(["Power BI", "Tableau", "SQL"])
print(employee_skills)

#Exercise 20
technologies = {
    "Python",
    "SQL",
    "Python",
    "Excel",
    "SQL",
    "Tableau"
}
print(technologies)
technologies.add("Power BI")
technologies.remove("SQL")
technologies.discard("Java")
print(technologies)
print(len(technologies))


#Part 3 — Set Operations
#Exercise 21 — Union
python_skills = {"Python", "Pandas", "NumPy"}
data_skills = {"SQL", "Excel", "Pandas"}
result = python_skills.union(data_skills)
print(result)

#Exercise 22 — Intersection
result = python_skills.intersection(data_skills)
print(result)

#Exercise 23 — Difference
result = python_skills.difference(data_skills)
print(result)

#Exercise 24 — Reverse Difference
result = data_skills.difference(python_skills)
print(result)

#Exercise 25 — Symmetric Difference
result = python_skills.symmetric_difference(data_skills)
print(result)

#Exercise 26 — Union Operator
a = {10, 20, 30}
b = {30, 40, 50}
result = a | b
print(result)

#Exercise 27 — Intersection Operator
result = a & b
print(result)

#Exercise 28 — Subset
basic_skills = {"Python", "SQL"}
all_skills = {"Python", "SQL", "Excel", "Power BI", "Tableau"}
print(basic_skills <= all_skills)

#Exercise 29 — Superset
print(all_skills >= basic_skills)

#Exercise 30 — Disjoint Sets
morning_shift = {"Ayesha", "Sara", "Ali"}
evening_shift = {"Fatima", "Riya", "John"}
print(morning_shift.isdisjoint(evening_shift))


#Part 4: Set Comprehension & Practical Set Usage
#Exercise 31 — Common Skills
employee1 = {"Python", "SQL", "Excel", "Power BI"}
employee2 = {"Python", "Tableau", "SQL", "Java"}
# Find the common skills
result = employee1.intersection(employee2)
print(result)

#Exercise 32 — Unique Skills of an Employee
employee1 = {"Python", "SQL", "Excel", "Power BI"}
employee2 = {"Python", "Tableau", "SQL", "Java"}
result = employee1.difference(employee2)
print(result)

#Exercise 33 — Combine Employee Skills
employee1 = {"Python", "SQL", "Excel"}
employee2 = {"SQL", "Power BI", "Tableau"}
result = employee1.union(employee2)
print(result)

#Exercise 34 — Department Skills
data_team = {"Python", "SQL", "Excel", "Power BI"}
marketing_team = {"Excel", "Tableau", "SQL", "Google Analytics"}
result = data_team | marketing_team
print(result)

#Exercise 35 — Skills Only in One Team
team_a = {"Python", "SQL", "Excel"}
team_b = {"SQL", "Power BI", "Tableau"}
result = team_a.symmetric_difference(team_b)
print(result)

#Exercise 36 — Check Required Skills
required_skills = {"Python", "SQL", "Excel"}
employee_skills = {"Python", "SQL", "Excel", "Power BI", "Tableau"}
print(required_skills.issubset(employee_skills))

#Exercise 37 — Check Candidate Eligibility
required = {"Python", "SQL", "Power BI"}
candidate = {"Python", "SQL", "Excel", "Power BI", "Tableau"}
print(required <= candidate)

#Exercise 38 — Check Superset
required = {"Python", "SQL"}
candidate = {"Python", "SQL", "Excel", "Power BI"}
print(candidate.issuperset(required))

#Exercise 39 — Check for No Common Skills
team_a = {"Python", "SQL", "Excel"}
team_b = {"Java", "C++", "HTML"}
print(team_a.isdisjoint(team_b))

#Exercise 40 — Data Cleaning Using Sets
technologies = [
    "Python",
    "SQL",
    "Python",
    "Excel",
    "Power BI",
    "SQL",
    "Tableau",
    "Excel"
]
unique_technologies = set(technologies)
print(unique_technologies)
print(len(unique_technologies))