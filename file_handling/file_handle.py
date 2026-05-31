# # Opening a file
# f = open("geek.txt", "r")
# # Accessing file properties
# print("File name = ", f.name)
# print("File mode = ", f.mode)
# print("File is closed" if f.closed else "File is still open")

# # Reading a file
# print(f.read())
# # closing a file
# f.close()
# print("File is closed" if f.closed else "File is still open")

# NOW WE WILL LEARN WRITING INTO A FILE
print("*+" * 50)
with open("geek.txt","w") as filee:
    filee.write("Hello My Name is Hafiz Mohsin \n")
    filee.write("Today I've completed Python Basics")

print("File written Successfully")

# File Exception Handling
try:
    file = open("geek.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("Error:", e)
finally:
    file.close()