from objectsss.objectcomponents.point import Point

class Poly:
    def __init__(self, *points):
        self.points = points
        
        x_avg = sum([p.x for p in self.points]) / len(self.points)
        y_avg = sum([p.y for p in self.points]) / len(self.points)
        z_avg = sum([p.z for p in self.points]) / len(self.points)
        
        self.midpoint = Point(x_avg, y_avg, z_avg)
    
    def __str__(self):
        return str(self.midpoint) + str(self.points[0]) + str(self.points[1]) + str(self.points[2])