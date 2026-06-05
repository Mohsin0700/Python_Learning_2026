name = "Mohsin"
reversedName = ""
print(len(name))
for x in range(len(name) - 1 , -1, -1):
    print(name[x])
    reversedName = reversedName + name[x]

print("Reversed Name:::::", reversedName)