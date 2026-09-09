f = open("file.txt")

# lines = f.readlines()
# print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5 =="")

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()


# Modes of opening a file
# r - open for reading
# w - open for writing
# a - open for appending
# + - open for updating
# 'rb' will open for read in binary mode.
# 'rt' will open for read in text mode.

# Append 
st = "Shobhit you are amazing"

f = open("myfile.txt", "a")

f.write(st)
f.close()

