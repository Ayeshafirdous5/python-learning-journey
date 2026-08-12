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