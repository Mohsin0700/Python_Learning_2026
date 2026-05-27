print("Just Like other languages we can use variables in Python")
print("Variables are containers for storing data values")
print("Variables are created the moment you first assign a value to them")

# Rules for Python variables
"""
1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. A variable name is case-sensitive (age, Age and AGE are three different variables)
"""
name = "Mohsin"
age = 28
print("My name is " + name + " and I'm " + str(age) + " years old")
print("We don't need closing statement in python which makes it faster for writing code")
print("*********************************************************************************")
print("we can also delete a variable if we don't need that, which help to save memory and it shows python performance over other languages")
print("let us delete name variable and check printing that variable")
del name
# print(name)
print("If you un comment above line you will see an error regarding accessing deleted keyword")

print("further python is shared references language which mean variable does not hold the value but the reference only, and python is also capable of assigning multiple values to multiple variable at a same time so we can swap the values easily")
x = 5
y = 10
x, y = y, x
print("Now You will be shoked")
# print("Value of X is" + x)
# print("Value of Y is" + y)
print("Aaah as I've been learning I got a new error which helped me to learn a new thing that we can't concatenate string and int, let me find the solution.")
print("Value of X is" , x)
print("Value of Y is" , y)
print("We use 'len' keyword to get the length of a string")
name = "Hafiz Sahab"
nameLenth = len(name)
print("Variable 'name' length is :", nameLenth)