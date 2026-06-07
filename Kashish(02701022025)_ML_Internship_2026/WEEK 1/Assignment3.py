#Q1.Create a function to print first ten natural numbers
def natural_numbers():
    for i in range(1,11):
        print(i)
natural_numbers()

#Q2.Create a function to print sum of first N natural numbers
def first_n_natural_numbers(num):
    numb=0
    for i in range (1,n+1):
        numb+=i
    print("The sum of first N natural numbers is",numb)

n=int(input("Enter the number"))
first_n_natural_numbers(n)


#Q3. Create a function to reverse the number
def reverse(num):
    for i in range(len(y)-1,-1,-1):
        print(y[i],end="")
number=int(input("Enter the number whose reverse is to be find "))
y=str(number)
reverse(y)

#Q4.Create a function to count digits in a number
def digit_count(num):
    print("The number if digits is",len(str(num)))
num=int(input("Enter the number"))
digit_count(num)

#Q5. Create a function to check palindrome number
def check_palindrome(n):
    z=""
    for i in range(len(y)-1,-1,-1):
        z=z+y[i]
    print(z)
    if y==z:
        print("The number is palindrome")
    else:
        print("The number is not palindrome")
number=int(input("Enter the number whose palindrome is to be find "))
y=str(number)
check_palindrome(y)

#Q6.Create a function to generate the fibonacci series
def fseries(n):
    a=0
    b=1
    for i in range(numb):
        c=a+b
        print(a)
        a,b=b,c

numb=int(input("Enter the number "))
fseries(numb)

#Q7.Calculate using functions
def calculation(a,b):
    print("chose a for addition")
    print("chose s for subtraction")
    print("chose d for division")
    print("chose m for multiplication")
    choice=input("enter your choice")
    if choice=="a":
        print("the sum of the number is ",a+b)
    elif choice=="s":
        print("the difference of the number is ",a-b)
    elif choice=="d":
        print("the divsion of the number is ",a/b)
    else:
        print("the multiplication of the number is ",a*b)
    
a=int(input("enter the first number"))
b=int(input("enter the second number"))
calculation(a,b)

#Q8.
import pandas as pd
def student(n):
    l1=[]
    l2=[]
    l3=[]
    for i in range (n):
        name=(input("enter uyour name"))
        age=int(input("enter your age"))
        standard=int(input("enter your class"))
        l1.append(name)
        l2.append(age)
        l3.append(standard)
        data={
            "Name":l1,
            "Age":l2,
            "Class":l3
        }
        return data

n=int(input("Enter the number of students"))
result=student(n)
df=pd.DataFrame(result)
df.to_csv("student.txt",sep="\t",index=False)
print("Data is saved in student.txt")

#Q9
def display_student():
    with open("student.txt","r")as file:
        print(file.read())
    
display_student()

#Q10
try:
    a=int(input("Enter the numerator"))
    b=int(input("Enter the denominator"))
    result=a/b
    print("The result is ",result)
except ZeroDivisionError:
    print("Error:Division by zero is not allowed")

#Q11
class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks=marks

    def display(self):
        print("Nmae:",self.name)
        print("Marks:",self.marks)

name=input("Enter your name")
marks=int(input("Enter your makrs"))
result=Student(name,marks)

result.display()
    
