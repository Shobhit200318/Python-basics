for i in range(4):
    print(i)

# For loops with lists
l = [1,4,6,234,6,764]
for i in l:
    print(i)

# For Loop with Tuples
t = (6,231,75,122)
for i in t:
    print(i)

# For loop with Strings 
s = "Harry"
for i in s:
    print(i)

# For with else
l = [1,7,8]

for item in l:
    print(item)

else:
    print("done") # this is printed when the loop exhausts!

# break
for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)

# continue
for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    print(i)

# pass 
for i in range(645):
    pass # without pass program will give throw an error

i = 0
while(i<45):
    print(i)
    i += 1

