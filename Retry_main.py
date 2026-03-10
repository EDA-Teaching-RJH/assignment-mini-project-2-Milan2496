import csv
import re
import random

#imports data from file Driver.py
from Driver import Driver

#allows user to choose from a variety of options within the menu
def display_menu():
    print("\n--------F1 MENU--------")
    print("1. View Grid")    #shows all drivers on the grid
    print("2. Reset Grid")   #resets grid to a default lineup of drivers
    print("3. Register Driver")   #allows user to add their own driver to the grid
    print("4. Start Qualifying")  #orders drivers
    print("5. Start Race") #completes a 5 lap race and shows drivers postions at the end
    print("6. Exit")  #allows user to exit menu
    
    while True:
        try:
            opt = int(input("Select option: "))
            break
        except ValueError:
            print("Invalid input")
    return opt


def view_grid():
    #open csv file
    with open("drivers.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        #reads each line of code in the csv file
        for line in csv_reader:
            new_name, new_number, new_team = line
            driver = Driver(new_name, new_number, new_team)
            driver.display()
            
            


def reset_grid():
    while True:
        #checks if the user is sure they want to reset grid
        decide = input("Are you sure you want to reset the grid? Select Yes or No: ")
        decide = decide.title() #capitalises first letter and leaves rest in lower case
        if decide == "Yes":
            #opens csv file to write in it
            with open ("drivers.csv", "w", newline='') as file:
                writer = csv.writer(file)
                #adds drivers to default grid
                writer.writerow(["Verstappen", "3", "Red Bull"])
                writer.writerow(["Hadjar", "6", "Red Bull"])
                writer.writerow(["Hamilton", "44", "Ferrari"])
                writer.writerow(["Leclerc", "16", "Ferrari"])
            print("GRID IS RESET")
            break
        elif decide == "No":
            print("Routing back to menu . . .")  #sends user back to main menu
            break
        else:
            print("Invalid input") #prompts user to try again


def register_driver():

    while True:
        new_name = input("Driver name: ").strip() 
        if re.search(r"^[a-zA-Z ]+$", new_name):   #checks that the input is valid inside the parameters of being in the alphabet
            new_name = new_name.title()
            break
        else: 
            print("Invalid name")

    while True:
        try:
            new_number = int(input("Driver number (2-99): "))
            while new_number < 2 or new_number > 99:    #checks that the numnber is within the range of 2 and 99
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
    #opens csv file and writes in the new driver
    with open ("drivers.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([driver.new_name, driver.new_number, driver.new_team])
    print("Driver added")


def qualifying():

    driver = []   #creates a list where the shuffled drivers will be stored

    with open("drivers.csv", "r") as csv_file:   #opens csv file
        csv_reader = csv.reader(csv_file)


        for line in csv_reader:
            new_name, new_number, new_team = line
            driver.append(line)  #writes the data into the list
   
    random.shuffle(driver)    #shuffles the drivers
    
    position = 1
    

    for line in driver:
        new_name, new_number, new_team = line
        lap_add = random.randint(0, 999)
        if lap_add < 10:
            lap_time = (f"1.00{lap_add}")
        elif lap_add < 100:    
            lap_time = (f"1.0{lap_add}")
        else:
            lap_time = (f"1.{lap_add}")

        print(f"{position} - {new_name} - {lap_time}")
        position = position + 1
        
        

def race():
    print()


#uses user input in the main menu to select which function to use
def main():
    while True:    
        opt = display_menu()
        if opt == 1:
            print("\n---------------VIEW GRID---------------")
            view_grid()
        if opt == 2:           
            print("\nRESET GRID")
            reset_grid()
        if opt == 3:           
            print("\n-----REGISTER DRIVER-----")
            register_driver()
        if opt == 4:
            print("\n---QUALIFYING RESULTS---")
            qualifying()
        if opt == 5:
            print("-----START RACE-----")  
            race()               
        elif opt == 6:
             print("Exit")
             return
main()