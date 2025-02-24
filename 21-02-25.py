#  Easy Questions:
# 1. Print all numbers from 1 to 100 using a  for  loop
for i in range(1,101):
    print(i)
# 2. write a program to print the sum of the first  n  natural 
# numbers. (n*n+1/ 2) 
limit=int(input())
sum=0
for i in range(1,limit+1):
    sum=sum+i
print(sum)

# 3. print all even numbers between 1 and 50 using a  while 
# loop. 
limit2= int(input())
for i in range(0,limit2+1,2):
    print(i)
# 4. write a program to display the multiplication table of a given 
# number. First 20 
table = int(input("Enter which table you want: "))
for i in range(1, 21):
    print(f"{table} x {i} = {table * i}")
# 5. reverse a number using a  while  loop. 
#       1.  Also can we get the sum of all the digits. 
# 6. write a program to count the number of digits in a given 
# number using a  while  loop.

num = int(input("Enter the number you want to reverse: "))
rev_num = 0
digit_sum = 0
count=0
while num > 0:
    digit_sum += num % 10 
    rev_num = rev_num * 10 + num % 10 
    count+=1
    num //= 10

print("Reversed number:", rev_num)
print("Sum of digits:", digit_sum)
print("Number of digits:", count)

#7. write a program that keeps asking the user to enter numbers 
# until they enter a negative number. Use a  while  loop. 

while True:
    non_negative=int(input("enter non negative number : "))
    if non_negative<0:
        break
#   Medium Questions
# --------------------------------

#  1. Print the first 10 terms of the Fibonacci series using a  for loop
num_terms=int(input("enter no.of terms : "))
n1=0
n2=1
for i in range(num_terms):
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3

# 2. check if a given number is a prime number using a  for loop.
number = int(input("Enter a number: "))
if number <= 1:
    print("Prime numbers start from 2")
else:
    flag = True
    for i in range(2, int(number ** 0.5) + 1):  
        if number % i == 0:
            flag = False
            break
    if flag:
        print(number, "is a Prime Number")
    else:
        print(number, "is not a Prime Number")

# 3. write a program to calculate the factorial of a number using a  while  loop. 

factorial_num = int(input("Enter a number: "))
if factorial_num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = 1
    num = factorial_num
    while num > 1:
        fact *= num
        num -= 1
    print(f"Factorial of {factorial_num} is {fact}")

# 4. print all numbers from 1 to 100 that are divisible by 3 and 5 using a  for  loop.

num_range=int(input("enter a range :"))
for num in range(15, num_range+1, 15):
    print(num, end=" ")

# 5. implement a menu-driven program where the user can choose to: 
# 1.  Find the square of a number. 
# 2.  Find the cube of a number. 
# 3.  Exit.

print("choose 1 for square a number")
print("choose 2 for cube a number")
print("choose 3 for Exist ")
while True:
    choose_options=int(input("choose your option (1/2/3):"))
    if choose_options==1:
        square_num=int(input("Enter a number : "))
        print(square_num*square_num)
    elif choose_options==2:
        cube_num=int(input("Enter a number : "))
        print(cube_num**3)
    elif choose_options==3:
        print("your are existed from this")
        break
    else:
        print("Invalid choice Please enter 1, 2, or 3.")

# 6. implement a basic login system where the user has three 
# attempts to enter the correct password using a loop. 

user_attemps=3
stored_EmailId="user@gmail.com"
stored_Password="user@10000"
while user_attemps>0:
    EmailId=input("enter a EmailId:")
    Password=input("enter a Password:")
    if stored_EmailId==EmailId and stored_Password==Password:
        print("login successfull")
        break
    user_attemps-=1
    if user_attemps==0:
        print("Login failed! No attempts left, Please try again later.")
    else:
        print(f"still you have {user_attemps} attemps")

    