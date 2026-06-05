student = {
    "name": "Mohsin",
    "age": 29,
}

print(student)

# it can also be created using constructor / function

student2 = dict(name = "Hasan", age = 29)
print(student2)

# we can get a key's value in using following ways

print(student["name"])
print(student2.get("name"))

# adding and updating key is similar to dart. to delete a dictionary item
student["location"] = "Karachi"


del student["age"]
print(student)

val = student2.pop("name")
print("poped value is::: ", val)
print("Student 2 Data ::::", student2)

print(student.popitem()) #It deletes and return last added item.
print(student)

# Let we have a map/dict containing employee details

employee = {
    "name" : "Mohsin",
    "age" : 29,
    "role" : "Software Engineer",
    "unit" : "MBS",
    "Company" : "Maccorp"
}

print(employee)
print("*" * 100)
print("Printing Keys and values")
for key in employee:
    print("Key:::::", key)

for val in employee.values(): 
    print("Value::::::::::", val)


print("#"*100)
print("Printing key-value pairs")

for key,val in employee.items():
    print("KEY -> ", key, ":", val, "<- VAL")