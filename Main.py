import sys
from ast import literal_eval

import numpy as np
from pip._vendor.distlib.compat import raw_input
from Model import Model


class Main:
    degree = 0
    def get_points(self):
        try:
            coords = [literal_eval(coord) for coord in raw_input("Please enter your points Ex: (3,0) (0,0) ").split()]
            for coord in coords:
                print(coord[0])
            self.degree = int(input("What degree polynomial: "))
        except ValueError:
            print("Please enter the coordinates in the format mentioned")
            exit()
        
        self.create_lists(coords)
    
    def create_lists(self, data):
        xList = []
        yList = []
        for coord in data:
            xList.append(coord[0])
            yList.append(coord[1])
        print(xList)
        print(yList)    
        model = Model(xList, yList, self.degree)
        model.calculate_result()

main = Main()
main.get_points()