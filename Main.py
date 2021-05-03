import sys
from ast import literal_eval

import numpy as np
from pip._vendor.distlib.compat import raw_input


class Main:
    def get_points(self):
        try:
            coords = [literal_eval(coord) for coord in raw_input("Please enter your points Ex: (3,0) (0,0) ").split()]
            for coord in coords:
                print(coord[0])
        except ValueError:
            print("Please enter the coordinates in the format mentioned")
            exit()

main = Main()
main.get_points()