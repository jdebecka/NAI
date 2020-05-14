import numpy as np

# Activation (sigmoid) function


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Output (prediction) formula
def output_formula(features, weights, bias):
    return sigmoid(np.dot(weights, features) - bias)


# Error (log-loss) formula
def error_formula(y, y_hat):
    return np.dot(np.dot((y - y_hat), y), (1 - y))
    #return -y * np.log(y_hat) - (1 - y) * np.log(1 - y_hat)


def update_weights(arr, errors, weights, bias, learn_rate):
    for weight, error in zip(weights, errors):
        for letter in arr:
            weight += letter * error * learn_rate
    bias -= errors * learn_rate
    return weights, bias
