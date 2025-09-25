# 1 - Ask the user to enter 5 numbers. 
# # Store them, then display them in ascending order and descending order.

def sort_nums():
    lista=[]
    count=0
    while count <5:
        
        try:
            n=float(input(f"enter the number {count+1} : "))
            lista.append(n)
            count=count+1
        except ValueError:
            print("enter valid number like 2 or 1.5 etc...")

    print(f"ascending order of the numbers is {sorted(lista)}")
    print(f"descending order of the numbers is {sorted(lista,reverse=True)}")



###################

# 2 - Write a function that takes two numbers: (length, start).
#         Generate a sequence of numbers with the given length,
#         starting from the given start number and increasing by one each time.
#         Print the result.

def increaseOne(length=0, start=0):
    lengthinput=int(input("enter length : "))
    start1=float(input("enter the start : "))

    length=lengthinput
    start=start1

    sequence = []  
    for i in range(length+1):
        sequence.append(start + i)   
    print(sequence)



###################


#3 - Keep asking the user for numbers until they type "done".
        # When finished, print:
        #     * The total of all numbers entered
        #     * The count of valid entries
        #     * The average
        # If the user enters something invalid, show an error and continue.



def count_until_done():
    lista=[]
    while True:
        num=input("enter num : ")
        if num.isdigit() :
            num=float(num)
            lista.append(num)

        elif num=="done" or num=="DONE" :
            break

        else:
            pass


    print(f"total of nums is {sum(lista)}  , count of nums is {len(lista)}  , average of nums is {sum(lista)/len(lista)} ")
            


    ###################    

#   4 - Ask the user to enter a list of numbers.
#         Remove any duplicates, sort the result, and display it.

def list_num():
    while True:
        try:
            listOf_nums = list(map(int,input("enter numbers sepreted by space ").split()))
            rem_dup= set(listOf_nums)
            sorted_nums= sorted(rem_dup)
            print(f"sorted unique nums : {sorted_nums}")
            break
            
        except ValueError:
            print("enter valid numbers")
    
    


###################

    # 6 - Ask the user to enter a sentence.Count how many times each word appears in the sentence and display the result.

def count_word():
    sentence=input("Enter sentence : ")
    words = sentence.split(" ")
    unique_words=set(words)
    for w in unique_words:
        print(f"word : {w}  appears {words.count(w)} times")




###################

#  7 - Create a small gradebook system:
#         - The user enters 5 students names and their scores.
#         - At the end, show:
#             * The highest score
#             * The lowest score
#             * The average score.

def gradebook_sys():
    dicta={}
    for _ in range(5):
        while True:
            try:       
                name=input("Enter student name : ")
                score=float(input("Enter student score : "))
                dicta[name]=score
                break
            except ValueError:
                print("valid value for name is string , valid value for score is number  ")
    
    print(f"The highest score is : {max(dicta.values())} /n, The lowest score is : {min(dicta.values())}   /n, The average score is : {round(sum(dicta.values())/len(dicta.values()),1)}  ")





###################

# 8 - Write a program that simulates a shopping cart:
#         - The user can add items with a name and a price.
#         - The user can remove items by name.
#         - The user can view all items with their prices.
#         - At the end, display the total cost.

def shopping():
    dicta={}
    
    while True:
        while True:
            try:       
                name=input("Enter item name : ")
                price=float(input("Enter item price : "))
                dicta[name]=price
                break
            except ValueError:
                print("valid value for name is string , valid value for price is number  ")
        print(f"the items u add them are : {dicta.items()}")
        reply=input("need to add more ? enter (y or n)")
        if reply=="y" or reply=="Y" :
            continue
        elif reply=="n" or reply=="N":
            break 
    while True:
        reply2=input("need to remove item ? enter (y or n)")
        if reply2=="y" or reply2=="Y" :
            rv_item=input("Enter item name : ")
            dicta.pop(rv_item)
            print(f"the current items are : {dicta.items()} ")
        elif reply2=="n" or reply2=="N":
            break 
    print(f"the total cost is : {sum(dicta.values())}")
        


###################

import random

def guess():
    number = random.randint(1, 20)   
    attempts = 0

    print(" guess a number between 1 to 20 ?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print(" choose a number bigger than taht")
            elif guess > number:
                print(" choose a number less than taht")
            else:
                print(f" correct, The number was {number}.")
                print(f" u guessed  {attempts} attempts.")
                break
        except ValueError:
            print(" Please enter a valid number.")




######## the script
print("The Current Functions \n " \
"1-sort_nums function \n 2-increaseOne function \n 3-count_until_done function \n 4-list_num function \n 5-count_word function \n 6-gradebook_sys function \n 7-shopping function \n 8-guess function \n")
while True:
    try:
        choice = int(input("Enter num of the function u need (enter 0 to exit) : "))
        match choice:
            case 0:
                print("Good bye")
                break
            case 1:
                sort_nums()
            case 2:
                increaseOne()   
            case 3:
                count_until_done()        
            case 4:
                list_num()
            case 5:
                count_word()
            case 6:
                gradebook_sys() 
            case 7:
                shopping()
            case 8:
                guess()         
            case _:
                print("Invalid choice") 
        reply=input("wanna to continue ? n or y")
        if reply=="y" or reply=="Y" :
            continue    
        elif reply=="n" or reply=="N":
            break
    except ValueError:
        print("please enter a number ")
        
