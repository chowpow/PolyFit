from ast import literal_eval

from pip._vendor.distlib.compat import raw_input
from Model import Model
from Plot import Plotter


class Main:
    degree = 0
    xList = []
    yList = []
    regResult = []

    def get_points(self):
        try:
            coords = [literal_eval(coord) for coord in raw_input("Please enter your points Ex: (3,0) (0,0) ").split()]
            self.degree = int(input("What degree polynomial: "))
        except ValueError:
            print("Please enter the coordinates in the format mentioned")
            exit()

        return coords

    def create_lists(self):
        data = self.get_points()
        for coord in data:
            self.xList.append(coord[0])
            self.yList.append(coord[1])

    def get_model_result(self):
        model = Model(self.xList, self.yList, self.degree)
        self.regResult = model.calculate_result()

    def get_plot(self):
        plotter = Plotter(self.xList, self.yList, self.regResult, self.degree)
        plotter.plot()


main = Main()
main.create_lists()
main.get_model_result()
main.get_plot()
