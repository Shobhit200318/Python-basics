# x=2
# y=5
# print((x//y))
# print(x-y)
# print(x%y)
# print(x**y)
# Fruit = "I like apple,mangoes,anime"    
# print(Fruit.split(','))
# s1 = {1,"a",True,2,"b",False}
# s1.update([10,20,30])
# print(s1)
# s1 = {1,2,3,4,5,6}
# s2 = {5,6,7,8}
# s3 = s1.intersection(s2) 
# print(s3)
fruit1 = {"Apple":10,"Orange":20}
fruit2 = {"Banana":30,"Guava":40}
fruit1.update(fruit2)
print(fruit1) 

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()