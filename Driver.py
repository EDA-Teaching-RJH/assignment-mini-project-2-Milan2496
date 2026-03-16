
class Driver:
    def __init__(self, new_name, new_number, new_team):
        self.new_name = new_name
        self.new_number = new_number
        self.new_team = new_team

    def display(self):
        print(f"{self.new_name:<12} #{self.new_number:<8} {self.new_team}")
        