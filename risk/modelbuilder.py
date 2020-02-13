import numpy as np
import random
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizers import Adam
from collections import deque
import math

class ModelBuilder:
    def __init__(self, xlist, ylist, empty):
        if empty is None:
            self.xlist = xlist
            self.ylist = ylist
            self.model = None
        else:
            self.model = None

    def generate_model(self):
        model = Sequential()
        model.add(Dense(24, input_dim=2, activation='sigmoid'))
        model.add(Dense(48, activation='relu'))
        model.add(Dense(96, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.01, decay=0.01))
        self.model = model

    def get_model(self):
        return self.model

    def train_model(self):
        self.model.fit(np.array(self.xlist), np.array(self.ylist), batch_size=len(self.xlist), verbose=0)
        self.model.save("..\model\model.h5")

    def predict(self, troops1, troops2):
        troops = np.array([troops1, troops2])
        troops = np.reshape(troops, (-1,2))
        return self.model.predict(troops)
