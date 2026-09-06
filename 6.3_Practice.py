#1 

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
    
a = 1
b = 23
c = 3

print(greatest(a, b, c))

#2 
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c,2)} °C")

#3
# Python print() function to print a new line at the end
print("a")
print("b")
print("c", end = "")
print("d", end = "")

#4 - Sum of first n natural numbers using recursion
'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4.... n -1 + n
sum(n) = sum(n-1) + n
'''

def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n

print(sum(4))

#5 - Star pattern
def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(3)

# 6 -  Inches to Centimeters
def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))
print(f"The corresponding value in cms is {inch_to_cms(n)}")


#7 
# WAP to remove a given word from a list and strip it at the same time.
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Harry", "Rohan", "Shubham", "an"]

print(rem(l,"an"))

#8 
# WAP to print multipication table of a given number.
def multiply(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

multiply(5)