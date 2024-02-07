"""user = {
    "name":"bibek",
    "age":"18",
    "country":"nepal",
}

print(user.get("name"))
user.setdefault("father_name","ram")
user["goal"]="greatest of all"
#getting keys of dict
print(user.keys())
#getting values of dict
print(user.values())
#getting values of a dict
user.get("name")
user.get("mother_name","default value if no key present")

breakpoint()"""
"""
write a program get name, age,religion,father_name,mother_name,college_name,
as inputs from terminal.
"""
"""user_detail = {
    name = input("Enter name:\n")
    age = input("enter age:\n")
    religion = input("Enter the religion:\n")
    father_name
}""""""
attrs = ["name","age","religion","father_name","mother_name","college_name"]
user_detail = {}
for i in attrs:
    user_detail.setdefault(i, input(f"Enter your {i}\n"))
user_detail.__setitem__(i, input(f"Enter your {i} \n"))
print(user_detail)
for i in user_detail:
    print(i)
print([i for i in user_detail])
breakpoint()
{}"""

user_detail_first = {
    "name":"bibek",
    "age":"18",
}
    
user_detail_second = {
    "country":"nepal",
    "state":"madhesh"
}
#merging two dict
user_detail = {
    **user_detail_first,
    **user_detail_second,
}
print(user_detail)
#merging two or more lists
student1 = ["ashish","sunil"]
student2 = ["raj","phone"]
student = [*student1,*student2,"9817847087"]
print(student)