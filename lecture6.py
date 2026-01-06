# exception handling 
try:
    x = int(input("enter value of x "))
    ans = 10/x

except ZeroDivisionError:
    print("division with 0 not allowed")

except ValueError:
    print("wrong value entered")

else:
    print(ans)

finally:
    print("end of file")

# list comprehensions
# define outout, iterable, condition(not neccessary)
# normal way
list = []
for i in range(6):
    list.append(i*i)

print(list)

# with comprenhensions
list = [i*i for i in range(6)]
print(list)

# store only odd numbers
list = [i*i for i in range(6) if i%2 != 0]
print(list)

list1 = [-1,2,-3,4,-5]
ans = [i if i > 0 else 0 for i in list1]
print(ans)

words = ["hello","tanya", "this", "side"]
words = [val.upper() for val in words]
print(words)

# About json data
# converting json string into python obj or dictionary
import json
json_str = '{"name":"Tanya", "isTeacher": true}'
py_obj = json.loads(json_str)
print(py_obj)

# converting python obj into json string 
import json
py_obj = {
  "id": 101,
  "name": "Tanya",
  "role": "MERN Developer",
  "isTeacher": False,
}
json_str = json.dumps(py_obj)
print(json_str)

# when we deal with only strings we use laods and dumps(here s stands for string)
# but usually we deal with files so we use load and dump

# reading a json data from file
import json
with open("data.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)

# writin a json data to a file
import json
data = {
  "orderId": 5421,
  "product": "Wireless Mouse",
  "price": 799,
  "customer": {
    "name": "Amit",
    "membership": "Prime"
  },
  "isOldCustomer": True
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)


