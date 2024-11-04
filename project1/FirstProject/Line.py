import math
class Line :
    def __init__(self, start=(0,0), end=(0,0), color = 'black'):
        self.start = start
        self.end = end
        self.color = color
    def show(self):
        print(f"from {self.start} to {self.end}")
        print(f"with {self.color}")
    def length(self):
        dx = self.start[0] - self.end[0]
        dy = self.start[1] - self.end[1]
        return math.sqrt(dx**2 + dy**2)
