#Q1.Find area of rectangle
a=int(input("Enter the length"))
b=int(input("Enter the breadth"))
print("The area of the rectangle is ",a*b)

#Q2.Find simple interest
p=int(input("Enter the principal amount"))
r=int(input("Enter the rate of iterest"))
t=int(input("Enter the time"))
print("The simple interest is ",(p*r*t)/100)

#Q3. Convert temperature from Celsius to Fahrenheit
temp=int(input("Enter the the temperature in celsius"))
temp_in_F= (temp*9/5)+32
print("The temoerature in Fahrenheit is ",temp_in_F)

#Q4. Calculate the average of three numbers
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))
avg=(a+b+c)/3
print("The average of three numbers are", avg)

#Q5.Find square and cube of a number
numb=int(input("Enter the number "))
print("The square of the number is ",numb*2)
print("The cube of the number is ",numb*3)

#Q6.Write a python code to swap the two numbers without including the third variable
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
a,b=b,a
print("After swapping the first number is ",a)
print("After swapping the second number is ",b)

#Q7.Student Report programme
name=(input("Enter your name"))
physics=int(input("Enter your physics marks"))
chemistry=int(input("Enter your chemistry marks"))
maths=int(input("Enter your maths marks"))
english=int(input("Enter your english marks"))
total=physics+chemistry+maths+english
print("The total marks scored is ",total)
percent=(total/400)*100
print('The total percentage scored is ',percent)
