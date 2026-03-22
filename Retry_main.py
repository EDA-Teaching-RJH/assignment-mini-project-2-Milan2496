import csv       #imports data from csv file
import re        #imports regex
import random    #has function to randomly generate number

from Driver import Driver    #imports data from file Driver.py
from Track import Track      #imports data from file Track.py

#allows user to choose from a variety of options within the menu
def display_menu():
    print("\n--------F1 MENU--------")
    print("1. View Grid")          #shows all drivers on the grid
    print("2. Reset Grid")         #resets grid to a default lineup of drivers
    print("3. Create your team")   #allows user to add their own driver to the grid
    print("4. Choose track")       #allows user to choose the track they want
    print("5. Start Qualifying")   #orders drivers
    print("6. Start Race")         #completes a 5 lap race and shows drivers postions at the end
    print("7. Exit")               #allows user to exit menu
    
    acceptnumber = [1,2,3,4,5,6,7]    #list of numbers accepted for opt

    while True:                                      #runs code while true
        try:                                         #tries to execute
            opt = int(input("Select option: "))      #asks user for an input giving them a choice from the menu
            if opt in acceptnumber:                  #checks if opt is in the list
                return opt                           #if it is then it returns it and breaks the loop
            else:
                print("Invalid input")               #if the input isn't valid, the program prompts the user to try again
        except ValueError:
            print("Invalid input")                   #if the input isn't valid, the program prompts the user to try again

def view_grid():
    with open("drivers.csv", "r") as csv_file:       #open csv file and reads it
        csv_reader = csv.reader(csv_file)

        name = "Name"   #assigns a word to the variable so that it can be outputted in a table in the print code below
        team = "Team"
        no = "Number"

        print(f"\n{name:<12} {no:<9} {team:<9} ")            #prints variables with a certain distance between them using :<
        print("-------------------------------------")       #prints a line between header and data
        
        for line in csv_reader:                              #reads each line of code in the csv file
            new_name, new_number, new_team = line   
            driver = Driver(new_name, new_number, new_team)
            driver.display()                                 #uses the function inside the other code and displays the information
                

def reset_grid():
    while True:
        decide = input("Are you sure you want to reset the grid? Select Yes or No: ")  #checks if the user is sure they want to reset grid
        decide = decide.title()                                                        #capitalises first letter and leaves rest in lower case
        if decide == "Yes":
            with open ("drivers.csv", "w", newline='') as file:       #opens csv file to write in it
                writer = csv.writer(file)                             #adds drivers to default grid
                writer.writerow(["Verstappen", "3", "Red Bull"])
                writer.writerow(["Hadjar", "6", "Red Bull"])
                writer.writerow(["Hamilton", "44", "Ferrari"])
                writer.writerow(["Leclerc", "16", "Ferrari"])
                writer.writerow(["Albon", "23", "Williams"])
                writer.writerow(["Sainz", "55", "Williams"])
                writer.writerow(["Lawson", "30", "Racing Bulls"])
                writer.writerow(["Lindblad", "41", "Racing Bulls"])
            print("GRID IS RESET")                                    #informs user that grid is reset
            break
        elif decide == "No":
            print("Returning to menu...")      #sends user back to main menu
            break
        else:
            print("Invalid input")             #prompts user to try again


