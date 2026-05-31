a = 15
b = 4

print("Addition:", a + b)  

print("Subtraction:", a - b) 

print("Multiplication:", a * b)  

print("Division:", a / b) 

print("Floor Division:", a // b)  

print("Modulus:", a % b) 

print("Exponentiation:", a ** b)

# Logical operators are similar as thery were in dart and js
# now we have three new operator in python (and, or, not) let's see some examples...

a = 10
b = 20
print(a == 10 and b == 20) # true
print(a == 10 and b == 15) # false
print(a == 10 or b == 10) # true
print(not a == 10) # false
print(not a == 51) # true

# As I already know about ternery operators which are one line conditional statement. it is little bit different in python.
x = 10
y = 20
z = x if x > y else y
print(z) #must be 20, let's check.