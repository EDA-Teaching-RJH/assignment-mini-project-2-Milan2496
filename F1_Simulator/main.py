from models import name

def display_menu():
    print("\n--- F1 ---")
    print("1. View Grid")
    print("2. Register Driver")
    print("4. Start Qualifying")
    print("5. Start Race")
    opt = int(input("\nSelect option: "))
    return opt



def main():
    
    run = True
    while True:    
        opt = display_menu()
        if opt == 1:
            register_driver(name, number, team, skill)         
        elif opt == 9:
             print("Shutting down.")
             return


main()