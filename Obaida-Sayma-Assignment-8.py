#!/usr/bin/python3
import mymodule #importing module
#Calling the greeting function from mymodule
mymodule.greeting(mymodule.person1["name"]) #for input value giving it the value from mymodule person1's name
print("Name:", mymodule.person1["name"]) #printing the name from first person
print("Age:",mymodule.person1["age"])
print("Country:", mymodule.person1["country"])

print("\n") # for newline

mymodule.greeting(mymodule.person2["name"]) #for input value giving it the value from mymodule person2's name
print("Name:", mymodule.person2["name"]) #printing the name from first person
print("Age:",mymodule.person2["age"])
print("Country:", mymodule.person2["country"])
print("\n")

import platform #importing platform

print("Platform: ", platform.system()) #printing the name of the system i am using
print("\n")

from numpy import random #importing random function from numpy

x = random.randint(1000) #will pick random int from 0 to 1000
print("My random number is: ", + x)
print("\n")

import pandas

df = pandas.read_csv('visitor_statistics.csv')
print(df)

from scipy import constants
#importing scipy constants and units in seconds
print("\n")
print("Units in seconds: ")
print("Minute: ",constants.minute)
print("Hour: ",constants.hour)
print("Day: ",constants.day)
print("Week: ",constants.week)
print("Year: ",constants.year)

import matplotlib.pyplot as plt #importing matplotlib to show the plot
df.plot() #ploting the csv file
plt.show() #showing the ploted file