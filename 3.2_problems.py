# Problem 1
# name = input("Enter your name: ")
# print(f"Good Afternoon, {name} ")

# Problem 2
letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''
print(letter.replace("<|Name|>", "Shobhit").replace("<|Date|>", "29 July 2026"))

# Problem 3
name = "Shobhit is a good  boy and "
print(name.find("  "))

# 4
name = "Shobhit is a good  boy and "
print(name.replace("  ", " ")) 
print(name) # name string didn't change as Strings are immutable which
# means that you cannot change them by running functions on them

# 5
letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"
print(letter)

