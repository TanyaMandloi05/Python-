# conditional statments, loops, functions
# 1.) Conditional Statements
# Que 1.) Write a Python program to check whether a person is eligible to vote and drive based on their age.

age = int(input("enter your age "))
if age >= 18:
    print("you can vote")
    print("you can drive")
else:
    print("you cannot vote")
    print("you cannot drive")


# Que 2.) Write a program that takes traffic light color as input and prints appropriate action (Stop/Look/Go).
color = input("enter color ")
if color == "red":
    print("stop")
elif color == "yellow":
    print("look")
else:
    print("go")

# Que 3.) Write a program to classify a person as child, teenager, or adult using age conditions.
age = int(input("enter age "))
if age < 13:
    print("child")
elif age > 13 and age < 18:
    print("teenager")
else:
    print("adult")

# Que 4.) Create a login system that checks username and password and prints appropriate error messages using nested conditionals.

username = input("enter username ")
password = input("enter password ")
if username == "admin" and password == "strict":
    print("successfull login")
else:
    if password != "strict":
        print("wrong password entered")
    else:
        print("wrong username entered")

# Que 5.) Write a program using a ternary operator to check whether a person is an adult or not.

age = int(input("enter age "))
status = "adult" if age >= 18 else "Not adult"
print(status)

# Que 6.) Write a Python program using match-case to handle traffic light actions based on color input.
color = input("enter color ")
match color:
    case "red":
        print("stop")
    case "green":
        print("go")
    case "yellow":
        print("look")
    case _:
        print("wrong color entered")


# looping started
# Que 1.) Write a program to print numbers from 1 to 5 using a while loop.
i = 1
while(i <= 5):
    print(i)
    i = i+1

# Que 2.) Write a program to print numbers from 5 to 1 using a while loop.
i = 5
while(i > 0):
    print(i)
    i = i-1

# Que 3.) break loop if number is multiple of 6 (loop control statement)
i = 1
while i <= 10:
    if(i % 6 == 0):
        break
    print(i)
    i = i+1

# for loop
# Que 1.) Write a program to print numbers from 0 to 4 using a for loop and range()

for num in range(5):
    print(num)

# Que 2.) Write a program to iterate over a string and print each character.
str = "Tanya"
for s in str:
    print(s)

# Que 3.) Write a program to check whether a specific character exists in a given string.
str = "tanya"
if 'a' in str:
    print("character exists")

# Que 4.) Write a program to count the number of occurrences of the letter 'i' in a word
word = "artificial intelligence"
ans = 0
for ch in word:
    if(ch == 'i'):
        ans = ans + 1

print(ans) 

# Que 5.) Write a program to demonstrate range() with one argument.
# Write a program to demonstrate range() with start and stop values.
# Write a program to demonstrate range() with start, stop, and step values.

for i in range(5): 
    print(i)
    
for j in range(2,10):
    print(j)

for k in range(0, 20, 2):
    print(k)

# Que 6.) multiplication table of n
n = int(input("enter value of table "))
for i in range(1, 11):
    print(i*n)
    
# functions started
# Que 1.) factorial of a number n
def factorial(n):
    if(n == 1):
        return 1
    return n * factorial(n-1)

fact = factorial(4)
print(fact)

# Que 2.) Write a function with a default parameter value
def sum(a, b=10):
    return a+b

print(sum(4))

# Que 3.) program for lambda function
avg = lambda a,b,c: (a+b+c) / 3
print(avg(1,2,3))


# Practice problem started 
# Write a program that takes salary as input and calculates the final tax rate using conditional statements based on the following rules:
# If salary is less than 30,000 → tax rate is 5%
# If salary is between 30,000 and 70,000 → tax rate is 15%
# If salary is greater than 70,000 → tax rate is 25%

salary = int(input("enter your salary "))
if(salary < 30000):
    print("tax rate is 5% ")
elif(salary >= 30000 or salary <= 70000):
    print("tax rate is 15% ")
else:
    print("tax rate is 25%")

# Que2 a) Write a function that takes two integers as input.
# b) The function should print all even numbers between them (inclusive).

def evenInRange(a, b):
    for val in range(a, b+1):
        if(val % 2 != 0):
            continue
        print(val)

evenInRange(10, 20)

# Q3. Print Digits of a Number
# Write a function that takes a number n as input and prints all its digits.
# Example:
# If n = 312, output should print digits 3, 1, and 2.

def print_digit(n):
    digits = []
    while(n > 0):
        digits.append(n%10)
        n = n//10
    for digit in reversed(digits):
        print(digit)

print_digit(312)


# Q4. Count Number of Digits
# Write a function that returns the total number of digits in a given number n.

def totalNumDigit(n):
    count = 0
    while(n > 0):
        n = n//10
        count = count+1
    return count

print(totalNumDigit(9000))

# Q5. Write a function that returns the sum of digits of a given number n.
def sumOfDigit(n):
    sum = 0
    for i in range(n+1):
        sum = sum+i
    return sum    

print(sumOfDigit(4))

# Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.
for i in range(1, 101):
    if((i % 3 == 0) and (i % 5 == 0)):
        print(i)

#Que7 Design a program that continuously takes numbers as input from the user and prints whether the number is positive or negative.
# The program should stop only when the user enters "Quit".

while True:
    userInput = input("enter number or type quit ")
    if (userInput == quit):
        break
    number = int(userInput)
    if(number < 0):
        print("number is negative ")
    else:
        print("number is positive ")    

# Q8. Simple Calculator
# Create a simple calculator function that performs arithmetic operations.
# The function should be defined as:
# calculator(a, b, operation)
# Where operation can be:
# '+' for addition
# '-' for subtraction
# '*' for multiplication
# '/' for division
# The function should perform the operation based on the parameter passed

def calculator(a, b, operation):
    if(operation == '+'):
        return a+b
    elif(operation == '-'):
        return a-b
    elif(operation == '*'):
        return a*b
    else:
        return a/b
    
print(calculator(10, 10, '-'))

# Q9. Prime Number Checker
# Write a function is_prime(n) that:
# Returns True if n is a prime number
# Returns False otherwise

def isPrime(n):
    if(n <= 0):
        return False
    if(n == 2):
        return True
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True
    
number = int(input("enter a number "))
print(isPrime(number))

# Que 10
# Create a Number Guessing Game program.
# A secret number is already decided by you
# Ask the user to guess the number
# Print:
# "Too high" if the guess is greater than the secret number
# "Too low" if the guess is less than the secret number
# "Correct!" if the guess matches the number

secretNum = 200
userNum = int(input("guess a number "))
if(userNum == secretNum):
    print("correct guess ")
elif(userNum < secretNum):
    print("too low")
else:
    print("too high")
