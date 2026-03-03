#!/usr/bin/python3

def first_function(): # Defining a function
    print("This is my first function in assignment 5\n")
    return #returning nothing in particular
first_function() #calling the function

def second_function(firstname): # Defining a function with parameter
    print(firstname  + "Doe")
    return #returning nothing in particular

second_function("John ") #calling the function with parameter John
second_function("Jane ") #calling the function with parameter Jane

class Person:
    def __init__(self, name, age): #Defining object properties
        self.name = name
        self.age = age

    def printnameage(self): #Defining a method to print name and age
        print(self.name, self.age)


# Creating objects of the Person class
p1 = Person("John", 50)
p2 = Person("Jane", 50)
print("\n")
#printing object properties
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
print("\n")
# Printing name and age using function of the class
p1.printnameage()
p2.printnameage()