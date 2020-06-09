def greet( name ):
    print("Hello "+ name +". Welcome to Python world")

name= input("Whats your name?")    
greet(name)

def addSix(x):
    print(5 +  x)

addFive(5)

addFive(62.5)

#addFive("Hi Five!")

def addFive(x):
    return(5 +  x)

print(addFive(5))

print(addFive(62.5))

#nested funcs

def outerfunc():
    print('Inside outer func')
    def innerfunc():
        print('Inside inner func')
    innerfunc()
outerfunc()


#Random module

import random

#find random number from first 100 numbers
random_num = random.randint(1, 100)
print(random_num)

#find random skills to learn today

skills = ["JSON", "JAVA", "Python", "SQL", "HADOOP", "ELASTIC SEARCH", "JIRA", "AGILE", "TABLEAU", "MS EXCEL"]

learn_skills = random.choice(skills)

print(learn_skills)

for i in range(4):
    print(i)
