#Create an empty dictionary called my_dict. Add three key-value pairs: 'name' with a value of 'john','age' with value of 25, and 'city' with a value of 'New York'.
my_dict ={}
my_dict['name']="John"
my_dict['age']=20
my_dict['city']='New York'
print(my_dict)

#Write a function merge_dicts(dicts1,dicts2) that takes two dictionarise as arguments and return a new dictionary containing the
def merge_dicts(dicts1,dicts2):
    merge_dicts=dicts1.copy()
    merge_dicts.update(dicts2)
    return merge_dicts
print(merge_dicts)


grades = {
    "alice": 90,
    "Bob":85,
    "charlie":92
}
average_grade = sum(grades.values())/len(grades)
print("Average grade:",average_grade)