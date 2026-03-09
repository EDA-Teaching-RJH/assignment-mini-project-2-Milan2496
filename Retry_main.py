import csv
import re

from Driver import Driver

def display_menu():
    print("\n--------MENU--------")
    print("1. View Grid")
    print("2. Reset Grid")
    print("3. Register Driver")
    print("4. Start Qualifying")
    print("5. Start Race")
    print("6. Exit")
    opt = int(input("\nSelect option: "))
    return opt


def view_grid():
    with open("drivers.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            new_name, new_number, new_team = line
            driver = Driver(new_name, new_number, new_team)
            driver.display()
            
            


def reset_grid():
    while True:
        decide = input("Are you sure you want to reset the grid? Select Yes or No: ")
        decide = decide.title()
        if decide == "Yes":
            with open ("drivers.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Verstappen", "3", "Red Bull"])
                writer.writerow(["Hadjar", "6", "Red Bull"])
                writer.writerow(["Hamilton", "44", "Ferrari"])
                writer.writerow(["Leclerc", "16", "Ferrari"])
            print("GRID IS RESET")
            break
        elif decide == "No":
            print("Routing back to menu . . .")
            break
        else:
            print("Invalid input")


def register_driver():

    while True:
        new_name = input("Driver name: ").strip() 
        if re.search(r"^[a-zA-Z ]+$", new_name):
            new_name = new_name.title()
            break
        else: 
            print("Invalid name")

    while True:
        try:
            new_number = int(input("Driver number (2-99): "))
            while new_number < 2 or new_number > 99:
                new_number = int(input("Number Unavailable. Choose driver number (2-99): "))
        except ValueError:
            print("Invalid input")
        else:
            break
    

    team_list = [1,2,3]
    
    while True:
        try:
            new_team = int(input("Choose team - | 1.Mercedes | 2.Audi | 3.Mclaren |: "))
            while new_team not in team_list:
                new_team = int(input("Invalid Team. Choose team - | 1.Mercedes | 2.Audi | 3.Mclaren |: "))
            break
            
        except ValueError:
            print("Invalid input")

    if new_team == 1:
        new_team = "Mercedes"
    elif new_team == 2:
        new_team = "Audi"
    elif new_team == 3:
        new_team = "Mclaren"      

    driver = Driver(new_name, new_number, new_team)

    with open ("drivers.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([driver.new_name, driver.new_number, driver.new_team])
    print("Driver added")


def main():
    while True:    
        opt = display_menu()
        if opt == 1:
            print("---------------VIEW GRID---------------")
            view_grid()
        if opt == 2:           
            print("RESET GRID")
            reset_grid()
        if opt == 3:           
            print("-----REGISTER DRIVER-----")
            register_driver()
        if opt == 4:
            print("Start Qualifying")
        if opt == 5:
            print("Start Race")                 
        elif opt == 6:
             print("Exit")
             return
main()