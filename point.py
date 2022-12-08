class Point:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"