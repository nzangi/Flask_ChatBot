import numpy as np


class LinearRegression:
    def __init__(self, lr=0.01, n_iterations=10000):
        self.lr = lr
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, Y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):
            y_predicated = np.dot(X, self.weights) + self.bias

            dw = (1 / n_samples) * np.dot(X.T, (y_predicated - Y))
            db = (1 / n_samples) * np.sum(y_predicated - Y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        y_predicated = np.dot(X, self.weights) + self.bias
        return y_predicated
