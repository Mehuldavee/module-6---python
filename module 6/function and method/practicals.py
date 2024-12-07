# (1) Write a Python program to print "Hello" using a string. 
# (2) Write a Python program to allocate a string to a variable and print it. 
# (3) Write a Python program to print a string using triple quotes. 

str = "hello"
str_1 = 'hello'
str_2 = """hello"""
print(f"{str}\n{str_1}\n{str_2}")

# (4) Write a Python program to access the first character of a string using 
# index value. 
str = "python"
print(str[0])

# (5) Write a Python program to access the string from the second position 
# onwards using slicing. 
str = "hello nice to meet you"
print(str[1:])

# (6) Write a Python program to access a string up to the fifth character. 
print(str[:6])

# (7) Write a Python program to print the substring between index values 1 
# and 4. 
print(str[1:5])

# (8) Write a Python program to print a string from the last character. 
print(str[-1])

# (9) Write a Python program to print every alternate character from the 
# string starting from index 1.
print(str[1::2])