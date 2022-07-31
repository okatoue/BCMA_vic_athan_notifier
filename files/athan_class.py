from datetime import datetime

class Athan:
    def __init__(self, prayer, time):
        self.prayer = prayer
        full_time = datetime.strptime(time, '%I:%M %p')
        self.time = full_time.strftime('%I:%M')

    def time_to_pray(self):
        return "Its time to pray " + self.prayer

    def reminder(self):
        return "15 minutes left before " + self.prayer + " ends!"
