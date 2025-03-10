from typing import Literal
from copy import deepcopy


class Face:
    def __init__(self,width:int,height:int,colors: list[list[int]]):
        self.width = width
        self.height = height
        self.colors = colors

        self._create_circle()

    def _create_circle(self):
        self.circle = []
        

    def turn(self,distance:Literal[90,-90,180,-180],left_face,right_face,up_face,down_face):
        new_colors = deepcopy(self.colors)




class Cube:
    def __init__(self,faces=6,face_width=3,face_height=3):
        self.cube = []
        for i in range(faces):
            self.cube