from datetime import datetime, date 
import time
from math import sqrt, ceil, floor


def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        runtime = round(end - start, 4)

        with open("execution_log.txt", "a") as log_file:
            log_file.write(f"{func.__name__} executed in {runtime} seconds\n")

        return result
    return wrapper











@log_time
def Math_Automation():
    
    while True:
        try:
            numbers=list(map(float,input("enter numbers seprated by comma like that (1,2,3,4) ").strip().split(",")))
            break
        except :
            print("please >> enter numbers seprated by comma like that (1,2,3,4) ")
    
    for num in numbers:
        file = open("math_report.txt", "a")
        f= floor(num)
        file.write(f"floor of number {num} is {f}\n")
        c=ceil(num) 
        file.write(f"ceil of number {num} is {c}\n")
        s=sqrt(num) 
        file.write(f"square root of number {num} is {s}\n")
    
    file.close()
    

    file2 = open("math_report.txt", "r")
    text = file2.read()
    print(text)





@log_time
def datetime_reminder():
    while True:
        user_input = input("Enter a date (YYYY-MM-DD): ").strip()
        try:
            reminder_date = datetime.strptime(user_input, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid format! Please use YYYY-MM-DD (e.g., 2025-12-31).")

    today = date.today()
    delta = (reminder_date - today).days

    if delta < 0:
        print("This date has already passed.")
    else:
        with open("reminders.txt", "a") as file:
            file.write(f"{reminder_date} -> {delta} days left\n")
        print(f"Reminder saved: {reminder_date} -> {delta} days left")


