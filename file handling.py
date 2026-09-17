# file handling includes opening, reading, writing, and closing files in Python. 

# Read mode is used to read the contents of a file.it give an error if the file does not exist.

Example: 1
f = open(r"comments.py", "r")
print(f)
text = f.read()
print(text)
f.close()

# Write mode is used to write data to a file.
# If the file does not exist, it will create a new file. If the file already exists, it will overwrite the existing content.
# Example: 2
f = open(r"comments.py", "w")
f.write("Hello, World!")
f.close()