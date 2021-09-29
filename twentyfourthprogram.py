#Q4. Python program to find the circumference and area of a circle with a given radius

#Method 1
PI = 3.14
radius = float(input(' Please Enter the radius of a circle: '))

diameter = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius

print(" Diameter Of a Circle = ", diameter)
print(" Circumference Of a Circle = ", circumference)
print(" Area Of a Circle = ", area)

#Method 2
import math

def find_Diameter(radius):
    return 2 * radius

def find_Circumference(radius):
    return 2 * math.pi * radius

def find_Area(radius):
    return math.pi * radius * radius

r = float(input(' Please Enter the radius of a circle: '))

diameter = find_Diameter(r)
circumference = find_Circumference(r)
area = find_Area(r)

print("\n Diameter Of a Circle = %.2f" %diameter)
print(" Circumference Of a Circle = %.2f" %circumference)
print(" Area Of a Circle = %.2f" %area)

#Q5. Python program to check whether the given integer is a multiple of 5

num = int(input("Enter an integer: "))
if(num%5==0):
    print(num, "is a multiple of 5")
else:
    print(num, "is not a multiple of 5")

#Q6. Assign a value of 5 to variable num. Use if statement to print “No. is smaller than 10” if it is and always print “This statement will always be executed” after if statement

num = 5;
if(num<10):
    print("Number is smaller than 10")

print("this statement will always be executed")


#Q7. Ask the user two inputs, “passing_score” and “my_score”. Use if statement to print “Congratulations! You have passed your exam” if passing score is more than or equal to 60 or else print “you need to work hard”

pass_score=int(num("Enter the passing score: "))
my_score=int(num("Enter my marks: "))
if(my_score>=pass_score):
    print("Congratulations, you have passed your exam!")
else:
    print("You need to work hard!!!")


#Q8. Assign a value of 5 to variable “num”. Print if statements to print “number is positive” if “num” is and print “number is less than 10” if it is also there,

num = 5
if(num > 10):
    print("Number is positive")
else:
    print("Number is negative")

print("number is less than 10")




#Q9. Take an input from user for any number in ‘n’. Check in nested if loop, first condition: n is not equal to 0
#Second condition: n is greater than 0. If both conditions satisfies Print “Number is greater than Zero”

k = int(num("Enter a number: "))
if(k! = 0):
    if(k > 0):
        print("Number is positive.")
    else:
        print("Number is negative.")
else:
    print("Number is greater than zero")



#Q10. Multiple conditions using “And” :Take inputs of three different nos. num1, num 2 and num3 from the user. Print “All the conditions are true” if num1 is 10, num 2 is 20 and num 3 is 30

a = int(num("Enter the first number: "))
b = int(num("Enter the second number: "))
c = int(num("Enter the third number: "))
if(a == 10 && b == 20 && c == 30):
    print("All the conditions are true")



#Q11. Multiple conditions using “or” :Take inputs of a fruitName from the user. Print ““It’s a fruit”” if the fruitName is either Mango or Apple or Grapes

a = input("Enter the fruit name"))
if(a == "Mango" || a == "Apple" || a == "Grapes"):
    print("It's a fruit")
