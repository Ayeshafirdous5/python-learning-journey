#DAY 07 — Dictionaries
#PART 1: Dictionary Fundamentals
#Exercise 1 — Create a Dictionary 
student = {
    "name": "Ayesha",
    "age": 21,
    "courses": "CSE",
    "city": "Hyderabad"
}
print(student)

#Exercise 2 — Access Values
print(student["name"])
print(student["age"])
print(student["courses"])

#Exercise 3 — Product Data
product = {
    "name": "Laptop",
    "price": 55000,
    "quantity": 2,
    "category": "Electronics"
}
print(product["name"])
print(product["price"])

#Exercise 4 — Dictionary Length
print(len(product))

#Exercise 5 — Check Keys
print("price" in product)
print("brand" in product)

#Exercise 6 — Employee Record
employee = {
    "id": 101,
    "name": "Ayesha",
    "department": "Data Analytics",
    "salary": 45000
}
print(employee["name"])
print(employee["department"])
print(employee["salary"])

#Exercise 7 — Different Data Types
mixed_dict = {
    "name": "Ayesha",
    "age": 20,
    "marks": 95.8,
    "passed": True,
}
print(mixed_dict["name"])
print(mixed_dict["age"])
print(mixed_dict["marks"])
print(mixed_dict["passed"])

#Exercise 8 — Duplicate Values
students = {
    "student1": "CSE",
    "student2": "CSE",
    "student3": "ECE"
}
print(students["student1"])
print(students["student2"])
print(students["student3"])

#Exercise 9 — Nested Data
employee = {
    "name" : "Ayesha",
    "age" : 21,     
    "skills" : ["Python", "SQL", "Power BI"]
}
print(employee)
print(employee["skills"])

#Exercise 10
sales = {
    "product": "Laptop",
    "units_sold": 5,
    "price": 50000,
    "region": "Hyderabad"
}
print(sales["product"])
print(sales["units_sold"])
print(sales["price"])
print(sales["region"])