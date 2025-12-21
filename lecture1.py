# average of two numbers
a = int(input("enter first number  "))
b = int(input("enter second number  "))
avg = (a+b)/2
print(type(avg))

# Que1. Write a program that asks the user for their name and age,then prints a sentence like:Hello Shradha, you are 21 years old!
name = input("enter you name ")
age = int(input("enter your age "))
print("Hello" , name , "your age is" , age)

# Que2. write program that will do sum, diffrence, product and quotient
a = float(input("enter first val "))
b = float(input("enter second val "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# # Que3. Ask the user to enter two integers and one float. Convert them all to floats and print their average.
a = int(input("Enter first integer value: "))
b = int(input("Enter second integer value: "))
c = float(input("Enter floating value: "))

avg = (float(a) + float(b) + c) / 3
print(avg)


# Q4. The user enters a string containing a number (e.g., "45"). Convert it to:
# an integer
# a float
# a string again
# Print all three values along with their types.

s = input("Enter a number string: ")

i = int(s)
f = float(s)
st = str(s)

print(i, type(i))
print(f, type(f))
print(st, type(st))



# Q5. Evaluate and print the result of the following expression:
# x = 10 + 3 * 2 ** 2

x = 10 + 3 * 2 ** 2
print(x)

# Q6. Write a program to swap the values of two numbers entered by the user.
a = int(input("enter value a "))
b = int(input("enter value b "))
temp = a
a = b
b = temp
print("value of a is ", a)
print("value of b is ", b)

# Q7. Ask the user for a temperature in Celsius (string input). Convert it to float, then calculate and print the temperature in Fahrenheit using the formula:
# Fahrenheit = (Celsius × 9/5) + 32

temp = input("enter the temperature i celsius ")
Celsius = float(temp)
Fahrenheit = (Celsius * 9/5) + 32
print(Fahrenheit)

# Q8. Take the radius as user input and print the area of a circle.
# Use the formula:
# Area = π × r²
# (Take the value of π as 3.14)

radius = int(input("enter radius for a circle "))
area = 3.14*radius*radius
print(area)

# Q9. Ask the user for Principal (P), Rate (R), and Time (T). Convert all values to float and compute simple interest using the formula:
# SI = (P × R × T) / 100

principal = input("enter principal ")
rate = input("enter rate ")
time = input("enter time")
p = float(principal)
r = float(rate)
t = float(time)
SI = (p*r*t) / 100
print(SI)

# Q10. Take a decimal number as input (e.g., 45.78) and output its:
# integer part (45)
# fractional part (.78)

num = float(input("enter decimal val "))
integer_part = int(num)
fractional_part = num - integer_part
print(integer_part)
print(fractional_part)
