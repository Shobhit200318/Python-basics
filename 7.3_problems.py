#1 
f = open("poem.txt")
content = f.read()
if("twinkle" in content.lower()):
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not present in the content")

f.close()

#2
import random
def game():
    print("You are playing the game..")
    score = random.randint(1, 62)
    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score: {score}")
    if(score > hiscore):
        # write this hiscore to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()

#3
# WAP to generate multiplication table from 2 to 4 and
# write it to different files. Place these files in a folder.
def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2,5):
    generateTable(i)


#4
# Replace the word donkey to ###### in a file
word = "Donkey"

with open("file2.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("file2.txt", "w") as f:
    f.write(contentNew)

#5 
# Repeat program 4 for a list of such words to be censored.
words = ["Donkey", "bad", "ganda"]

with open("file2.txt", "r") as f:
    content = f.read()

# We make a copy in lowercase only to check
content_lower = content.lower()

for word in words:
    content = content.lower().replace(word.lower(), "#" * len(word))
# Note: This will convert whole file to lowercase
with open("file2.txt", "w") as f:
    f.write(content)

#6 
# WAP to mine a log file and find out whether it contains 'python'.
with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("Yes python is present")
else:
    print("No Python is not present")


#7 
# WAP to find out the line number where python is present from ques 6.
with open("log.txt") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present. Line no.: {lineno}")
        break
    lineno += 1 
else:
    print("No Python is not present")   

#8
# WAP to make a copy of a text file "this.txt"
with open("this.txt") as f:
    content = f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)

#9 
# WAP to find out whether a file is identical & matches the content of another file.
with open("file.txt") as f:
    content1 = f.read()

with open("poem.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes these files are identical")

else:
    print("No these files are not identical")

#10
# WAP to wipe out the content of a file using python.
with open("this_copy.txt", "w") as f:
    f.write("")

#11 
# WAP to rename a file to "renamed_by_python.txt"
with open("poem.txt") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)

# Better code:
import os
old_name = "para.txt"
new_name = "renamed_by_python.txt"

# Rename the file
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"File renamed from {old_name} to {new_name}")
else:
    print("Old file not found")

##12
# WAP to extract individual words of a paragraph from a file
with open("poem.txt", "r") as f:
    content = f.read()
    a = content.split()
    print(a)

# Clean code:-
# Read file and extract words
with open("renamed_by_python.txt", "r") as f:
    content = f.read()

# split() breaks paragraph into words by space/newline
words = content.split()
print(words)

# If you want one word per line
for word in words:
    print(word)    

# If you don't want new line
    for word in words:
        print(word, end = " ")