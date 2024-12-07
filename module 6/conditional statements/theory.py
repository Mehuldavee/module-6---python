""" 
(1)Introduction to conditional statements: if, else, elif. 
*  Nested if-else conditions. 

1. if, else, and elif

if   =  Checks a condition and executes the block if true.

elif =  Checks another condition if the if condition is false.

else =  Executes when all conditions are false.

 * syntax :
 ------------

if condition1:
    # Executes if condition1 is true
elif condition2:
    # Executes if condition1 is false and condition2 is true
else:
    # Executes if none of the conditions are true

2. Nested if-else
A nested if-else places one if or else inside another for more complex decisions.

When is it used?

When a decision depends on multiple conditions, one within another.

syntax :
----------

if condition1:
    if condition2:
        # Executes if both condition1 and condition2 are true
    else:
        # Executes if condition1 is true but condition2 is false
else:
    # Executes if condition1 is false

conlsusion:-
---------------
Use if:For the first condition to be checked.

Use elif: execute when the if condition is false.

Use else:For the fallback code when all conditions fail.

Nested if-else:Use it when a condition depends on another condition.
"""