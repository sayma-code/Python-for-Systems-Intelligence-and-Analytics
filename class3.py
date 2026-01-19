print(1*1)
print(1/1)
#Here we creating a list
oslist = ["Windows", "macOS", "Linux"]

#Here we are creating the tupple
ostuple = ("Windows", "Mac", "Linux")

#Here we are printing tuple
print(ostuple)
#We also can print one items
print(ostuple[0])

#Negative indexing
print(ostuple[-1])

#tuple is unchangable
#We change tuple to list then we change the item then we reverse
oslist = list(ostuple)
oslist[2] = "FreeBSD"
ostuple2 = tuple(oslist)
print(ostuple2)

#sets 

osset = {"Windows", "Mac", "Linux"}
print(osset)

#Add set Items
osset.add("FreeBSD")
print(osset)

#Remove set Items
osset.remove("FreeBSD")
print(osset)

#Discard
osset.discard("Linux")

#Removing random item
a = osset.pop()


#Dictonaries
#In dictonary there is always key:value combination

person = {
    "name": "Jani",
    "age": "18"
}
person2 = {
    "name": "John",
    "age": "65"
}
print(person)
print(person2)
#
person2["age"] = 66

#Add something
person2["favourite_color"] = "red"
print(person2)

#Remove something
person2.pop("age")
print(person2)

#Array
oses = ["Windows", "macOS", "Linux"]
a = oses[0]
print(a)

#Change something
oses[2] = "FreeBSD"
print(oses)

#Calculateing number of elements in the oses array
b = len(oses)
print(b)
