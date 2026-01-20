#!/usr/bin/python3
print ("This is ICAT3310 Python for Systems Intelligence and Analytics - Python Programming Assignment 2\n")

#Create 3 variables a, b and c (a = your age as a number, b = your full name and c = 1.5)
a = "29"
b = "Sayma Obaida"
c = 1.5

print("\tThis is my age:")
print("\t",a)
print("\t\tThis is my name:")
print("\t\t",b)
print("\n\t\t\tThis is a float:")
print(" \t\t\t", c)

#Create multiple variables e, f, g which has multiple values: Python, Systems/Business Intelligence, Data Analytics.

e = "Python"
f = "Systems/Business Intelligence"
g = "Data Analytics"
print("\n", e, f, g,"\n")

#Create 3 variables h, i, j which has multiple values: h = string, i = your age and j = float 1.5.

h = "string"
i = 29
j = float(1.5)

print(type(h))
print(type(i))
print(type(j),"\n")

#Create string variable k and value for that is your last name.

k= "Obaida"
print(len(k), "\n")

#Create f-string called age = "My age is x". X is variable i from step 6. Embed the variable in the text.
print(f"My age is {i}", "\n" )

#Create variables l and m. l = 0 and m = 1.

l = 0
m = 1

print(l==m)
print(l<m)
