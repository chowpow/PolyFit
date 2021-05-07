from ast import literal_eval

from pip._vendor.distlib.compat import raw_input
from Model import Model
from Plot import Plotter


class Main:
    degree = 0
    x_list = []
    y_list = []
    regResult = []

    def get_points(self):
        try:
            coords = [literal_eval(coord) for coord in raw_input("Please enter your points Ex: (3,0) (0,0) ").split()]
            print(coords)
            self.degree = int(input("What degree polynomial: "))
        except ValueError:
            print("Please enter the coordinates in the format mentioned")
            exit()

        return coords

    def create_lists(self):
        data = self.get_points()
        self.x_list = []
        self.y_list = []
        print(data)
        for coord in data:
            self.x_list.append(coord[0])
            self.y_list.append(coord[1])

    def create_lists_web(self, data, degree):
        self.degree = degree
        self.x_list = []
        self.y_list = []
        for coord in data:
            self.x_list.append(coord[0])
            self.y_list.append(coord[1])
        return self.x_list

    def get_model_result(self):
        model = Model(self.x_list, self.y_list, self.degree)
        self.regResult = model.calculate_result()

    def get_model_result_web(self):
        model = Model(self.x_list, self.y_list, self.degree)
        return model.calculate_result()

    def get_plot(self):
        plotter = Plotter(self.x_list, self.y_list, self.regResult, self.degree)
        plotter.plot()


# main = Main()
# main.create_lists()
# main.get_model_result()
# main.get_plot()

# while True:
#     main = Main()
#     main.create_lists()
#     main.get_model_result()
#     main.get_plot()

# while True:
#     main = Main()
#     main.create_lists()
#     print(main.get_model_result_web())

