#1
n = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{n} X {i} = {n * i}")
    
#2
l = ["Ayush", "Shobhit", "Srijan", "Ram", "Arin"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")

#3
n = int(input("Enter a number: "))

i = 1
while(i<11):
    print(f"{n} X {i} = {n * i}")
    i += 1

#4
n = int(input("Enter a number: "))
for i in range(2,n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")

#5 - Sum of first n natural numbers
n = int(input("Enter the number: "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i += 1

print(sum)

#6
# 5! = 1 X 2 X 3 X 4 X 5
n = int(input("Enter the number: "))
product = 1
for i in range(1,n+1):
    product = product * i

print(f"The factorial of {n} is {product}")

#7
'''
For n = 3
  *
 ***
*****

For n = 5
    *
   ***
  *****
 ********
**********

'''
n = int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end= "")
    print("")

#8
n = int(input("Enter the number: "))
for i in range(1,n+1):
    print("*"* i, end ="")
    print("")

#9
'''

***
* *       for n = 3
***

'''
n = int(input("Enter the number: "))
for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*" * n, end= "")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*",end = "")
    print("")

#10
# multiplication table in reverse order
n = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{n} X {11 - i} = {n*(11-i)}")

