#1. Create and print a dictionary storing your information
info = {
    "name": "Archisha",
    "age": 21,
    "gender": "Female",
    "course": "Computer Science"
}
print(info)

#2. Access items of a dictionary using its key
print("Name:", info["name"])
print("Age:", info["age"])

#3. Get a list of values from a dictionary
values = list(info.values())
print(values)

#4. Change the value of a specific item using its key
info["age"] = 22
print(info)

#5. Print all key names one by one
for key in info:
    print(key)

#6. Create a dictionary that contains three nested dictionaries
students = {
    "student1": {"name": "Rahul", "age": 20},
    "student2": {"name": "Anita", "age": 21},
    "student3": {"name": "Kiran", "age": 22}
}
print(students)

#7. Create three dictionaries and store them inside one dictionary
dict1 = {"Math": 85}
dict2 = {"Science": 90}
dict3 = {"English": 88}
marks = {
    "Subject1": dict1,
    "Subject2": dict2,
    "Subject3": dict3
}
print(marks)

#8. Convert two lists into a dictionary
list1 = ["name", "age", "gender"]
list2 = ["Archisha", 21, "Female"]
result = dict(zip(list1, list2))
print(result)

#9. Merge two dictionaries into one
dictA = {"a": 10, "b": 20}
dictB = {"c": 30, "d": 40}
merged_dict = dictA | dictB
print(merged_dict)

#10. Get the key of the lowest value from the dictionary
sample_dict = {
    'C': 92,
    'Java': 66,
    'Python': 85
}
lowest_key = min(sample_dict, key=sample_dict.get)
print("Key with lowest value:", lowest_key)

