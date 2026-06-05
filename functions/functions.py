
# Creating a function
# def func():
    # print("This is my first function in python")

# calling a function
# func()

# Function with arguments
# def findEvenOrOdd(num):
#     if(num % 2 == 0):
#         print("Number is Even")
#     else:
#         print("Number is odd")

# findEvenOrOdd(8)
# findEvenOrOdd(3)

# Function with default argument
# def greetUser(name = "User"):
#     print("Hello!", name)

# greetUser('Mohsin')
# greetUser()

# def printALine(name, age):
#     print("{} is {} years old".format(name, age))

# printALine(29, "Hasan") Now uncomment this line to see why do we need named parameters/arguments

# printALine(age = 29, name = "Mohsin") order doesn't matter when we use named parameters.

# Arbitrary Arguments:
# In other languages if we have to pass a list to a function then we need to create a list necessary to pass it.but python provides us easiest way to do that through Arbitrary arguments.See the example below.

# def cartItems(*items):
#     num = 1
#     print("Your cart items are below:")
#     for item in items:
#         print(num, item)
#         num += 1


# cartItems('Burger', 'Shawarma', 'Beef Roll')

# similarly we can also pass dictionary directly without defining it.

def printUsers(**user):
    for k, v in user.items():
        print("{}:{}".format(k,v))

printUsers(name = "Mohsin", age = 29)