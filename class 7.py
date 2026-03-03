# Read the entire file
a = open("demofile.txt", "r") # This will open my file in read mode
print(a.read()) # Read the entire file
a.close() # Good practice

# Read a part of the file
b = open("demofile.txt", "r") # This will open my file in read mode
print(b.read(5)) # Read the first 5 characters of the file
b.close() # Good practice

# Read one line of the file or multiple lines of the file
c = open("demofile.txt", "r") # This will open my file in read mode
print(c.readline()) # Read the first line of the file
print(c.readline()) # Read the second line of the file
print(c.readline()) # Read the third line of the file
c.close() # Good practice

# WRITING/CREATING FILES
d = open("demofile2.txt", "w") # This will create a file named demofile2.txt
d.write("This is my demofile2.txt") # Write this text to the file
d.close() # Good practice

# Reading the newly created file
e = open("demofile2.txt", "r") # Open the file in read mode
print(e.read()) # Read the content of the file
e.close() # Good practice

# Overwriting the existing content of the file
f = open("demofile2.txt", "w") # Open the file in write mode
f.write("This is my new text in demofile2.txt") # This will overwrite the existing content
f.close() # Good practice

# Reading the overwritten file
g = open("demofile2.txt", "r") # Open the file in read mode
print(g.read()) # Read the content of the file
g.close() # Good practice


# How to add text to the file
h = open("demofile2.txt", "a") # Open the file in append mode
h.write("This text is added to the file.") # This will add text to the end of the file
h.close() # Good practice

# Reading the appended file
i = open("demofile2.txt", "r") # Open the file in read mode
print(i.read()) # Read the content of the file
i.close() # Good practice