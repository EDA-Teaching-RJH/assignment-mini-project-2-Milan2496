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
    with open("drivers.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            print(line)

def register_driver():

    while True:
        new_name = input("Driver name: ").strip() 
        if re.search(r"^[a-zA-Z ]+$", new_name):
            new_name = new_name.title()
            break
        else: 
            print("Invalid name. Try again: ")

    while True:
        try:
            new_number = int(input("Driver number (2-99): "))
            while new_number < 2 or new_number > 99:
                new_number = int(input("Invalid number. Try again: "))
        except ValueError:
            print("Invalid input. Try again: ")
        else:
            break
    

    team_list = [1,2,3]
    
    while True:
        try:
            new_team = int(input("Choose team (1.Audi, 2.Mercedes, 3.Cadillac): "))
            while new_team not in team_list:
                new_team = int(input("Invalid number. Try again: "))
            break
            
        except ValueError:
            print("Invalid input. Try again: ")
        

    



    


def main():
    while True:    
        opt = display_menu()
        if opt == 1:
            print("View Grid")
            view_grid()
        if opt == 2:
            print("Register Driver")
            register_driver()
        if opt == 3:
            print("Start Qualifying")
        if opt == 4:
            print("Start Race")                 
        elif opt == 5:
             print("Exit")
             return
main()