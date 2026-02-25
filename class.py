print("Hello World")
#divya
# This is single line comment 

print("Divya")

#Variable
a=10 #integer 
b="StudyGlance" #string 
c=12.5 #float 
print(a) 
print(b) 
print(c)

a = 15
b = "DivyaAswini"
print(a)
print(b)


#type casting
a=int(3)
b=int(34.5)
c=float(2.0)
d=str(10)
print(a); print(b)
print(c/2); print(d)

#operators
#arithmetic operator
x=12; y=2
print(x+y)
print(x-y)
print(x/y)
print(x%y)
print(x*y)
print(x//y)
print(x**y)

#comparision 

#program-day1
print("Hello World")
print("Welcome to Python Programming")

name=input("Enter your name:")
print("Hello",name)

name = input("Enter name: ")
age = input("Enter age: ")
city = input("Enter city: ")

print("Name:", name)
print("Age:", age)
print("City:", city)

#Addition of Two Numbers


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)

#swapping
a=10
b=20
temp=a
a=b
b=temp
print(a,b)

#Swapping of Two Numbers
a = input("Enter first value: ")
b = input("Enter second value: ")

a, b = b, a

print("a =", a)
print("b =", b)

#add
print(a+b)

x=5
y=10
print(x,y)
print("value of x is:", x+5)
print("value of y is:", y-5)

#task1

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Input marks for 5 subjects
maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))
hindi = float(input("Enter Hindi marks: "))
computer = float(input("Enter Computer marks: "))

# Calculate total and percentage
total = maths + science + english + hindi + computer
percentage = (total / 500) * 100

# Print marksheet
print("\n*Marksheet*")
print(f"Name: {name}")
print(f"Roll No: {roll_no}")
print(f"Maths: {maths}")
print(f"Science: {science}")
print(f"English: {english}")
print(f"Hindi: {hindi}")
print(f"Computer: {computer}")
print(f"Total: {total}/500")
print(f"Percentage: {percentage:.2f}%")
