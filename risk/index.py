from flask import Flask
from risk.modelbuilder import ModelBuilder
from risk.simulator import Simulator
from keras.optimizers import SGD
import numpy as np
from keras.models import load_model
app = Flask(__name__)

@app.route('/')
def index():
    return "Er kan gekozen worden voor /calculateProbability/#troop1/#troop2/#dobbelstenen of /startSim/"

@app.route('/calculateProbability/<troop1>/<troop2>')
def calculate(troop1, troop2):
    model = load_model("..\model\model.h5")
    model.compile(loss='binary_crossentropy', optimizer=SGD(lr=0.01, momentum=0.9))
    troops = preprocess(troop1, troop2)
    return str(model.predict(troops))

def startSimulator():
    print("Simulator is gestart")
    sim = Simulator(1500)
    xlist, ylist = sim.run()
    return xlist, ylist

def trainModel():
    xlist, ylist = startSimulator()
    modelBuilder = ModelBuilder(xlist, ylist, None)
    modelBuilder.generate_model()
    modelBuilder.train_model()

def preprocess(troop1, troop2):
    troops = np.array([troop1, troop2])
    troops = np.reshape(troops, (-1, 2))
    return troops

if __name__ == "__main__":
    trainModel()
    app.run(debug=True)
