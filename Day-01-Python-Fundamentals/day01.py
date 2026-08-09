#Exercise 1
print("Hello, I'm Ayesha Firdous\nI'm learning Python\nI want to become a Data Analyst")

#Exercise 2
name = "Ayesha Firdous"
age = 20
city = "Hyderabad"
print(name)
print(age)
print(city)

#Exercise 3
product_name = "Pencils"
price = 5
quantity = 7
total_price = price * quantity
print(total_price)

#Exercise 4
print(type(name))
print(type(age))

#Exercise 5
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("Hello %s, you are %d years old and you live in %s" % (name,age,city))

#CHALLENGE
python_marks = int(input("Enter your python marks: "))
excel_marks = int(input("Enter your excel marks: "))
sql_marks = int(input("Enter your sql marks: "))
average_marks = (python_marks + excel_marks + sql_marks) / 3
print(average_marks)