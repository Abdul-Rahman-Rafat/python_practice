# Lab1:
##########



# 	- write a program that prints hello world
print("hello world")





# 	- application to take a number in binary form from the user, and print it as a decimal
binary_num= input("Enter number in Binary form :")
if all(ch in "01" for ch in binary_num):
    print("the decimal number is : ",int(binary_num,2))
else:
    print("please enter 0 or 1")



# 	- write a function that takes a number as an argument and if the number
# 		divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 		divisible by both return "FizzBuzz"
def fun(num):
    if (num % 3  ==0) and (num % 5 ==0) :
        return("FizzBuzz")
    elif num % 3 ==0   :
        return("Fizz")
    elif num % 5 ==0 :
        return("buzz")

print(fun(3))
print(fun(5))
print(fun(15))





# 	- Ask the user to enter the radius of a circle print its calculated area and circumference
circle_radius= input("enter the radius of a circle : ")
pi = 3.14
if circle_radius.isnumeric() :
    circle_radius=float(circle_radius)
    area = float(pi*circle_radius*circle_radius)
    circumference= float(2*pi*circle_radius)
    print(f"area : {area}  circumference : {circumference} ")
else:
    print("enter valid number")    







# 	- Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data
name=input("Enter ur name : ")
if not(name.isnumeric()):
    if name.strip():
        e_mail=input("Enter ur e_mail : ")
        if "@" not in e_mail:
            print("enter domain @")
        else:
            print(f"ur name is : {name} /n e-mail is : {e_mail}")
    else:
        print("enter valid string")
else:
    print("enter valid string")    


# 	- Write a program that prints the number of times the substring 'iti' occurs in a string
str = "ITI is best of the best , iti make ur future"
low_str=str.lower()
freq= low_str.count("iti")

print(freq)
