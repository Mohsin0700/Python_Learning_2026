print("In this file we'll be learning only about list data type")
students = ['Mohsin', 'Arbab']
students.append('Kamran')
print(students)
# As we use .add method in dart here we use .append
# While in python .insert() method is used for adding an element at specific index
students.insert(2, 'Ali')
print("Updated List", students)
# .extend() method takes a list of multiple elements to add at the end of the list
students.extend(['Munawwar', 'Muzammil'])
print("List after extended", students)
# Similarly like other scripting and programming languages we can change the elements of a list using it's index in a square bracket.

# .remove() method takes an element as an argument and removes it from the list
students.remove('Munawwar')
print(students)
# But in case if we have multiple similar elements the it only removes the first one it finds.
students.append("Ali")
print("List with two similar names", students)
students.remove('Ali')
print('List after removing name ALI',students)
# We use pop() method to remove an element from the list. it takes an optional argument as a parameter which is an index. if give it an index it removes item from that specific index. If no index is given it removes last element of the list.
x = students.pop(0)
print("Pop method returns the removed value", x)
# Similarly like pop we have del method in python which deos not return any value
del students[1] # if we try to store it's value the complier will through an error.
# Just like other languages we can also run a loop over list see below example

for n in students:
    print(n)


# .clear() method removes all the item from the list
students.clear()
print('List after clear', students)