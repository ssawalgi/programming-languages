#There are multiple ways to add two numbers. This exercise showcases different ways to add two numbers in python

#One way - simple addition of two nos

print(2+5)

#Alternate way

num1 = 2
num2 = 5
sum = num1 + num2
print(sum)

#Alternate way
def sum(num1, num2):
    return(num1+num2)

result = sum(2, 5)
print(result)

num1 = input("Enter first number:")
num2 = input("Enter second number: ")
#TODO::find out why conversion in required
result = sum(int(num1), int(num2))
print("Sum of {0} and {1} is: {2}" .format(num1, num2, result))