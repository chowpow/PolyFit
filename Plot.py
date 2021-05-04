import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    xVals = []
    yVals = []
    solnMatrix = []
    degree = 0

    def __init__(self, xVals, yVals, solnMatrix, degree):
        self.xVals = xVals
        self.yVals = yVals
        self.solnMatrix = solnMatrix
        self.degree = degree

    def reg(self, t):
        eqn = self.solnMatrix[0]
        for x in range(1, self.degree+1):
            eqn = eqn + self.solnMatrix[x]*t**x  
        return eqn

    def plot(self):
        t = np.arange(min(self.xVals)-1, max(self.xVals)+1, 0.1)
        plt.plot(t, self.reg(t), 'red', self.xVals, self.yVals, 'bo')
        plt.show()