"""
def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")
a = 9
b = 8 
isGreater(a, b)
calculateGmean(a,b)
c = 8
d = 8
isGreater(c, d)
calculateGmean(c,d)
"""

# Function Arguments
"""
def average(a,b,c=1):
    print("The Average is", (a+b+c)/2)

average(4,6)
"""

# Using arguments/iterable

def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))

average(5,6,7,1) 
average(3,7,4,6)

def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Singh", lname = "Dhoni", fname = "Mahendra")