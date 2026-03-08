import random

class Driver:

    new_name = input("Last name: ")
    new_name = new_name.title()

    new_number = int(input("Driver number (2-99): "))
    while new_number < 2 or new_number > 99:
        new_number = int(input("Invalid number. Try again: ")) 
        
    team_list = [1,2,3]
    new_team = int(input("Choose team (1.Audi, 2.Mercedes, 3.Cadillac): "))     
    while new_team not in team_list:
        new_team = int(input("Invalid number. Try again: "))

    Audi = 0
    Merc = 0
    Cadillac = 0

    if Audi < 2 and Merc < 2 and Cadillac < 2:

        while True:
    

            if new_team == 1:
                if Audi < 2: 
                    new_team = "Audi"
                    Audi = Audi + 1
                else:
                    print("Team is full")
            elif new_team == 2:
                if Merc < 2: 
                    new_team = "Mercedes"
                    Merc = Merc + 1
                else:
                    print("Team is full")
            elif new_team == 3:
                if Cadillac < 2: 
                    new_team = "Cadillac"
                    Cadillac = Cadillac + 1
                else:
                    print("Team is full")

    else:
        print("Grid is full, no more drivers")

    new_skill = random.randint(5, 10)
    
    new_number = str(new_number)
    new_skill = str(new_skill)

    file = open("Drivers.txt", "w")
    file.write(new_name)
    file.close()
    
    file = open("Teams.txt", "w")
    file.write(new_team)
    file.close()
    
    file = open("Number.txt", "w")
    file.write(new_number)
    file.close()