import csv
import re


def display_menu():
    print("\n-----MENU-----")
    print("1. View Grid")
    print("2. Register Driver")
    print("3. Start Qualifying")
    print("4. Start Race")
    print("5. Exit")
    opt = int(input("\nSelect option: "))
    return opt


def view_grid():
    
        print("driver")




def main():
    while True:    
        opt = display_menu()
        if opt == 1:
            print("View Grid")
            view_grid()
        if opt == 2:
            print("Register Driver")
        if opt == 3:
            print("Start Qualifying")
        if opt == 4:
            print("Start Race")                 
        elif opt == 5:
             print("Exit")
             return
main()