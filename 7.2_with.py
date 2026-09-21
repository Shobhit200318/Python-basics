# Best way to open and close a file in read mode using
# 'with', which automatically closes the file

f = open("file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("file.txt", "r") as f:
    # Read the contents of the file
    print(f.read())

# You don't have to explicitly close the file while using with



