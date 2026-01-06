# Create a program that:
# Opens a file named names.txt in write mode
# Takes 5 names as input from the user and writes them to the file (one name per line)
# Opens the same file in read mode and prints all the names

with open("names.txt", "w") as f:
    for i in range(5):
        name = (input("enter names "))
        f.write(f"{name}\n")

with open("names.txt", "r") as f:
    data = f.read()
    print(data)

# Create a program that:
# Opens a file named log.txt in append mode
# Adds a new log entry such as "Program run successfully"
# Opens the file in read mode and prints all log entries
with open("log.txt", "a") as f:
    f.write("Program run successfully\n")

with open("log.txt", "r") as f:
    data = f.read()
    print(data)

# Create a program that:
# Has a list of numbers:
# [5, 10, 15, 20, 25]
# Uses list comprehension to create a new list containing only numbers greater than 15
# Prints the new list
 
numbers = [5, 10, 15, 20, 25]
filtered_numbers = [n for n in numbers if n > 15]
print(filtered_numbers)


# Create a Python dictionary of 3 cities and their populations.
# Write a program that:
# Saves this dictionary into a JSON file named cities.json
# Loads the JSON file and prints each city with its population
# Asks the user for a new city and its population
# Updates this new information into the same JSON file
 
import json
city_data = {
    "Indore": 10_0000,
    "Dewas": 50_000,
    "ujjain": 70_000
}

with open("cities.json", "w") as f:
    json.dump(city_data, f)
    
with open("cities.json", "r") as f:
    data = json.load(f)
    for cities, population in data.items():
        print(cities , ":" , population)

    new_city = input("enter a new city ")
    new_population = int(input("enter population of the city "))
    data[new_city] = new_population

with open("cities.json", "w") as f:
    json.dump(data, f)

# Write a program that:
# Tries to open a file named data.txt in read mode
# If the file does not exist, catches the exception and prints:
# File not found!

try:
    with open("data.txt", "r") as f:
        data = f.read()

except FileNotFoundError:
    print("File not found")

else:
    print(data)

finally:
    print("program ended")
