#!/usr/bin/python3

variable1 = open("demofile.txt", "r") # This will open my file in read mode
print(variable1.read()) # Read the entire file
variable1.close() # Good practice

variable2 = open("demofile.txt", "r") # This will open my file in read mode
print(variable2.read(6)) # Read the first 6 characters of the file
variable2.close() # Good practice

variable3 = open("demofile.txt", "r") # This will open my file in read mode
line = variable3.readlines()
print(line[-2]) # Print the second last line
print(line[-1]) # Read the last line of the file
variable3.close() # Good practice

variable4 = open("demofile.txt", "r") # This will open my file in read mode
print(variable4.readline()) # Read the first line of the file
print(variable4.readline()) # Read the second line of the file
variable4.close()

variable5_write = open("demofile2.txt", "w") # This will create a file named demofile2.txt
variable5_write.write("This is my demofile2.txt") # Write this text to the file
variable5_write.close()

variable5_read = open("demofile2.txt", "r") # Open the file in read mode
data = variable5_read.read()# Read the content of the file
print(data) # Print the content of the file
variable5_read.close() # Good practice

demo_write = open("demofile3.txt", "w")  # Open the destination file in write mode
demo_write.write(data)  # Write the copied content
demo_write.close() # Good practice


with open("demofile3.txt", "w") as f:
  f.write("This is my demofile3.txt")

with open("demofile3.txt") as f:
  print(f.read()) 