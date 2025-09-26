import task1
import task2
import task3
import task4
import task5
import task6
import task7


def main():
    ######## the script
    print("The Current Functions \n " \
    "1- function Math Automation \n 2- function Regex Log Cleaner \n 3- function datetime_reminder \n 4- function product_data_transformer \n 5- function os_file_manager \n 6- function Random_Data_Generator \n 7- function decorators with Math_Automation \n 8- function decorators with datetime_reminder \n")
    while True:
        try:
            choice = int(input("Enter num of the function u need (enter 0 to exit) : "))
            match choice:
                case 0:
                    print("Good bye!")
                    break
                case 1:
                    task1.Math_Automation()
                case 2:
                    task2.Regex_Log_Cleaner() 
                case 3:
                    task3.datetime_reminder()       
                case 4:
                    task4.product_data_transformer()
                case 5:
                    task5.os_file_manager()
                case 6:
                    task6.Random_Data_Generator()
                case 7:
                    task7.Math_Automation()

                case 8:
                    task7.datetime_reminder()
                
            
                case _:
                    print("Invalid choice") 
            reply=input("wanna to continue ? n or y  : ")
            if reply=="y" or reply=="Y" :
                continue    
            elif reply=="n" or reply=="N":
                print("Good bye!")
                break
        except ValueError:
            print("please enter a number ")


if __name__ == "__main__": 
    main()