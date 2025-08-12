5 Quick Review Questions (Post-lecture)
How do you print "Hello, World!" in Python?


What is the purpose of comments in code?
Purpose of comment is to stop execution of particular command

Which function is used to get input from the user?

python3 main.py (file Extension name is used to get input from user )


How do you run a Python script from the command line?
by entering a command in inverted quotes


What is the difference between Python 2 and Python 3? (basic idea)
Basic Syntax and Print
Write a Python program to print your name.
Ans:
name = input("Enter your name: ")
print(name)


Print the numbers from 1 to 5 on separate lines.
Ans : a = """1
2
3
4
5"""
print (a)



Print the following exactly as shown:

 Hello,
Python!

Ans : a = """Hello,
Python!"""
print (a)


Write a program to print the sum of two numbers: 10 and 20.


Print a multiline string using triple quotes.

Ans : print(3+3)

What happens if you forget the closing quotation mark on a string? Test and explain.
Ans :When we forget closing quotation mark on string say 
	a = "hello world
	print (a)
it gives an error which is sytax error.						
PS C:\Users\retes\OneDrive\Desktop\Python> python3 main.py
  File "C:\Users\retes\OneDrive\Desktop\Python\main.py", line 1
    a = "hello world
        ^
SyntaxError: unterminated string literal (detected at line 1)


Write a comment explaining what print() does.
Print gives the output of command the user inputs 
say : a = 10+20
	print (a) will give output as : 30


Write a program to print the phrase: Python is fun!
Ans : a = "Python is fun!"
	print (a)


Print the result of 7 + 3.
Ans : a = 7 + 3
print (a)

Output on running is 10



What is the output of print(2 * 5)?
Ans : a = 2 * 5
print (a)
 Output is 10


User Input and Data Types
 11. Write a program that asks the user for their age and prints it.
Ans : age = input("Enter your age: ")
	print (age)


 12. What data type is returned by the input() function?
Ans : () it is used to call a function eg : print ("Hello World")

 13. Convert the user input for age into an integer and print the result.
Ans : age = input("Enter your age: ")
print (age)
print (int(age))


 14. Write a program that asks for two numbers and prints their sum.
 Ans : a = int(input("Enter a number :"))
b = int(input("Enter a number : "))
sum = a + b
print(sum)

 15. What happens if you add a string and an integer in Python?
Ans : a = int(input("Enter a number :"))
b = int(input("Enter a name : "))
sum = a + b
print(sum)

Enter a number :3
Enter a name : Retesh
Traceback (most recent call last):
  File "C:\Users\retes\OneDrive\Desktop\Python\main.py", line 2, in <module>
    b = int(input("Enter a name : "))
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'Retesh'


Errors and Debugging
 16. Write a program that will cause a syntax error. Explain the error.

 a = 10
b = 20
print(bool(a b))


PS C:\Users\retes\OneDrive\Desktop\Python> python3 main.py
  File "C:\Users\retes\OneDrive\Desktop\Python\main.py", line 3
    print(bool(a b))
               ^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?

 17. What error will be raised if you try to print a variable that does not exist? 
a = For
print(a)

PS C:\Users\retes\OneDrive\Desktop\Python> python3 main.py
Traceback (most recent call last):
  File "C:\Users\retes\OneDrive\Desktop\Python\main.py", line 1, in <module>
    a = For
        ^^^
NameError: name 'For' is not defined
 18. Fix the following code snippet:
print("Hello World)

What is indentation, and why is it important in Python?
print ("hello world")
  print ("I am funny")
    
PS C:\Users\retes\OneDrive\Desktop\Python> python3 main.py
  File "C:\Users\retes\OneDrive\Desktop\Python\main.py", line 2
    print ("I am funny")
IndentationError: unexpected indent

Try running print("Hello" + 5) and explain the error.

PS C:\Users\retes\OneDrive\Desktop\Python> python3 main.py 
Traceback (most recent call last):
  File "C:\Users\retes\OneDrive\Desktop\Python\main.py", line 1, in <module>
    print("Hello" + 5)
          ~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
Can only add str to str not an integer

Miscellaneous
 21. What is the file extension of Python files? = .py
 22. How do you write a single-line comment? = Print("I have a class")
 23. Can Python variables start with numbers? Try and explain. No it cannot start with number as these are illegal variable which gives error for eg : 

2A = "Retesh"
print (2A)

PS C:\Users\retes\OneDrive\Desktop\Python> python3 main.py
  File "C:\Users\retes\OneDrive\Desktop\Python\main.py", line 1
    2A = "Retesh"
    ^
SyntaxError: invalid decimal literal


 24. Write a Python program that prints your favorite quote. = print ("No pain no gain")

 25. How to write a multiline comment in Python? using print ("""Hello
lets
have 
fun"""
)
 26. What happens if you print a number without quotes? 
Ans :
print(1)

PS C:\Users\retes\OneDrive\Desktop\Python> python3 main.py
1

print 1
PS C:\Users\retes\OneDrive\Desktop\Python> python3 main.py
  File "C:\Users\retes\OneDrive\Desktop\Python\main.py", line 1
    print 1
    ^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)

 27. Write a program that prints both single and double quotes inside a string.
 28. What is the output of print("5" * 3)?
here 5 is a variable which is printed three times 

 29. Write a program that prints the result of 100 / 4.
 30. Explain what the Python interpreter does.

