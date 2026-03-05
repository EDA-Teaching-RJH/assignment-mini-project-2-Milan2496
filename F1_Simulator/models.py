

name = input("Driver Name:")

file = open("Drivers.txt", "w")
file.write(name)
file.close()
