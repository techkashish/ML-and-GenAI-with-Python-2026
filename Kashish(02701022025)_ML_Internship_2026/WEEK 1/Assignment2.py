#Q1. Find the sum of first 10 natural numbers
num=0
for i in range (11):
    num+=i
print(num)

#Q2. Find factorial of a number
factnum=int(input("Enter the number"))
fact=1
for i in range (factnum,0,-1):
    fact*=i
print("The Factorial of the number is ",fact)

#Q3. To print the fibonacci series
a=0
b=1
numb=int(input("Enter the number "))
for i in range(numb):
    c=a+b
    print(a)
    a,b=b,c

#Q4. Find largest among 3 numbers
first=int(input("Enter the first number"))
second=int(input("the second number"))
third=int(input("Enter the third number"))
if first>second and first>third:
    print("The largest number is",first)
elif second>first and second>third:
    print("The largest number is",second)
else:
    print("The largest number is",third)

#Q5. Create student result system
#-Input student details
#-Input marks
#-calculate percentage
#-Display grade

students=[]
n=int(input("enter the number of students "))
for i in range(n):
    dict={}
    dict["name"]=input("Enter your name")
    dict["stuclass"]=int(input("Enter your class"))
    dict["rno"]=int(input("Enter your roll number"))
    dict["marks"]=int(input("Enter your marks"))
    marks=dict["marks"]
    if marks>=80:
        grade="A"
    elif marks<80 and marks>=65:
        grade="B"
    elif marks<65 and marks>=50:
        grade="C"
    elif marks<50 and marks>=35:
        grade="D"
    else:
        grade="Fail"
    dict["grade"]=grade
    students.append(dict)
print (students)



    



