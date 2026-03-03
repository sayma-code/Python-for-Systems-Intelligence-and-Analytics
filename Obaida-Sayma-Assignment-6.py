#!/usr/bin/python3

x = min(1,2,3) #min() function and with values 1, 2 and 3
y = max(5,10,15) # max() function and values 5, 10, 15
print(x)
print(y)

z = abs(-5.00) #abs() function and with value -5.00
print(z)

power = pow(2,3) #pow() function and with value of 2 to the power of 3
print(power)

import math #Importing math module
b = math.sqrt(256) #Creating variable b with math.sqrt() method with value 256
print(b)

c= math.ceil(1.5) #Create variable c with math.ceil() method with value 1.5 
d = math.floor(2.5) #create variable d with math.floor() method with value 2.5
print(c)
print(d)

e = math.pi #e with math.pi constant
print(e)


import json
f = '{ "name":"John Doe", "age":50, "city":"Vaasa" }' #f with JSON content
# parseing f:
parse_f = json.loads(f)

#printing name, age and city
print(parse_f["name"])
print(parse_f["age"])
print(parse_f["city"])

# a Python object (dict) h:
h = { "name":"John Doe", "age":50, "city":"Vaasa" } #Create variable h
# convert into JSON:
i = json.dumps(h)

# the result is a JSON string:
print(i)

import re #importing RegEx module.
txt = "Python for Systems Intelligence and Analytics"   #Create variable txt with string "Python for Systems Intelligence and Analytics".
j = re.findall("Python", txt)#creating variable j with findall("Python", txt) function.
print(j)

k = re.search("Python", txt)#Createing variable k with search("Python", txt) function.
print(k)

l = re.split("\s", txt) #l with split("\s", txt) 
print(l)

m= re.sub("\s", "0", txt) #Create variable m with sub("\s", "0", txt)
print(m)

try:
  print(n)
except:
  print("An exception occurred")
finally:
  print("The Try Except is finished") 