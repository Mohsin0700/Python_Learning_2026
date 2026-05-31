# name = "mohsin"
# print(name) # mohsin
# name2 = name.upper() 
# print(name2) # MOHSIN
# name3 = name.lower()
# print(name3) # mohsin
# name4 = name.capitalize()
# print(name4) # Mohsin

name = 'mOhSin'
print(name)
# print(name.capitalize())

name2 = 'aRbAb'
# print(name2, name2.title())

name3 = 'moHSIN'
# print(name3, name3.swapcase())

#casefold() method is similar to lower() method but it removes all other cases and converts it to lowercase

x = name3.casefold()
y = name3.lower()
# print(x)
# print(y)
# print(x.center(10,"*"))
# print(y.center(20,"-"))
# .count() method is used to find occurence of a character in a string

n = name3.count('o')
# print(n)

#  but it does more
# note = "My name is Mohsin Hussain, I was born in Karachi, Pakistan. I am 28 years old. I am a software developer. I am learning python. I am a good learner. My name Mohsin was selected by my Brother"
# myNameCounts = note.count('Mohsin')
# myNameCountsAfterFirstName = note.count('Mohsin',16) # we can also set ending index if we know where it ends.
# print("My Name Counts",myNameCounts)
# print("My Name Counts after first occurence", myNameCountsAfterFirstName)
# .find() method is used to find the index of a character in a string

#.find() methods finds the nearest, very first and lowest index.
# myNameIndex = note.find('Mohsin')
# print(myNameIndex)


# .expandTabs() method in python.
# while working on python often we need to print a table.By default it expends by 8 characters.
# we use \t for tab.

table1 = "Name\tAge\tlocation\tCNIC"
print("Table 1 without expendTab",table1)
print("Table 1 with expendTab",table1.expandtabs())
