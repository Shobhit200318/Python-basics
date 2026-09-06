e = set() #Empty set 
# Don't use e = {} as it will create an empty dictionary
# Set is a collection of non-repetitive elements and sets are unindexed
s = {1, 5, 32, 5, 54, 5, "Shobhit"}
#print(s, type(s))

# set methods
s.add(566)
s.remove(1)
# s.pop() # Removes Random Element from the set
# s.clear() # Empties the set s
print(s,type(s))
print(len(s))


s1 = {1,45,6}
s2 = {7,8,1,78}
print(s1.union(s2))
print(s1.intersection(s2))

s3 = {1, 23, 45}
s4 = {6, 1, 3, 34, 23, 54}
print(s3 - s4) 

# practice 
# 1
words = {
    "madad" : "Help",
    "kursi" : "Chair",
    "billi" : "Cat"
}
word = input("Enter the word you want meaning of: ")
print(words[word])

#2
s = set()
n = input("Enter number 1: ")
s.add(int(n))
n = input("Enter number 2: ")
s.add(int(n))
n = input("Enter number 3: ")
s.add(int(n))
n = input("Enter number 4: ")
s.add(int(n))
n = input("Enter number 5: ")
s.add(int(n))
n = input("Enter number 6: ")
s.add(int(n))
n = input("Enter number 7: ")
s.add(int(n))
n = input("Enter number 8: ")
s.add(int(n))

print(s)

#3
s = set()
s.add(18)
s.add("18")

print(s) 

# 4
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(s)
print(len(s))
# 20(int) == 20.0(float) in python are equal


# 5
s = {}
print(type(s))

#6
d = {}
name = input("Enter friends name: ")
lang = input("Enter Language name ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

print(d)