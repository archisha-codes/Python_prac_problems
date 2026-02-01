# 1.  Write a python program to create and print a dictionary which stores your information. (name, age, gender .....)

dict1={"name":'Rohan Vij',"age":'19',"gender":'male'}
print(dict1)

# 2. Write a python program to access the items of a dictionary by referring to its key name.

dict2={"name":'Rohan Vij',"age":'19',"gender":'male'}
print(dict2["name"])

# 3.  Write a python program to get a list of the values from a dictionary

dict3={"name":'Rohan Vij',"age":'19',"gender":'male'}
print(list(dict3.values()))

# 4. Write a python program to change the value of a specific item by referring to its key name.

dict4={"name":'Rohan Vij',"age":'19',"gender":'male'}
dict4["age"] = 18
print(dict4)

# 5. Write a python program to print all key names in the dictionary, one by one.

dict5={"name":'Rohan Vij',"age":'19',"gender":'male'}

for key in dict5:
    print(key)

# 6. Write a python program to create a dictionary that contains three dictionaries. (nested)

dict6 = {
    "student1": {"name": "Aman", "age": 18},
    "student2": {"name": "Riya", "age": 19},
    "student3": {"name": "Rohan", "age": 18}
}

print(dict6)

# 7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.

d1 = {"name": "Rohan"}
d2 = {"age": 19}
d3 = {"gender": "Male"}

combined = {
    "dict1": d1,
    "dict2": d2,
    "dict3": d3
}

print(combined)


# 8. Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.


list1 = ["name", "age", "gender"]
list2 = ["Rohan", 18, "Male"]

result = dict(zip(list1, list2))
print(result)


# 9. Write a python program to merge two python dictionaries into one dictionary.

dic1 = {"a": 1, "b": 2}
dic2 = {"c": 3, "d": 4}

dic1.update(dic2)
print(dic1)

# 10. Write a python program to get the key of lowest value from the dictionary. sample_dict = {
# 'C': 92,
# 'Java': 66,
# 'Python': 85
# }

marks = {
    "C": 92,
    "Java": 66,
    "Python": 85
}

print(min(marks, key=marks.get))