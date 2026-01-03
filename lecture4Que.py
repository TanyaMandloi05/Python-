# Q1. Bank Account Class
# Create a class BankAccount with the following:
# Attributes:
# account_number
# owner_name
# balance
# Methods:
# deposit()
# withdraw()
# check_balance()

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def check_balance(self):
        return self.balance


b1 = BankAccount(12345678, "Tanya", 10000)
b1.deposit(2000)
b1.withdraw(1000)
print(b1.check_balance())

# Q2. Book Class with Reviews
# Create a class Book with the following attributes:
# title
# author
# list_of_reviews
# Add methods to:
# Add a new review
# Count total reviews
# Display all reviews

class Book:
    totalReview = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def addReview(self, new_review):
        self.reviews.append(new_review) 
      
    def countReview(self):
        return len(self.reviews)

    def displayReview(self):
        for review in self.reviews:
            print(review) 

b1 = Book("atomic Habit", "James Goslin")
b1.addReview("4 star")
b1.displayReview()
print(b1.countReview())

# Q3. Student Class (Encapsulation)
# Create a class Student using encapsulation with private attributes:
# _name
# _roll_no
# _marks
# Provide getter and setter methods with validation:
# Name cannot be empty
# Roll number must be between 1 and 100
# Marks cannot be negative

class Student:
    def __init__(self, name, rollNo, marks):
        self.set_name(name)
        self.set_roll(rollNo)
        self.set_marks(marks) 

    def set_name(self, name):
        if  not name:
            raise ValueError("Name cannot be empty")
        else:
            self.__name = name

    def set_roll(self, rollNo):
        if(rollNo < 1 or rollNo > 100):
            raise ValueError("roll number must be between 1 and 100")
        else:
            self.__rollNo = rollNo

    def set_marks(self, marks):
        if(marks < 0):
            raise ValueError("marks cannot be negative")
        else:
            self.__marks = marks

    def get_name(self):
        return self.__name
    
    def get_marks(self):
        return self.__marks
    
    def get_rollNo(self):
        return self.__rollNo
    
s1 = Student("Tanya", 12, 99)
print(s1.get_marks())
print(s1.get_name())
s1.set_name("kirti")
print(s1.get_name())
s1.set_name("")
print(s1.get_name())
    
# Q4. Shape Class (Method Overriding)
# Create a base class Shape with a method area().
# Create subclasses:
# Circle
# Rectangle
# Triangle
# Each subclass should override the area() method.

import math
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.b * self.h)/2

c1 = Circle(3)
res = c1.area()
print(res)

# Q5. Vehicle Class (Inheritance)
# Create a base class Vehicle with attributes:
# brand
# model
# Create subclasses:
# Car → add attribute seats
# Bike → add attribute engine_cc

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
     def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc
    
c1 = Car("BMW","BMW 3 Series", 5)
print(c1.brand, c1.model, c1.seats)

# Q6. Employee Class (Abstraction)
# Create an abstract class Employee with an abstract method:
# calculate_salary()
# Create subclasses:
# Intern
# FullTimeEmployee
# ContractEmployee
# Each subclass should implement calculate_salary() differently.

from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self, stipend):
        self.salary = stipend

    def calculate_salary(self):
        return self.salary

class FullTimeEmployee(Employee):
    def __init__(self, basic, hra, tax):
        self.basic = basic
        self.hra = hra
        self.tax = tax

    def calculate_salary(self):
        return self.basic + self.hra - self.tax
    
class contractEmployee(Employee):
    def __init__(self, hourly_rate, hour_worked):
        self.hourly_rate = hourly_rate
        self.hour_worked = hour_worked

    def calculate_salary(self):
        return self.hour_worked*self.hourly_rate

e1 = FullTimeEmployee(5000, 1000, 1000)
print(e1.calculate_salary())

# Q7. Person Class (Constructor Overloading using Default Parameters)
# Create a class Person whose constructor supports:
# name only
# name + age
# name + age + address
# (Note: Python does not support multiple constructors directly, so use default parameters.)

class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

p1 = Person("tanya")


# Q8. Player Class (Instance & Class Attributes)
# Create a class Player with:
# A class variable player_count
# Instance variables name and level
# Track how many player objects are created using the class variable.

class Player:
    player_count = 0
    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

    @classmethod
    def get_player_count(cls):
        return cls.player_count

p1 = Player("tanya", 1)
p2 = Player("aman", 3)
print(Player.get_player_count())

# Q9. Multiple Inheritance
# Create the following classes with suitable attributes and methods:
# Herbivore
# Carnivore
# Omnivore
# Then create a class Bear that inherits from all the above classes to demonstrate multiple inheritance.

class Herbivore:
    def eat_plant(self):
        print("plants, such as grass, leaves, fruits, and roots.")

class Carnivore:
    def eat_meat(self):
        print("meat")

class Omnivore: 
    def eat_both(self):
        print("eat plants and meat")

class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} can eat : ")
        self.eat_meat()
        self.eat_plant()

bear = Bear("Bear")
bear.eat()


# Q10. Mini Project – OOP Chat System
# Create a Chat System using OOP concepts.
# Create the following classes:
# User
# Message
# ChatRoom
# Implement functionalities:
# Sending messages
# Viewing chat history
# User joining the chat room
# User leaving the chat room

class User:
    def __init__(self, name):
        self.name = name


class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text


class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []

    def join_chat(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"{user.name} joined the chat room")

    def leave_chat(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user.name} left the chat room")

    def send_message(self, user, text):
        if user not in self.users:
            print(f"{user.name} is not in the chat room")
            return

        message = Message(user, text)
        self.messages.append(message)

    def view_history(self):
        print("\n--- Chat History ---")
        if not self.messages:
            print("No messages yet")
            return

        for msg in self.messages:
            print(f"{msg.sender.name}: {msg.text}")

u1 = User("Tanya")
chat = ChatRoom()

chat.join_chat(u1)
chat.send_message(u1, "hi this is difficult but I did it")
chat.send_message(u1, "do your best")
chat.view_history()
chat.leave_chat(u1)