def create_team():

    with open("drivers.csv", "r") as csv_file:     #open csv file and reads it
        csv_reader = csv.reader(csv_file)
        drivers = list(csv_reader)                 #creates a list of all the drivers
  
    if len(drivers) == 10:                         #checks length of drivers and executes code
        print("Previous save file uploaded...")

        drivelist = []
        teamlist = []

        for line in drivers:
            new_name, new_number, new_team = line
            drivelist.append(new_name)              #writes all the drivers into a list
            teamlist.append(new_team)               #writes all the teams into a list

        print(f"\nTeam: {teamlist[8]}")             #writes the team of the previous save file
        print(f"Driver 1: {drivelist[8]}")          #writes the first driver of the previous save file
        print(f"Driver 2: {drivelist[9]}\n")        #writes the second driver of the previous save file

        rep_choice = ["Yes", "No"]                  #list of accepted inputs

        while True:
            try:
                choice = input("Do you want to replace this save file. Select yes or no: ")
                choice = str(choice)            #convert variable to a string
                choice = choice.title()         #Converts first letter to uppercase and rest to lowercase
                if choice not in rep_choice:    #checks if choice is in list
                    print("Invalid input")      #if not in list prints invalid        
                else:
                    break                       #breaks code
            
            except ValueError:
                print("Invalid input")          #if input is not accepted then prints invalid

        if choice == "Yes":
            with open ("drivers.csv", "w", newline='') as file:     #opens and writes to csv file
                writer = csv.writer(file)                           #adds drivers to default grid
                writer.writerow(["Verstappen", "3", "Red Bull"])    #writes driver, number and team to file
                writer.writerow(["Hadjar", "6", "Red Bull"])
                writer.writerow(["Hamilton", "44", "Ferrari"])
                writer.writerow(["Leclerc", "16", "Ferrari"])
                writer.writerow(["Albon", "23", "Williams"])
                writer.writerow(["Sainz", "55", "Williams"])
                writer.writerow(["Lawson", "30", "Racing Bulls"])
                writer.writerow(["Lindblad", "41", "Racing Bulls"])
            print("Save file deleted!")                             #tells user that previous save is deleted
        elif choice == "No":
            print("Returning to menu...")                           #if user doesn't want to delete the file then it returns them to the menu
            return
        else:
            print("Invalid Input")

    team_list = [1,2,3]       #list of accepted values for new_team

    while True:         
        try:
            new_team = int(input("Choose team - | 1.Mercedes | 2.Audi | 3.Mclaren |: "))
            while new_team not in team_list:
                new_team = int(input(f"Invalid Team\nChoose team - | 1.Mercedes | 2.Audi | 3.Mclaren |: "))    #if new_team not in list then code asks user to try again
            break
            
        except ValueError:
            print("Invalid Team")

    if new_team == 1:                         #appends the users input to a team
        new_team = "Mercedes" 
        print("Team selected - Mercedes")     # 1 = Mercedes
    elif new_team == 2:
        new_team = "Audi"
        print("Team selected - Audi")         # 2 = Audi
    elif new_team == 3:
        new_team = "Mclaren" 
        print("Team selected - Mclaren")      # 3 = Mclaren

    print(f"\nChoose 2 drivers\n")

    team_full = 1

    while team_full < 3:                      #runs while team_full is smaller than 3
        add_driver(new_team, team_full)       #runs code under function add_driver
        team_full = team_full + 1             #adds 1 to team_full every time the loop runs so that it only runs twice

    print("Team Created!")

    with open("drivers.csv", "r") as csv_file:   #opens and reads csv file
        csv_reader = csv.reader(csv_file)
        drivers = list(csv_reader)

        drivelist = []             #creates list for drivers
        teamlist = []              #creates list for teams

        for line in drivers:
            new_name, new_number, new_team = line
            drivelist.append(new_name)               #writes all the drivers into a list
            teamlist.append(new_team)                #writes all the teams into a list

        print(f"\nTeam: {teamlist[8]}")              #writes the team of the previous save file
        print(f"Driver 1: {drivelist[8]}")           #writes the first driver of the previous save file
        print(f"Driver 2: {drivelist[9]}\n")         #writes the second driver of the previous save file


