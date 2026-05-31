# we create tuple using paranthesis
tup1 = ("Mohsin", 28, False)
# print(tup1)
# we can access tuples elements using indexing
# print(tup1[0])
# print(tup1[0:1])
# print(tup1[1:2])
# print(tup1[0:2])

# we can't add or remove elements from tuple
# We can depack tuple
a,b,c = tup1
# print(a)
# print(b)
# print(c)

tup2 = (2,4,5)
# tuples can be concatenated with only tuples and not with other data types
tup3 = tup1 + tup2
# print(tup3)

tupp = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(tupp[0:]) # 0 is starting while nothing after : mean till end

print(tupp[::-1]) # for printing a complete tuple in reverse.

subTup = tupp[1:4] # It's called slicing means copying / creating sub-tuple from original one.
print(subTup) #for specific range starting from second index and less than index 4 // bcd
