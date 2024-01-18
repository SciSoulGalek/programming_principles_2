#Strings in python are surrounded by either single quotation marks, or double quotation marks.
#'hello' is the same as "hello"

#-------------------

#You can assign a multiline string to a variable by using three quotes:
#You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Or three single quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#in the result, the line breaks are inserted at the same position as in the code.

#-------------------

#Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

#result: e

#-------------------

#Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
  print(x)

#result:
'''
b
a
n
a
n
a
'''

#-------------------

#To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))

#result: 13

#-------------------

#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

#result: True

#Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#-------------------
  
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)

#Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")