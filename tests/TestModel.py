import unittest
from keras.optimizers import SGD
import numpy as np
from keras.models import load_model
from risk.simulator import Simulator
from risk.modelbuilder import ModelBuilder

class TestModel(unittest.TestCase):

    def testSimulator(self):
        sim = Simulator(1500)
        xlist, ylist = sim.run()
        self.assertTrue(type(xlist) is list)
        self.assertTrue(type(ylist) is list)

    def testUseCase(self):
        model = load_model("../model/model.h5")
        model.compile(loss='binary_crossentropy', optimizer=SGD(lr=0.01, momentum=0.9))
        troops = np.array([4, 6])
        troops = np.reshape(troops, (-1, 2))
        solution = str(model.predict(troops))
        print(solution)
        self.assertTrue(type(solution) is str)




