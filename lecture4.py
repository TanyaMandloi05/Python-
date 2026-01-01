# Object Oriented Programming
# class is a blueprint for object and objects are real world entities
class Student:
    subject = "Python"
    year = "4th"
    college = "AITR"

stu1 = Student()
print(stu1.subject, stu1.year, stu1.college)

# constructor
# self is a parameter which is always required which assign variable in memory for objects
# self is basically the object who is calling to it
# there are two type of constructor parameterized and default(1 parameter)
# python only allow one constructor at a time 
class Student:
    subject = "Python" #class attribute
    def __init__(self, name, cgpa):
        self.name = name #instance attribute
        self.cgpa = cgpa

    def get_Cgpa(self):
        return self.cgpa
    
s1 = Student("Tanya", 9.8)
s2 = Student("Urvashi", 9.2)
print(s1.name, s1.cgpa)
print(f"cgpa for {s1.name} is {s1.get_Cgpa()}")


# type of methods 1.) Instance Method
class Laptop:
    storage_type = "SSD"
    def __init__(self, RAM, Storage): #instance method
        self.RAM = RAM
        self.Storage = Storage

    def get_info(self):
        print(f"laptop ram is {self.RAM}, storage is {self.Storage} and storage type is {self.storage_type}")

    @classmethod
    def get_storage(cls):
        print(f"{cls.storage_type}")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * price/100)
        print(f"discounted price = {final_price}")

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")
l1.get_info()
l1.get_storage()
l1.calc_discount(40_000, 10)
        
#Que Product Store
# Design and create an online store for products with the following details:
# Product name
# Product price
# The system should:
# Track the total number of products being created.
# Include a static method to calculate the discount on each product based on a given percentage (%) parameter.

class Product:
    total_product = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_product += 1
    
    @classmethod
    def get_total_product(cls):
        print(f"total products sell are {cls.total_product}")

    @staticmethod
    def cal_dis(price, dis):
        final_price = price-(dis*(price/100))
        print(f"final price {final_price}")

p1 = Product("mobile", 12000)
p2 = Product("laptop", 40000)
p3 = Product("handfree", 500)

p1.cal_dis(p1.price, 10)

# Encapsulation-> wrap data in single unit(properties and methods)
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance #privat attribute

    # getters(to get the private value)
    def get_balance(self):
        return self.__balance
    
    # setter (to set a private value)
    def set_balance(self, newBalance):
        self.__balance = newBalance
    
acc1 = BankAccount("Tanya", 10_000)
print(acc1.get_balance())
acc1.set_balance(20_000)
print(acc1.get_balance())

# inheritance
class Employee:
    start_time = "6pm"
    end_time = "9pm"

    def __init__(self, end_time):
        self.end_time = end_time

class Teacher(Employee):
    def __init__(self, sub):
        self.sub = sub

t1 = Teacher("Math")
print(t1.sub, t1.start_time, t1.end_time)

# multilevel inheritance
class Employee:
    start_time = "8am"
    end_time = "9pm"

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class Account(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary

A1 = Account(35000, "CA")
print(A1.salary, A1.role, A1.start_time)

# multiple inheritance
class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, cgpa):
        self.cgpa = cgpa

class TA(Teacher, Student):
    def __init__(self, salary, cgpa, name):
        super().__init__(salary)
        Student.__init__(self,cgpa)
        self.name = name

t1 = TA(40000, 9.2, "Tanya")
print(t1.salary, t1.cgpa, t1.name)

# Abstraction -> Hiding implementation detail and showing only important or essential features
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar")

l1 = Lion()
l1.make_sound()

# Polymorphism
# (function overloding)
class Employee:
    def get_desgination(self):
        print("Designation = Employee")
    
class Teacher(Employee):
    def get_desgination(self):
        print("Desgination = Teacher")

t1 = Teacher()
t1.get_desgination()

# duck typing
class Employee:
    def get_desgination(self):
        print("Designation = Employee")
    
class Teacher():
    def get_desgination(self):
        print("Desgination = Teacher")

t1 = Teacher()
t1.get_desgination()