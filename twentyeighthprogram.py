#List Exercises

# 1. Make an empty list. Append Input as List element.
#Since Lists are mutable, change the lists elements that are given as output.

# Creating a List
List = []
print("List: ")
print(List)
List.append('b')
print(List)

# creating an empty list
a = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    b = int(input())

    a.append(b) # adding the element

print(a)

#Mutable lists

#a = [12, 35, 9, 56, 24]
print(a)
a[0] = 24
print(a)

#2.	Find the length of list [1, 4, 5, 7, 8]

# Initializing list
m = len([1, 4, 5, 7, 8])

# Printing the list
print ("The list is : " + str(m))
# Printing the length of the list
print ("The length of the string is: ", m)

#3.	Make an empty list. Append “Geeks” ,“ Are”, “For”, “Geeks” in a list. Then print the length of the list like “ the length of list is …”

p = []
p.append("Geeks")
p.append("Are")
p.append("For")
p.append("Geeks")
print("The length of list is: ", len(p))

#4.	Given two numbers, write a Python code to find the Maximum and min of these two numbers.

# Python program to find the maximum of two numbers

a = 2
b = 4

maximum = max(a, b)
print(maximum)

# Python program to find the minimum of two numbers


a = -1
b = -4

minimum = min(a, b)
print(minimum)
