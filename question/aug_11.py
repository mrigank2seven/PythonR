# Print "Hello, World!" to the console
print("Hello, World!")

# Get input from the user and store it in the variable 'name'
name = input("Enter your name: ")

# Print the value stored in 'name'
print(name)

# Print numbers from 1 to 5 on separate lines using a multiline string
a = """1
2
3
4
5"""
print(a)

# Print exactly the following string on separate lines
a = """Hello,
Python!"""
print(a)

# Print the sum of two numbers: 10 and 20
print(10 + 20)

# Print a multiline string using triple quotes
print("""This is a
multiline string
example.""")

# Example of a syntax error: missing closing quotation mark on a string
# a = "hello world
# print(a)
# This will raise a SyntaxError: unterminated string literal

# Explain print() function:
# print() outputs whatever is passed inside its parentheses to the console
a = 10 + 20
print(a)  # Outputs: 30

# Print the phrase "Python is fun!"
a = "Python is fun!"
print(a)

# Print the result of 7 + 3
a = 7 + 3
print(a)  # Outputs: 10

# Print the result of 2 * 5
a = 2 * 5
print(a)  # Outputs: 10

# Ask the user for their age and print it
age = input("Enter your age: ")
print(age)

# input() returns a string data type
# To convert it to integer use int()

# Convert user input for age to integer and print it
age = input("Enter your age: ")
print(age)         # Prints string input
print(int(age))    # Converts to integer and prints

# Ask for two numbers from the user and print their sum
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
sum = a + b
print(sum)

# What happens if you add string and integer in Python?
# This will cause a TypeError because you cannot add str and int directly.

# Example causing SyntaxError:
# a = 10
# b = 20
# print(bool(a b))
# This will raise SyntaxError: missing comma or operator between 'a' and 'b'

# Example causing NameError when printing undefined variable:
# a = For
# print(a)
# 'For' is not defined, so Python raises NameError

# Fix the code snippet with missing quote:
# print("Hello World")

# Indentation is important in Python to define code blocks.
# Wrong indentation causes IndentationError.

# Example:
# print("hello world")
#  print("I am funny")  # Indented unexpectedly - raises error

# Try running print("Hello" + 5)
# Raises TypeError because you cannot concatenate str and int

# Python file extension is '.py'

# Single-line comments start with '#'

# Python variables cannot start with numbers. Example:
# 2A = "Retesh"  # SyntaxError

# Print favorite quote
print("No pain no gain")

# Multiline comment can be done using triple quotes in a string (not exactly a comment but used as multiline string)
print("""Hello
lets
have
fun""")

# Printing a number without quotes outputs the number itself
print(1)

# To print quotes inside a string, use escaping or different quote types:
print('She said "Python is fun!"')
print("It's a nice day!")

# Output of print("5" * 3) is "555" because string '5' is repeated 3 times
print("5" * 3)

# Print the result of 100 divided by 4
print(100 / 4)  # Outputs: 25.0

# Python interpreter executes the code line by line translating it to machine code and running it.