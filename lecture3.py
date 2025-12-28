# Strings (strings are immutable we cannot change its character)
word1 = "I love "
word2 = "Coding"
print(word1 + " " + word2)
print(word2[4])

# slicing 
print(word2[2:6]) 

# formating using format
a = 5
b = 10
sum = a+b
print("sum is {}".format(sum))
print("sum of {} and {} is {}".format(a,b,sum))

# index based formatting
print("sum of {1} and {0} is {2}".format(a,b,sum))

# value based formatting
print("value of a is {a} b is {b}".format(a=10, b=10))

# using f string
print(f"sum of {a} and {b} is {a+b}")

# lists in python
# lists are mutable in python we can change the value .
marks = [100, 200, 300, "abc", 99.88]
print(len(marks))
print(marks[2])
print(marks[3:len(marks)])

# Methods of list
nums = [2,5,6,1,9]
nums.append(10)
print(nums)

nums.insert(2,18)
print(nums)

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

nums.reverse()
print(nums)

# loops in lists to find out index value of x

value = [10, 19, 17, 15, 20]
x = 19
idx = 0
for val in value:
    if(val == x):
        print(f"idx found at {idx}")
        break
    idx = idx+1


# tuples (immutable) stored data in (open brackets)
# tuple works similar to lists like it can have multiple values slicing works same
#  but we cannnot keep a single value in tuple if we want we need to give , otherwise it will take the value type

tup = (1,2,5,6,9,3)
print(type(tup))
print(tup[2])

tup = ("abc")
print(type(tup)) 

# methods in tuple
tupl = (2,3,4,2,2,4,6)
print(tupl.index(2))
print(tupl.count(4))

# Dictonary(this are mutable) and unorderd it stores key value pair where keys are unique
info = {
    "name":"tanya",
    "cgpa":7.79,
    "marks":[99, 87, 45],
    3.14: "PI"
}

print(type(info))
info["cgpa"] = 9.1
print(info)

# Methods in dictionary

# to return all keys
dict_keys = list(info.keys())
# can also change its type
print(dict_keys)

# to get all values
dict_Val = info.values()
print(dict_Val)

# to get set of key value pair
print(info.items())

# to add new key value pair
info.update({
    "city":"Indore"
})

print(info)

# to get a value (it wil return none if key not exists) normal accessing info["cgpa2"] will give error
print(info.get("cgpa"))
print(info.get("cgpa2"))

# sets -> sets are collection of unique element
# sets are mutable but the values inside the sets should be immutable
# like dictionary and lists are not allowed in set

s = {1,2,2,3}
s.add(5)
print(len(s))
print(s)

empty_set = set()
print(empty_set)

# methods on set
s1 = {1,2,3,4,5,6}
s2 = {1,2,8,9,10}
s3 = {1,1,2,3,4,5}
print(s1.remove(6))
print(s3.clear())
print(s1.intersection(s2))
print(s1.union(s2))

# Que
information = [
    ("Alice","Science"),
    ("Bob", "Math"),
    ("tanya", "physics"),
    ("rudra", "Science"),
    ("priyanshu", "Math"),
    ("tanya", "Math"),
    ("Alice", "physics")
]


# list student enroll in math
# list all unique courses
unique_Courses = set()
for tup in information:
    unique_Courses.add(tup[1])
    if(tup[1] == "Math"):
        print(f"student enroll in Math {tup[0]}")
    

print(unique_Courses)

# create dictionary (student, set of courses)
studentInfo = {}
for name, course in information:
    if(studentInfo.get(name) == None):
        studentInfo.update({
            name:set()
        })
    studentInfo[name].add(course)

print(studentInfo)

# Q1. Palindrome String
# Ask the user for a string and check whether it is a palindrome or not.
# (A palindrome is a string that reads the same forward and backward, e.g., "madam", "racecar".)

