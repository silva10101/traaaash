import numpy as np


def sigmoid(x):
    '''функция активации'''
    return 1 / (1 + np.exp(-x))


class Neuron:
    '''класс нейрона'''

    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        '''
        Вход: вес и смещение
        Выход: результат функции
        '''
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)


class Neural_network:
    '''
    Нейронная сеть
    -2 входа x
    -1 скрытый слой(2 нейрона) h
    -1 выход o
    у каждого нейрона одинаковый вес и смещение
    '''

    def __init__(self):
        weights = np.array([0, 1])
        bias = 0

        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)

    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)

        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))

        return out_o1


network = Neural_network()
x = np.array([2, 3])
print(network.feedforward(x))
