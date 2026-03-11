import csv   #imports data from csv file
import re
import random    #has function to randomly generate number


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
    print("6. Choose track")
    print("7. Exit")  #allows user to exit menu
    
    while True:
        try:    #tries to execute
            opt = int(input("Select option: "))   #asks user for an input giving them a choice from the menu
            break
        except ValueError:
            print("Invalid input")    #if the input isn't valid, the program prompts the user to try again
    return opt


def view_grid():
    #open csv file
    with open("drivers.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        #reads each line of code in the csv file
        for line in csv_reader:
            new_name, new_number, new_team = line   
            driver = Driver(new_name, new_number, new_team)
            driver.display()   #usees the function inside the other code and displays the information
            
            


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

def race_track(race_name):
    

    track_list = ["Monza","Spa","Silverstone"]
    
    while True:
        try:
            race_name = (input("Select a track - Monza | Spa | Silverstone: "))
            race_name = race_name.title()
            while race_name not in track_list:
                race_name = int(input(f"Invalid input \nSelect a track - Monza | Spa | Silverstone: "))
                return race_name
            break
            
        except ValueError:
            print("Invalid input")


def qualifying(race_name):
    print(race_name)
    import time

    driver = []   #creates a list where the shuffled drivers will be stored

    with open("drivers.csv", "r") as csv_file:   #opens csv file
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            new_name, new_number, new_team = line
            driver.append(line)  #writes the data into the list
   
    random.shuffle(driver)    #shuffles the drivers
    
    position = 1   

    track_weather = random.randint(5, 10)
    
    if track_weather == 7:
        lap_time = 20.294    #wet lap conditions
        print("\nWeather: Rain")
        print("Warning **Wet Track**\n")
        time.sleep(0.7)
        weather = "wet"
    else:
        lap_time = 18.792    #dry lap conditions
        print("\nWeather: Sunny\n")
        time.sleep(0.7)
        weather = "dry"

    if weather == "dry":
        add_time = 0.999
    elif weather == "wet":
        add_time = 1.999

    Pos = "Position"
    Name = "Name"
    Time = "Time"
    print(f"{Pos:<9} {Name:<12} Time ")

    for line in driver:
        new_name, new_number, new_team = line
        lap_add = random.uniform(0, add_time)
        lap_time = round(lap_time + lap_add, 3)
        
        if re.search(r"^[0-9]{2}.[0-9]{2}+$", str(lap_time)):
            print(f"{position:<9} {new_name:<12} 1:{lap_time:.3f}0")
            position = position + 1
        elif re.search(r"^[0-9]{8}.[0-9]{1}+$", str(lap_time)):
            print(f"{position:<9} {new_name:<12} 1:{lap_time:.3f}00")
            position = position + 1
        else:
            print(f"{position:<9} {new_name:<12} 1:{lap_time:.3f}")
            position = position + 1


def race():
    
    import time     #import a library to delay the time it takes to print out an output

    race_track = input("Select a track to ")


    track_weather = random.randint(5, 10)

    if track_weather == 7:
        lap_time = 20.294    #wet lap conditions
        print("\nWeather: Rain")
        print("Warning **Wet Track**\n")
        time.sleep(0.7)
        weather = "wet"
    else:
        lap_time = 18.792    #dry lap conditions
        print("\nWeather: Sunny\n")
        time.sleep(0.7)
        weather = "dry"

    if weather == "dry":
        add_time = 2.999
    elif weather == "wet":
        add_time = 4.999

    lights = ["🔴", "🔴", "🔴", "START!!!"]
    for line in lights:
        print(line)
        time.sleep(0.7)
    
    driver = []   #creates a list where the shuffled drivers will be stored

    with open("drivers.csv", "r") as csv_file:   #opens csv file
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            new_name, new_number, new_team = line
            driver.append(line)  #writes the data into the list
   
    random.shuffle(driver)    #shuffles the drivers
    
    position = 1   

    Pos = "Position"
    Name = "Name"
    Time = "Interval"
    print(f"\n{Pos:<9} {Name:<11} {Time} ")

    for line in driver:
        new_name, new_number, new_team = line
        lap_add = random.uniform(0, add_time)
        lap_time = round(lap_add, 3)
        
        if position == 1:
            if re.search(r"^[0-9]{2}.[0-9]{2}+$", str(lap_time)):
                print(f"{position:<9} {new_name:<11}    -")
                position = position + 1
            elif re.search(r"^[0-9]{2}.[0-9]{1}+$", str(lap_time)):
                print(f"{position:<9} {new_name:11}    -")
                position = position + 1
            else:
                print(f"{position:<9} {new_name:<11}    -")
                position = position + 1       
        else:
            if re.search(r"^[0-9]{2}.[0-9]{2}+$", str(lap_time)):
                print(f"{position:<9} {new_name:<11} +{lap_time}0")
                position = position + 1
            elif re.search(r"^[0-9]{2}.[0-9]{1}+$", str(lap_time)):
                print(f"{position:<9} {new_name:11} +{lap_time}00")
                position = position + 1
            else:
                print(f"{position:<9} {new_name:<11} +{lap_time}")
                position = position + 1





#uses user input in the main menu to select which function to use
race_name = "Unselected"
def main(race_name):
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
            qualifying(race_name)
        if opt == 5:
            print("-----START RACE-----")  
            race()  
        if opt == 6:
            print("-----CHOOSE TRACK-----")  
            race_name = race_track(race_name)              
        elif opt == 7:
             print("Exit")
             return
main(race_name)