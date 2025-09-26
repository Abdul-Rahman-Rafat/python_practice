from math import sqrt,ceil,floor 

def Math_Automation():
    
    while True:
        try:
            numbers=list(map(float,input().strip().split(",")))
            break
        except :
            print("enter numbers seprated by comma like that (1,2,3,4) ")
    
    for num in numbers:
        file = open("math_report.txt", "a")
        f= floor(num)
        file.write(f"floor of number {num} is {f}\n")
        c=ceil(num) 
        file.write(f"ceil of number {num} is {c}\n")
        s=sqrt(num) 
        file.write(f"square root of number {num} is {s}\n\n\n")
    
    file.close()
    

    file2 = open("math_report.txt", "r")
    text = file2.read()
    print(text)




