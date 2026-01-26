#!/usr/bin/python3

x = 10
y = 11
if x > y:
    print("x is greater than y")
elif x == y:
    print("x and y are equal")
else:
    print("y is greater than x")
print("\n")
a = 100
b = 50
c = 200

if a > b and c > a:
    print("a and c greater than b")
print("\n")


i = 1
while i <= 10:
    if i == 10:
        print("i is no longer less than 10")
        break
    print(i)
    i += 1
print("\n")
oses = ["Windows 10", "Windows 11", "macOS", "Linux", "BSD"]

for os in oses:
    print(os)
print("Finished!")
print("\n")

oses2 = ["macOS"]

for os in oses:
    if os==oses2[0]:
        break
    print(os)