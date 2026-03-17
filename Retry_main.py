import csv   #imports data from csv file
import re
import random    #has function to randomly generate number

from Driver import Driver    #imports data from file Driver.py
from Track import Track      #imports data from file Track.py

#allows user to choose from a variety of options within the menu
def display_menu():
    print("\n--------F1 MENU--------")
    print("1. View Grid")    #shows all drivers on the grid
    print("2. Reset Grid")   #resets grid to a default lineup of drivers
    print("3. Create your team")   #allows user to add their own driver to the grid
    print("4. Choose track")    #allows user to choose the track they want
    print("5. Start Qualifying")  #orders drivers
    print("6. Start Race") #completes a 5 lap race and shows drivers postions at the end
    print("7. Exit")  #allows user to exit menu
    
    acceptnumber = [1,2,3,4,5,6,7]

    while True:
        try:    #tries to execute
            opt = int(input("Select option: "))   #asks user for an input giving them a choice from the menu
            if opt in acceptnumber:
                return opt
            else:
                print("Invalid input") 
        except ValueError:
            print("Invalid input")    #if the input isn't valid, the program prompts the user to try again
    return opt


def view_grid():
    #open csv file
    with open("drivers.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        name = "Name"
        team = "Team"
        no = "Number"

        print(f"\n{name:<12} {no:<9} {team:<9} ")
        print("-------------------------------------")
        

        #reads each line of code in the csv file
        for line in csv_reader:
            new_name, new_number, new_team = line   
            driver = Driver(new_name, new_number, new_team)
            driver.display()   #uses the function inside the other code and displays the information
                

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
                writer.writerow(["Albon", "23", "Williams"])
                writer.writerow(["Sainz", "55", "Williams"])
                writer.writerow(["Lawson", "30", "Racing Bulls"])
                writer.writerow(["Lindblad", "41", "Racing Bulls"])
            print("GRID IS RESET")
            break
        elif decide == "No":
            print("Returning to menu...")  #sends user back to main menu
            break
        else:
            print("Invalid input") #prompts user to try again


def create_team():

    with open("drivers.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        drivers = list(csv_reader)
  
    if len(drivers) == 10:  #checks length of drivers and executes code
        print("Previous save file uploaded...")

        drivelist = []
        teamlist = []

        for line in drivers:
            new_name, new_number, new_team = line
            drivelist.append(new_name) 
            teamlist.append(new_team)  

        print(f"\nTeam: {teamlist[8]}")
        print(f"Driver 1: {drivelist[8]}")
        print(f"Driver 2: {drivelist[9]}\n")

        rep_choice = ["Yes", "No"] 

        while True:
            try:
                choice = input("Do you want to replace this save file. Select yes or no: ")
                choice = choice.title()
                if choice not in rep_choice:
                    choice = int(input(f"Invalid input\nDo you want to replace this save file. Select yes or no: "))
                    choice = choice.title()
                else:
                    break
            
            except ValueError:
                print("Invalid input")

        if choice == "Yes":
            with open ("drivers.csv", "w", newline='') as file:
                writer = csv.writer(file)
                #adds drivers to default grid
                writer.writerow(["Verstappen", "3", "Red Bull"])
                writer.writerow(["Hadjar", "6", "Red Bull"])
                writer.writerow(["Hamilton", "44", "Ferrari"])
                writer.writerow(["Leclerc", "16", "Ferrari"])
                writer.writerow(["Albon", "23", "Williams"])
                writer.writerow(["Sainz", "55", "Williams"])
                writer.writerow(["Lawson", "30", "Racing Bulls"])
                writer.writerow(["Lindblad", "41", "Racing Bulls"])

            print("Save file deleted!")
        elif choice == "No":
            print("Returning to menu...")
            return
        else:
            print("Invalid Input")

    team_list = [1,2,3]

    while True:
        try:
            new_team = int(input("Choose team - | 1.Mercedes | 2.Audi | 3.Mclaren |: "))
            while new_team not in team_list:
                new_team = int(input(f"Invalid Team\nChoose team - | 1.Mercedes | 2.Audi | 3.Mclaren |: "))
            break
            
        except ValueError:
            print("Invalid Team")

    if new_team == 1:
        new_team = "Mercedes"
        print("Team selected - Mercedes")
    elif new_team == 2:
        new_team = "Audi"
        print("Team selected - Audi")
    elif new_team == 3:
        new_team = "Mclaren" 
        print("Team selected - Mclaren")

    print(f"\nChoose 2 drivers\n")

    team_full = 1

    while team_full < 3:
        add_driver(new_team, team_full)
        team_full = team_full + 1

    print("Team Created!")

    with open("drivers.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        drivers = list(csv_reader)

        drivelist = []
        teamlist = []

        for line in drivers:
            new_name, new_number, new_team = line
            drivelist.append(new_name) 
            teamlist.append(new_team)  

        print(f"\nTeam: {teamlist[8]}")
        print(f"Driver 1: {drivelist[8]}")
        print(f"Driver 2: {drivelist[9]}\n")


def add_driver(new_team, team_full):
    while True:
        new_name = input(f"Driver {team_full} last name: ").strip() 
        if re.search(r"^[a-zA-Z ]+$", new_name):   #checks that the input is valid inside the parameters of being in the alphabet
            new_name = new_name.title()
            break
        else: 
            print("Invalid name")

    unavailable_numbers = []

    with open("drivers.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            unavailable_numbers.append(int(line[1]))

    while True:
        try:
            new_number = int(input(f"Driver {team_full} number (2-99): "))
            while new_number < 2 or new_number > 99 or new_number in unavailable_numbers:    #checks that the numnber is within the range of 2 and 99
                new_number = int(input(f"Number Unavailable\nDriver {team_full} number (2-99): "))
        except ValueError:
            print("Invalid input")
        else:
            break    

    driver = Driver(new_name, new_number, new_team)

    #opens csv file and writes in the new driver
    with open ("drivers.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([driver.new_name, driver.new_number, driver.new_team])
    print("Driver added\n")




def race_track():
    
    print("")   #adds space between print codes
    
    while True:           
            race_name = input("Select a track - Monza | Spa | Silverstone: ")
            race_name = race_name.title()
            if re.match(r"^(Monza|Spa|Silverstone)$", race_name):              
                break        
            else:
                print("Invalid input")

    wet, dry = read_track(race_name)
        
    return race_name, wet, dry

    
def read_track(race_name):
        
        track = []

        with open("tracks.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                track_name, best_time, dry, wet = line

                dry = float(dry)
                wet = float(wet)
            
                if race_name == track_name:
                    track = Track(track_name, best_time, dry, wet)
                    print(f"")
                    track.track_display()        
                    return float(wet), float(dry)
          
    

def qualifying(race_name, wet, dry):

    import time

    with open("drivers.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        drivers = list(csv_reader)
        
    
    if len(drivers) == 8:
        print("\nNot enough drivers on the grid (8/10). Create a new team in the menu!")
    else:
        print("\nTeam save file uploaded...")

        if race_name == "Unselected":
            while race_name == "Unselected":
                print("\nTrack not selected")
                race_name, wet, dry = race_track()
        else:
            read_track(race_name)

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
            lap_time = wet   #wet lap conditions
            print("Weather: Rain")
            print("Warning **Wet Track**\n")
            time.sleep(0.7)
            weather = "wet"
        else:
            lap_time = dry    #dry lap conditions
            print("Weather: Sunny\n")
            time.sleep(0.7)
            weather = "dry"

        if weather == "dry":
            add_time = 0.999
        
        elif weather == "wet":
            add_time = 1.999

        print("----------QUALIFYING RESULTS----------\n")
        

        Pos = "Position"
        Name = "Name"
        print(f"{Pos:<9} {Name:<12} Time ")

        for line in driver:
            new_name, new_number, new_team = line
            lap_add = random.uniform(0, add_time)
            lap_time = round(lap_time + lap_add, 3)
        
            print(f"{position:<9} {new_name:<12} 1:{lap_time:.3f}")
            position = position + 1
        


def race(race_name):
    
    import time     #import a library to delay the time it takes to print out an output

    with open("drivers.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        drivers = list(csv_reader)
        
    
    if len(drivers) == 8:
        print("\nNot enough drivers on the grid (8/10)\nCreate a new team in the menu!")
    else:
        print("\nTeam save file uploaded...")

        if race_name == "Unselected":
            while race_name == "Unselected":
                print("\nTrack not selected")
                race_name = race_track()
        else:
            read_track(race_name)

        track_weather = random.randint(5, 10)

        if track_weather == 7:
        
            print("Weather: Rain")
            print("Warning **Wet Track**\n")
            time.sleep(0.7)
            weather = "wet"
        else:
       
            print("Weather: Sunny\n")
            time.sleep(0.7)
            weather = "dry"

        if weather == "dry":
            add_time = 4.999
        elif weather == "wet":
            add_time = 8.999

        pit = [1,2]

        tyre1 = ["1. Medium → Hard", "2. Hard → Medium", "3. Medium → Medium"]
        tyre2 = ["1. Soft → Medium → Soft", "2. Medium → Soft → Medium", "3. Medium → Hard → Soft"]

        while True:
            try:
                pit_stop = int(input("Choose pit stop strategy (1 stop | 2 stop). Enter 1 or 2: "))
                while pit_stop not in pit:
                    pit_stop = int(input(f"Invalid option\nChoose pit stop strategy (1 stop | 2 stop). Enter 1 or 2: "))
                break
            
            except ValueError:
                print("Invalid option")

        tyre_num = [1,2,3]
        
        if pit_stop == 1:
            print("\n1 pit stop\n")
            print("Available tyre strategies:\n")
            for i in tyre1:
                print(i)
            print("")
            while True:
                try:
                    tyre_choice = int(input("Select tyre strategy. Enter 1 or 2 or 3: "))
                
                    while tyre_choice not in tyre_num:
                        tyre_choice = int(input(f"Invalid option\nSelect tyre strategy. Enter 1 or 2 or 3: "))
                    break
            
                except ValueError:
                    print("Invalid option")

            if tyre_choice == 1:
                print("\nSTRATEGY: 1 Stop (Medium → Hard)")
            elif tyre_choice == 2:
                print("\nSTRATEGY: 1 Stop (Hard → Medium)")
            elif tyre_choice == 3:
                print("\nSTRATEGY: 1 Stop (Medium → Medium)")
        

        elif pit_stop == 2:
            print("\n2 pit stop\n")
            print("Available tyre strategies:\n")
            for i in tyre2:
                print(i)
            print("")
            while True:
                try:
                    tyre_choice = int(input("Select tyre strategy. Enter 1 or 2 or 3: "))
                    while tyre_choice not in tyre_num:
                        tyre_choice = int(input(f"Invalid option\nSelect tyre strategy. Enter 1 or 2 or 3: "))
                    break
            
                except ValueError:
                    print("Invalid option")
            if tyre_choice == 1:
                print("\nSTRATEGY: 2 Stop (Soft → Medium → Soft)")
            elif tyre_choice == 2:
                print("\nSTRATEGY: 2 Stop (Medium → Soft → Medium)")
            elif tyre_choice == 3:
                print("\nSTRATEGY: 2 Stop (Medium → Hard → Soft)")




        print("")

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
        print("\n---------RACE RESULTS---------")
        print(f"\n{Pos:<9} {Name:<11} {Time} ")
        

        for line in driver:
            new_name, new_number, new_team = line
            lap_add = random.uniform(0, add_time)
            lap_time = round(lap_add, 3)
        
            if position == 1:
                print(f"{position:<9} {new_name:<11}    -")
                position = position + 1       
            else:
                print(f"{position:<9} {new_name:<11} +{lap_time:.3f}")
                position = position + 1


#uses user input in the main menu to select which function to use
race_name = "Unselected"
wet = 0
dry = 0
def main(race_name,wet,dry):
    while True:    
        opt = display_menu()
        if opt == 1:
            print("\n--------------VIEW GRID--------------")
            view_grid()
        elif opt == 2:           
            print("\nRESET GRID")
            reset_grid()
        elif opt == 3:           
            print("\n---------------------CREATE TEAM---------------------\n")   
            create_team()
        elif opt == 4:
            print("\n-----------------CHOOSE TRACK-----------------")  
            race_name, wet, dry = race_track()  
        elif opt == 5:
            print("\n----------------START QUALIFYING----------------")
            qualifying(race_name, wet, dry)
        elif opt == 6:
            print("\n--------------START RACE--------------")  
            race(race_name)                
        elif opt == 7:
             print("Exit")
             return


main(race_name,wet,dry)