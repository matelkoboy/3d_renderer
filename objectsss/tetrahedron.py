from objectsss.objectcomponents.point import Point
from objectsss.objectcomponents.polygon import Poly
from visual.mesh_utils import dist_of_points

class Tetrahedron:
    def __init__(self, point_1, point_2, point_3, point_4):
        
        self.sides = [
            Poly(point_1, point_2, point_3),
            Poly(point_1, point_2, point_4),
            Poly(point_1, point_3, point_4),
            Poly(point_2, point_3, point_4)
        ]
        
        
    def for_render(self):
        return self.sides