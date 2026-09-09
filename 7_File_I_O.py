# File I/O - File - Input/Output
'''
a = "a very long string with emails"

emails = []
3 seconds
'''
# Reading a file
f = open("file.txt", "r") 
# in open() function by default mode is read ("r").
data = f.read()
print(data)
f.close()

# Writing a file
st = "Hey Shobhit you are amazing"
f = open("myfile.txt", "w")

f.write(st)

f.close()