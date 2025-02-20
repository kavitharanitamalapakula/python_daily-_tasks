#  Easy Questions

# 1 write a program to check if a given number is positive, 
# negative, or zero. 

num=float(input("enter a number"))
if num==0:
    print("zero")
elif num>0:
    print("positive")
else:
    print("negative")

#2 Determine if a number is odd or even. 
num=int(input())
if num^1==0:
    print(num,"is even")
else:
    print(num,"is odd")

#3 Check if a person is eligible to vote (age >= 18). 
print("is eligible") if num>=18 else print("not eligible")

#4 Write a program to find the greatest of two numbers. 
num1,num2= 10,20
print(num1,"is greater") if num1>num2 else print(num2,"is greater")

#5 print "Pass" if a student scores more than 40 marks; 
# otherwise, print "Fail." 
marks=int(input())
print("Pass") if marks>40 else print("Fail")

#6 prite a program to display the day of the week based on a 
# number input (1 for Monday, 2 for Tuesday, etc.).

num=input()
if num=="1":
    print("Monday")
elif num=="2":
    print("Tuesday")
elif num=="3":
    print("Wednesday")
elif num=="4":
    print("thursday")
elif num == "5":
    print("friday")
elif num=="6":
    print("saturday")
elif num=="7":
    print("sunday")
else:
    print("invalid Number")
# 7 implement a simple calculator to perform addition, 
# subtraction, multiplication, and division

operation=input("enter an operation : ").lower()
if operation in ["add","+","substraction","sub","division","multiplication","-","mul","*","div","/","power","**","exponent","addition"]:
    op1=int(input("Enter a first Number : "))
    op2=int(input("Enter a second Number : "))
    if operation in ["add","+","addition"] :
        print(op1+op2)
    elif operation in ["sub","-", "substraction"]:
        print(op1-op2)
    elif operation in ["mul","*","multiplication"]:
        print(op1*op2)
    elif operation in ["div","/","division"]:
        print(print(op1/op2)) if op2!=0 else print("ZeroDivisionError")
    elif operation in ["power","**","exponent"]:
        print(op1**op2)
else:
    print("invalid operation")


# 8. Write a program to display the name of a month based on 
# the month number (1 for January, 2 for February, etc.)

month_number=int(input("Enter a Month Number : "))
if month_number == 1:
    print("January")
elif month_number == 2:
    print("February")
elif month_number == 3:
    print("March")
elif month_number == 4:
    print("April")
elif month_number == 5:
    print("May")
elif month_number == 6:
    print("June")
elif month_number == 7:
    print("July")
elif month_number == 8:
    print("August")
elif month_number == 9:
    print("September")
elif month_number == 10:
    print("October")
elif month_number == 11:
    print("November")
elif month_number == 12:
    print("December")
else:
    print("Invalid month number!")

#  Medium Questions

# 1. Write a program to find the greatest of three numbers. 
num3=float(input("enter 1st number : "))
num4=float(input("enter 2nd number : "))
num5=float(input("enter 3rd number : "))
if num3>num4 and num3>num5:
    print(num3,"is greater")
else :
    print(num4,"is greater") if num4>num5 else print(num5,"is greater")

# 2. Check if a year is a leap year. 
num6=int(input("enter a year : "))
if (num6%4==0) and (num6%100!=0 or num6%400==0):
    print(num6,"is leap year")
else:
    print(num6,"is not leap year")

# 3. write a program to classify a character entered by the user 
# as a vowel, consonant, or neither.

character = input("enter a single character : ").lower()
if len(character)!=1:
    print("invalid character")
else:
    if character in "aeiou":
        print("character is vowel")
    elif character.isalpha():
        print("character is a consonant")
    else:
        print(character,"is a special character")

# 4 . calculate the grade of a student based on the marks they 
# score: 
# 1.  90-100  : Grade A 
# 2.  80-89  : Grade B 
# 3.  70-79  : Grade C 
# 4.  <70  : Fail.

student_marks=float(input("enter a student marks : "))
if student_marks>=100 or student_marks<0:
    print("invalid marks")
elif 100>=student_marks>=90 :
    print("Grade A")
elif 89>=student_marks>=80:
    print("Grade B")
elif 79>=student_marks>=70:
    print("Grade C")
elif student_marks<70:
    print("Fail")

# 5. write a program to check if three sides length form a valid triangle. 
side1=int(input("Enter 1st side of a triangle : "))
side2=int(input("Enter 2nd side of a triangle : "))
side3=int(input("Enter 3rd side of a triangle : "))
if side1+side2 >side3 and side1+side3>side2 and side2+side3>side1:
    print("it form a valid triangle")
else:
    print("it not form a valid triangle")
