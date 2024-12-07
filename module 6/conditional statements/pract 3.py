# (3) Write a Python program to calculate grades based on percentage using 
# if-else ladder. 

marks = int(input("Enter your marks: "))

if marks<=100:
    if marks >=70:
        print("A ")
    elif marks>=60 and marks<70:
        print("B ")
    elif marks>=50 and marks<60:
        print("C ")
    else:
        print("fail")
else:
    print("Invalid mark !!!")