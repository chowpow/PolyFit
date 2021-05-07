import numpy as np


class Model:
    xMatrix = []
    yMatrix = []
    degree = 0

    def __init__(self, x_matrix, y_matrix, degree):
        self.xMatrix = x_matrix
        self.yMatrix = y_matrix
        self.degree = degree

    def create_matrix(self):
        A = np.vander(self.xMatrix, (self.degree + 1), increasing=True)
        return A

    def calculate_result(self):
        A = self.create_matrix()
        yMatrix = np.matrix(self.yMatrix).T
        c = np.linalg.inv(A.T @ A) @ (A.T @ yMatrix)
        c = c.flatten().tolist()[0]
        return c
