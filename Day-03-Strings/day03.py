#Exercise 1
name = "Ayesha"
print(name)
print(len(name))

#Exercise 2
first_name = "Ayesha"
last_name = "Firdous"
full_name = first_name +" " + last_name
print(full_name)

#Exercise 3
name = "Ayesha"
print(name[0])
print(name[2])
print(name[5])

#Exercise 4
print(name[-1])
print(name[-2])

#Exercise 5
#name[0] = "B"
#When you run this it gives an errro because strings are immutable
#Once a string is created, its individual characters cannot be changed directly.

#Exercise 6
employee_name = "Ayesha Firdous"
employee_id = "DA102"
department = "Data Analytics"
print("Employee: %s, ID: %s, Department: %s" % (employee_name,employee_id,department))


# -----------------------------
# PART 2 - STRING SLICING
# -----------------------------

# Exercise 7
name = "Ayesha"
print(name[0:3])
print(name[3:])
print(name[:3])
print(name[:])

#Exercise 8 — Negative slicing
name = "Ayesha"
print(name[-3:])
print(name[:-3])

#Exercise 9 — Step
word = "PYTHON"
print(word[0:6:2])
print(word[0:6:3])

#Exercise 10 — Reverse
word = "PYTHON"
print(word[0:6:2])
print(word[0:6:3])



# --------------------------------
# PART 3 - STRING METHODS
# --------------------------------

# Exercise 11 - upper() and lower()

name = "Ayesha"
print(name.upper())
print(name.lower())


# Exercise 12 - strip()

name = "   Ayesha Firdous   "
print(name.strip())
print(name.lstrip())
print(name.rstrip())


# Exercise 13 - replace()

city = "Hyderabad"
print(city.replace("Hyderabad", "Mumbai"))


# Exercise 14 - find() and count()

text = "banana"
print(text.find("a"))
print(text.count("a"))


# Exercise 15 - startswith() and endswith()

employee_id = "EMP102"
email = "ayesha@gmail.com"
print(employee_id.startswith("EMP"))
print(email.endswith(".com"))


# Exercise 16 - split()

name = "Ayesha Firdous"
print(name.split())


# Exercise 17 - join()

names = ["Ayesha", "Firdous"]
print(" ".join(names))


# Exercise 18 - checking strings

print("Ayesha".isalpha())
print("12345".isdigit())
print("Ayesha21".isalnum())