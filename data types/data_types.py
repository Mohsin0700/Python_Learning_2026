print("Python Data Types")
# Let's Start From Numeric Data Types

# *************************************************************************
# NUMERIC DATA TYPES
print('###########################---Numeric Data Types---#############################')
# In python there are three numeric data types
# (01) Integer int just like dart.

x = 8
print(type(x))

# (02) Float just like double in dart.
x = 12.5
print(type(x))

# (03) Complex, this is a new type which I'm learning in Python. It stores real and imaginery numbers.

x = 2 + 4j
print(x, type(x))

print('###########################---Sequence Data Types---#############################')
# A sequence is an ordered collection of items, which can be of similar or different data types. Elements in a sequence can be accessed using indexing.
# (01) String, represented by str in python String in dart and typescript.
note = "My Name is Mohsin Hussain"
note2 = 'I am learning python'
note3 = ''''When we write String in three single
qoutes or three double qoutes our string becomes 
multiline which is not allowed in single or double
qoutes and not in Dart or javascript'''

print(note, note2,note3)
print("String type is: ", type(note))
# We can also get an specific character using it's index as string in python is sequence data type.
print(note[11])
print(note[-14])