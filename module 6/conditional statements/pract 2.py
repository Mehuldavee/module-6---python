#  (2) Write a Python program to check if a number is prime using if_else. 

n = int(input("Enter any number:"))
if n>1:
    for i in range(2,n):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            break 
        
    else:
        print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number.")