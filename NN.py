import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


training_in = np.array([[0, 0, 1],
                        [1, 1, 1],
                        [1, 0, 1],
                        [0, 1, 1]])

training_out = np.array([[0, 1, 1, 0]]).T

np.random.seed(1)

synaptic_w = 2 * np.random.random((3, 1)) - 1

print("\n Random weights:")
print(synaptic_w)

# Метод обратного распространения

for i in range(2000):
    input_layer = training_in
    outputs = sigmoid(np.dot(input_layer, synaptic_w))

    err = training_out - outputs
    adjustment = np.dot(input_layer.T, err * (outputs * (1 - outputs)))

    synaptic_w += adjustment

print('\n Weights after leaning:')
print(synaptic_w)

print('\n Results after leaning:')
print(outputs)

# Test

new_in = np.array([1, 1, 1])
new_out = sigmoid(np.dot(new_in, synaptic_w))

print('\n New results after leaning:')
print(new_out)
