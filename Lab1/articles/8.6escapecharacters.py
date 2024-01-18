#To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash \ followed by the character you want to insert.

#An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
#txt = "We are the so-called "Vikings" from the north."

#To fix this problem, use the escape character \":
txt = "We are the so-called \"Vikings\" from the north."

#result: We are the so-called "Vikings" from the north.

'''
Code	Result
\'	    Single Quote	
\\	    Backslash	
\n	    New Line	
\r	    Carriage Return	
\t	    Tab	
\b	    Backspace	
\f	    Form Feed	
\ooo	Octal value	
\xhh	Hex value
'''