import numpy as np


class RandomGenerator(object):

    def __init__(self):
        pass

    @staticmethod
    def generate():
        return np.random.random_integers(1, 10, size=(1, 10))
