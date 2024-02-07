num1 = [2,4,6,8,10]
sum=sum(num1)
print("The sum of list:",sum)

num1.insert(5,12)
print(num1)
num2 = [1,3,5,7,9]
num1.extend(num2)
print(num1)

num3 = [1,2,3,4,3,5,6,1,3]
unique_list =list(set(num3))
print("After removing the duplicate number:",unique_list)