def isPalindorm(str):
    i = 0
    j = len(str)-1
    while i < j:
        if(str[i] != str[j]):
            return False
        i = i+1
        j = j-1
    return True

str = input("enter a string ")
print(isPalindorm(str))

# Q2. Average of Numbers in a List
# Given a list of integers, compute and print the average of all numbers in the list.

numbers = [2, 3, 4, 5, 1, 9, 8, 7]

total = 0
n = len(numbers)

for num in numbers:
    total += num

print(f"Average of numbers is {total / n}")

# Q3. Merge and Sort Lists
# Take two lists of integers as input from the user, merge them into a single list, and sort the result.

list1 = [1, 2, 7]
list2 = [2, 4, 5]
result = []

for num in list1:
    result.append(num)

for num in list2:
    result.append(num)

result.sort()
print(result)

# # or
list1 = [1, 2, 7]
list2 = [2, 4, 5]
result = list1 + list2
result.sort()
print(result)

# Q4. Even and Odd Tuples
# Given a tuple of integers, create:
# A tuple containing all even numbers
# A tuple containing all odd numbers

tuple = (1,2,3,4,5,6,7,8)
evenTup = ()
oddTup = ()

for num in tuple:
    if(num % 2 == 0):
        evenTup = evenTup + (num,)
    else:
        oddTup = oddTup + (num,)

print(evenTup)
print(oddTup)

# Q5. Student Marks Dictionary (Menu-Based Program)
# Create a dictionary where:
# Keys = student names
# Values = marks (integer)
# Write a menu-based program where the user presses a key to perform operations:
# A → Add a student
# B → Update marks
# C → Search for a student
# D → Display all students and their marks

studentDic = {
    "tanya":90,
    "kirti":100,
    "khushi":89
}

def performTask(operation):
    match operation:
        case 'A':
            newDataKey = input("enter the key ")
            newDataValue = int(input("enter value "))
            studentDic.update({
            newDataKey : newDataValue
            })
        case 'B':
            name = input("enter name of student")
            if name in studentDic:
                marks = int(input("enter marks to update"))
                studentDic[name] = marks
                print("student marks updated")
            else:
                print("student not found")
        case 'C':
            name = input("enter name of the student")
            if name in studentDic:
                print(f"{name} : {studentDic[name]}")
            else:
                print("student not found")
        case 'D':
            if not studentDic:
                print("no student found")
            else:
                for name, marks in studentDic.items():
                    print(name, ":", marks)
    

print("A → Add student")
print("B → Update marks")
print("C → Search student")
print("D → Display all students")

choice = input("Enter choice: ").upper()
performTask(choice)


# Que6.) Given a list of words:
#  Create a dictionary that maps each word to its length.

words = ["apple", "banana", "mango", "cherry"]
dict = {}
for word in words:
    key = word
    value = len(word)
    dict.update({
        key:value
    })

print(dict)

# Que 7.)Count Spaces in a String
# Write a program that takes a string from the user and prints the number of spaces present in the string.
userStr = input("enter a sentence ")
count = 0
for ch in userStr:
    if(ch == " "):
        count = count+1

print(count)

# Q8. Check Common Elements Between Lists
# Write a program to check whether two lists share no common elements.

list1 = [1,2,3]
list2 = [3,4] 

if(set(list1).intersection(set(list2))):
    print("common element exists")
else :
    print("no common elements")      

# Que 9) Given a list, print all elements that appear more than once in the list.
nums = [1, 2, 1, 2, 2, 3, 4, 5, 3, 3, 3, 3, 5]
nums.sort()

ans = []
for i in range(1, len(nums)):
    if nums[i] == nums[i-1] and nums[i] not in ans:
        ans.append(nums[i])

print(ans)

# Q10. Unique Characters in a String
# Ask the user for a string and print:
# All unique characters
# The count of unique characters

userInput = input("enter a string ")
ans = set()
for ch in userInput:
    ans.add(ch)

print(ans)
print(len(ans))