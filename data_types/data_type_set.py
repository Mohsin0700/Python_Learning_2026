# Sets are similar like a list but it's element are unordered and we use curly braces {} in sets.
# It's items are usually access through a loop. Futhermore it depricates duplicate values and each time order of it's item can vary
childrens = {"Khizar", "Yaman", "Rayan", "Rohan", "Rayan", "Meesum"}
print("First Print", childrens)
print("Second Print", childrens)
# we use .add method for sets
childrens.add("Abbas")
print(childrens)

# As we have set data type in python there is another data type which is frozenset which can't be changes like set or list.
# Normal set
nomralSet = set(["Mohsin", "Arbab", "Habeeb", "Kamran"])
frozenSet = frozenset(["Hafiz","Muhammad", "Mohsin"])
print("Normal Set: ",nomralSet, " and it's type is ", type(nomralSet))
print("Frozen Set: ",nomralSet, " and it's type is ", type(frozenSet))
# A frozenset supports common set operations such as 
# union, 
# intersection,
# difference and symmetric difference.
# Although it is immutable, these operations return new frozenset objects without modifying the original sets.
a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])

c = a.copy()
print(c)

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

# a.copy() creates a copy of a.
# a.union(b) combines elements of both sets.
# a.intersection(b) returns common elements.
# a.difference(b) returns elements only in a.
# a.symmetric_difference(b) returns elements that are not common to both sets.