# LCM
a = int(input("enter a number: "))
b = int(input("enter a number: "))
greater = max(a, b)
smallest = min(a, b)
for i in range(greater, a*b+1, greater):
    if i % smallest == 0:
        print("LCM of", a, "and", b, "is", i)
        break
# GCD
n1 = int(input("enter a number: "))
n2 = int(input("enter a number: "))
while n2 != 0:
    n1, n2 = n2, n1 % n2
print(n1) 

# prime numbers in range 
lower = int(input("enter a lower limit: "))
upper = int(input("enter a upper limit: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

# nearest prime 
num = int(input("Enter a number: "))
temp = num
c = 0
while c < 1:
    num += 1
    fact = True
    for i in range(2, num):
        if num % i == 0:
            fact = False
            break
    if fact:
        print(num, "is next prime")
        c += 1

