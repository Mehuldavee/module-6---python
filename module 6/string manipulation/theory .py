
"""Understanding how to access and manipulate strings. 
Basic operations: concatenation, repetition, string methods (upper(), lower(), etc.). 
String slicing. 

-->Concatenation: The + operator combines two strings into one.

Ex 1 : "what are" + " you doing" results in "what are you doing".
Repetition: The * operator repeats a string multiple times.

Ex 2 : "hyyy " * 3 results in "hyyy hyyy hyyy ".
String Methods:

.upper(): Converts all characters in the string to uppercase.

.lower(): Converts all characters in the string to lowercase.

.title(): Capitalizes the first character of each word.


String Slicing:
-----------------

You can extract parts of a string using slicing: string[start:end].
Example: "Hello World"[0:5] results in "Hello".

Negative Indexing:
---------------------

Negative indices allow you to count from the end of the string.
Example: str[-1] gives the last character.

Advanced Slicing:
-------------------

You can also define a step size in slicing: string[start:end:step].
Example: "Hello World"[0:10:2] results in "Hoo ol".
String Length: len() function give the length of the string.

Example: len("Hello") returns 5.
String Membership: The in operator checks if a substring exists in a string.

Example: 'Hello' in 'Hello World' returns True.

"""