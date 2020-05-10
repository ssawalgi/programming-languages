#Python program to find the square root

#For positive numbers
num = 4

num_sqrt = num ** 0.5

print('The square root of %0.3f is %0.3f'%(num, num_sqrt))

#Get input from user

def sqrt(number):
    return (number ** 0.5)

num =  float(input('Enter first number: '))
print('The square root of %0.3f is %0.3f'%(num, sqrt(num)))

#For negative and complex numbers
#Importing the complex math module
import cmath

#To take input from user use input() and apply eval() func

num = eval(input('Enter a number: '))

num_sqrt =  cmath.sqrt(num)

print('The square root of {0} is {1}'.format( num, num_sqrt ) )