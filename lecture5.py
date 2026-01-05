# read all the data
f = open("sample.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

# read data line by line
f = open("sample.txt", "r")
data = f.readline()
print(data)
data = f.readline()
print(data)
f.close()

# completely write the file(write mode first trucate the whole file then start writing)
f = open("sample.txt", "w")
f.write("we are writing the new data to the file")
f.close()

# append mode(append text in the file where it was ended)
f = open("sample.txt", "a")
f.write("\n appending new text to the file")

# x (creates a new file if not exists already)
f = open("sample2.txt", "x")
f.write("writing file with x mode")

# a+(for reading and writting both)
# pointer start from the starting so it override the initial data if we write first
f = open("sample.txt", "r+")
f.write("writing data with r+")
data = f.read()
print(data)

# a+ (if we first read pointer will go to the end and then if we write the data it will write from the end)
f = open("sample.txt", "r+")
data = f.read()
print(data)
f.write("writing data with r+")

# w+(trucncate whole then write pointer goes to the end so we didnt see nothing when read)
f = open("sample.txt", "w+")
f.write(" writing data with w+ ")
data = f.read()
print(data)

# a+(appneding starts from end so pointer goes to the end and we see nothing when read)
f = open("sample.txt", "a+")
f.write(" writing data with a+ ")
data = f.read()
print(data)

# with keyword(it is used to open file but we does not explicitely need to close the file)
with open("sample.txt", "r") as f:
    data = f.read()
    print(len(data))

# delete a file
import os
os.remove("sample3.txt")

# Practice problem (searcha word python)
word  = "python"
data = True
line = 1
with open("sample.txt", "r") as f:
    while(data):
        data = f.readline()
        if(word in data):
            print(f"{word} found at line {line}")
        line += 1
    