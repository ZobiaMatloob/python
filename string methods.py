# Split method
text = "Hello, World!"
result = text.split(", ")
print(result)  # Output: ['Hello', 'World!']

# Join method
words = ['Hello', 'World!']
result = " ".join(words)
print(result)  # Output: 'Hello World!'

# Format method
name = "Alice"
age = 30
message = "Hello, my name is {} and I am {} years old.".format(name, age)
print(message)  # Output: 'Hello, my name is Alice and I am 30 years old.'

# F-String method 
name = "Alice"
age = 30
message = f"Hello, my name is {name} and I am {age} years old."
print(message)  # Output: 'Hello, my name is Alice and I am 30 years old.'