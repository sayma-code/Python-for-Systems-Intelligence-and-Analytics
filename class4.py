

#FOr loop in python
oslist = ["Windows", "Mac", "Linux", "FreeBSD"] #This will create a list of operating systems
for x in oslist:  #This will run our os list as soon as we have item
    print(x)
for y in "Windows":  #This will run each letter in the word Windows
    print(y)

#break statement in python
for x in oslist:  #This will run our os list as soon as we have item
    print(x)
    if x == "Linux": #when x is equal to Linux, it will
        break #break the loop