def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Select operator:")
print("1. Addition")
print("2. subtraction")
print("3. mutiply")
print("4. divide")
while True:
    choice=input ("Enter choice:")
    if choice in ('1','2','3','4'):
     num1=float(input("Enter first number:"))
     num2=float(input("Enter second number:"))
     
    if choice =='1':
        print("Result:",add(num1,num2)) 
    if choice =='2':
        print("Result:",subtract(num1,num2)) 
    if choice =='3':
        print("Result:",multiply(num1,num2)) 
    if choice =='4':
        print("Result:",divide(num1,num2)) 
    break
else:
    print("Invalid input")

