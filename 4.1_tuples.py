my_tuple = (1,2,3)
a,b,c = my_tuple
print(a,b,c)

fruits = []

marks = []

f1 = int(input("Enter Marks here: "))
marks.append(f1)
f2 = int(input("Enter Marks here: "))
marks.append(f2)
f3 = int(input("Enter Marks here: "))
marks.append(f3)
f4 = int(input("Enter Marks here: "))
marks.append(f4)
f5 = int(input("Enter Marks here: "))
marks.append(f5)
f6 = int(input("Enter Marks here: "))
marks.append(f6)
f7 = int(input("Enter Marks here: "))
marks.append(f7)
marks.sort()

print(marks)

l = [3,3,5,1]
print(sum(l))

a = (7,0,8,0,0,9)

n = a.count(0)
print(n)

# LM -> List - mutable.
# SI -> String - Immutable
# TI -> Tuple - Immutable
# DM -> Dictionary - Mutable