def add_driver(new_team, team_full):   #sends variables back to create_team
    while True:
        new_name = input(f"Driver {team_full} last name: ").strip()    #.strip removes  blank spaces
        if re.search(r"^[a-zA-Z ]+$", new_name):                       #checks that the input is valid inside the parameters of being in the alphabet
            new_name = new_name.title()                                
            break
        else: 
            print("Invalid name")    

    unavailable_numbers = []         #creates a list for the next code

    with open("drivers.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            unavailable_numbers.append(int(line[1]))     #this reads the second column of data which are the driver numbers and appends them to the list

    while True:
        try:
            new_number = int(input(f"Driver {team_full} number (2-99): "))
            while new_number < 2 or new_number > 99 or new_number in unavailable_numbers:    #checks that the numnber is within the range of 2 and 99 and checks that the number isn't already used by another driver by checking the list
                new_number = int(input(f"Number Unavailable\nDriver {team_full} number (2-99): "))
        except ValueError:
            print("Invalid input")
        else:
            break    

    driver = Driver(new_name, new_number, new_team)

    
    with open ("drivers.csv", "a", newline='') as file:   #opens csv file as append
        writer = csv.writer(file)
        writer.writerow([driver.new_name, driver.new_number, driver.new_team])   #writes in the data for the new driver
    print("Driver added\n")




def race_track():
    
    print("")   #adds space between print codes
    
    while True:           
            race_name = input("Select a track - Monza | Spa | Silverstone: ")
            race_name = race_name.title()                                         #capitalises first letter
            if re.match(r"^(Monza|Spa|Silverstone)$", race_name):                 #checks to see if input matches accepted data
                break        
            else:
                print("Invalid input")

    wet, dry = read_track(race_name)         
        
    return race_name, wet, dry               #returns variables

    
def read_track(race_name):
        
        track = []       #creates a track list

        with open("tracks.csv", "r") as csv_file:     #opens and reads file
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                track_name, best_time, dry, wet = line

                dry = float(dry)    #converts to float
                wet = float(wet)    #converts to float
             
                if race_name == track_name:                        #checks if race_name is equal to track_name
                    track = Track(track_name, best_time, dry, wet)
                    print(f"")
                    track.track_display()                          #uses function from other file
                    return float(wet), float(dry)                  #returns variables as floats
          
    

def qualifying(race_name, wet, dry):     #create function passing these variables

    import time     #imports a library called time

    with open("drivers.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        drivers = list(csv_reader)      #writes all the drivers into a variabel
        
    
    if len(drivers) == 8:         #checks if the length of the variable is equal to 8
        print("\nNot enough drivers on the grid (8/10). Create a new team in the menu!")
    else:
        print("\nTeam save file uploaded...")

        if race_name == "Unselected":
            while race_name == "Unselected":
                print("\nTrack not selected")
                race_name, wet, dry = race_track()     #runs the fucntion and passes the variables through them
        else:
            read_track(race_name)

        driver = []   #creates a list where the shuffled drivers will be stored

        with open("drivers.csv", "r") as csv_file:   #opens csv file
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                new_name, new_number, new_team = line
                driver.append(line)  #writes the data into the list
   
        random.shuffle(driver)    #shuffles the drivers
    
        position = 1   #sets the position to 1

        track_weather = random.randint(5, 10)     #generates a random numnber between 5 and 10
    
        if track_weather == 7:       #if the random number is 7, the code runs, so there is a 1 in 5 chance of the code running
            lap_time = wet   #wet lap conditions
            print("Weather: Rain")
            print("Warning **Wet Track**\n")
            time.sleep(0.7)    #uses the time library to delay the time it takes to print out a code by 0.7 seconds
            weather = "wet"
        else:
            lap_time = dry    #dry lap conditions
            print("Weather: Sunny\n")
            time.sleep(0.7)   #uses the time library to delay the time it takes to print out a code by 0.7 seconds
            weather = "dry"

        if weather == "dry":
            add_time = 0.999   #when weather is dry then the lap time becomes shorter
        
        elif weather == "wet":
            add_time = 1.999       # when weather is wet then lap times become longer

        print("----------QUALIFYING RESULTS----------\n")
        

        Pos = "Position"
        Name = "Name"
        print(f"{Pos:<9} {Name:<12} Time ")     #use :< to create a grid

        for line in driver:
            new_name, new_number, new_team = line
            lap_add = random.uniform(0, add_time)   #generates a number between 0 and the chosen lap time
            lap_time = round(lap_time + lap_add, 3)    #rounds the time to 3 decimal places
        
            print(f"{position:<9} {new_name:<12} 1:{lap_time:.3f}")
            position = position + 1         #adds 1 to each position so that it increases by one in every row of the list
        


def race(race_name):
    
    import time     #import a library to delay the time it takes to print out an output

    with open("drivers.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        drivers = list(csv_reader)
        
    
    if len(drivers) == 8:   #checks length of drivers
        print("\nNot enough drivers on the grid (8/10)\nCreate a new team in the menu!")
    else:
        print("\nTeam save file uploaded...")

        if race_name == "Unselected":
            while race_name == "Unselected":
                print("\nTrack not selected")
                race_name = race_track()      #runs function of race track and passed the name of the track through
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

        pit = [1,2]    #2 variables in the list

        tyre1 = ["1. Medium → Hard", "2. Hard → Medium", "3. Medium → Medium"]     #list to show a choice of what tyres can be selected for the race
        tyre2 = ["1. Soft → Medium → Soft", "2. Medium → Soft → Medium", "3. Medium → Hard → Soft"]       #list to show a choice of what tyres can be selected for the race

        while True: #runs until code breaks it when a valid input is passed
            try:
                pit_stop = int(input("Choose pit stop strategy (1 stop | 2 stop). Enter 1 or 2: "))
                while pit_stop not in pit:
                    pit_stop = int(input(f"Invalid option\nChoose pit stop strategy (1 stop | 2 stop). Enter 1 or 2: "))
                break
            
            except ValueError:
                print("Invalid option")  #lets the user try again with any input that does not match the required format

        tyre_num = [1,2,3]
        
        if pit_stop == 1:
            print("\n1 pit stop\n")
            print("Available tyre strategies:\n")
            for i in tyre1:
                print(i)   #prints the row of the list
            print("")   
            while True:
                try:
                    tyre_choice = int(input("Select tyre strategy. Enter 1 or 2 or 3: "))
                
                    while tyre_choice not in tyre_num:
                        tyre_choice = int(input(f"Invalid option\nSelect tyre strategy. Enter 1 or 2 or 3: "))
                    break
            
                except ValueError:
                    print("Invalid option")

            if tyre_choice == 1:    #assigns the number choice to the correct choice in the list
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
            time.sleep(0.7)   #prints every line of the list with a gap of 0.7seconds
    
        driver = []   #creates a list where the shuffled drivers will be stored

        with open("drivers.csv", "r") as csv_file:   #opens csv file
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                new_name, new_number, new_team = line
                driver.append(line)  #writes the data into the list
   
        random.shuffle(driver)    #shuffles the drivers
    
        position = 1        #position set to 1

        Pos = "Position"  #assigns 3 variables with their corresponding names
        Name = "Name"
        Time = "Interval" 
        print("\n---------RACE RESULTS---------")  #prints the race results
        print(f"\n{Pos:<9} {Name:<11} {Time} ")
        

        for line in driver:
            new_name, new_number, new_team = line
            lap_add = random.uniform(0, add_time)
            lap_time = round(lap_add, 3)    #round time to 3 decimal place
        
            if position == 1:                   #if the position is 1 then there is no time interval to the next driver
                print(f"{position:<9} {new_name:<11}    -")
                position = position + 1        #adds position to next column
            else:                          #the rest of the drivers have a time interval so the time is printed out
                print(f"{position:<9} {new_name:<11} +{lap_time:.3f}")
                position = position + 1        #add position to next column


#uses user input in the main menu to select which function to use
race_name = "Unselected"    #pre-assigns 3 variables
wet = 0
dry = 0
def main(race_name,wet,dry):
    while True:             #runs the program until user decides to exit
        opt = display_menu()    #returns the variable from the menu
        if opt == 1:      #when opt is equal to 1
            print("\n--------------VIEW GRID--------------")
            view_grid()       #runs the function 
        elif opt == 2:           
            print("\nRESET GRID")
            reset_grid()
        elif opt == 3:           
            print("\n---------------------CREATE TEAM---------------------\n")   
            create_team()
        elif opt == 4:
            print("\n-----------------CHOOSE TRACK-----------------")  
            race_name, wet, dry = race_track()      #passes the variables
        elif opt == 5:
            print("\n----------------START QUALIFYING----------------")
            qualifying(race_name, wet, dry)         #passes the variables
        elif opt == 6: 
            print("\n--------------START RACE--------------")  
            race(race_name)                
        elif opt == 7:
             print("Exit")
             return            #breaks the loop when the user wants to exit

if __name__ == "__main__":
    main(race_name,wet,dry)  #return variables