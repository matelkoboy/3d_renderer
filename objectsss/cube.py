from objectsss.objectcomponents.point import Point
from objectsss.objectcomponents.polygon import Poly
from visual.mesh_utils import dist_of_points

class Brick:
    def __init__(self, point_1, point_2):
        # point_1 ---- top left back
        # point_2 ---- bottom right front
        top_left_back = Point(point_1.x, point_1.y, point_1.z)
        top_right_back = Point(point_2.x, point_1.y, point_1.z)
        top_right_front = Point(point_2.x, point_1.y, point_2.z)
        top_left_front = Point(point_1.x, point_1.y, point_2.z)
        bottom_left_back = Point(point_1.x, point_2.y, point_1.z)
        bottom_right_back = Point(point_2.x, point_2.y, point_1.z)
        bottom_right_front = Point(point_2.x, point_2.y, point_2.z)
        bottom_left_front = Point(point_1.x, point_2.y, point_2.z)
        
        self.sides = [
            Poly(top_left_back, top_right_back, top_right_front, top_left_front), #top
            Poly(top_right_front, top_left_front, bottom_left_front, bottom_right_front), #front
            Poly(top_left_front, top_left_back, bottom_left_back, bottom_left_front), #left
            Poly(top_left_back, top_right_back, bottom_right_back, bottom_left_back), #back
            Poly(top_right_front, top_right_back, bottom_right_back, bottom_right_front), #right
            Poly(bottom_left_back, bottom_right_back, bottom_right_front, bottom_left_front), #bottom
        ]
        
        
    def for_render(self):
        return self.sides