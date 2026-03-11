
class Track:
    def __init__(self, track_name, best_time, wet_time, dry_time):
        self.track_name = track_name
        self.best_time = best_time
        self.wet_time = wet_time
        self.dry_time = dry_time

    def display(self):
        print(f"Name: {self.new_name} | #{self.new_number} | Team: {self.new_team}")