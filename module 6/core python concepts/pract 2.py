# (2) Practical Example 1: How does the Python code structure work? 
name = "steven"  # Name variable

a = 20           # F  number
b = 10           # S  number

mul = a * b      # multiplication
print(mul)       # Print result

# for Loop
 
for i in range(1, 10):  
    if i % 2 == 0:       # Check even or odd
        print("Even")    
    else:
        print("Odd ")  


# loop ( start,stop,step)

for i in range(10,0,-1):
    print(i,end=" ")


# Division input(conditional)

number = int(input("Enter the numerator num: "))  
denominator = int(input("Enter the denominator num: ")) 

#if condition
  
if number >= 0 and denominator != 0:  
    print("Division possible")          
else:
    print("Division is not possible")    


# Add two numbers(typecasting)

fnum = input("Enter the value of fname: ")     #  input
fnum2 = input("Enter the value of fnum2: ")    #  input
result = int(fnum) + int(fnum2)  # Convert and add
print(result)  #print result