# importing required libaries
import random
from math import exp

random.seed(0)


# Defining our main class
class LogisticRegression:
    # initializing the class
    def __init__(self, weight=0.1, alpha=0.15):
        self.alpha = alpha
        self.weight = weight

    # Make a prediction with coefficients
    def predict(self, row, coefficients):
        y = coefficients[0]
        for j in range(len(row) - 1):
            y = y + coefficients[j + 1] * row[j]
        # sigmoid function
        return 1.0 / (1.0 + exp(-y))

    # defining the training function
    def train(self, dataset, labels, n=200):
        counter = 0
        error = []
        for row in dataset:
            row.append(labels[counter])
            counter = counter + 1
        # Estimate the regression coefficients using the stochastic gradient descent
        coeficient = [self.weight for j in range(len(dataset[0]))]
        for epoch in range(n):
            # reshuffling the dataset
            random.shuffle(dataset)
            summazation_error = 0
            for row in dataset:
                y = self.predict(row, coeficient)
                my_error = row[-1] - y
                summazation_error = summazation_error + (my_error ** 2)
                coeficient[0] = coeficient[0] + self.alpha * my_error * y * (1.0 - y)
                for j in range(len(row) - 1):
                    coeficient[j + 1] = coeficient[j + 1] + self.alpha * my_error * y * (1.0 - y) * row[j]
            error.append(summazation_error)
        self.coefficient = coeficient
        return error

    # declaring a classify function
    def classify(self, dataset, threshold):
        predicted_values = []
        # predicting the labels either 0,1
        for row in dataset:
            y = self.predict(row, self.coefficient)
            # appealing the predicted values into a predicted_values myList
            if y <= threshold:
                predicted_values.append(0)
            else:
                predicted_values.append(1)
        return predicted_values


def printRounded(myList):
    print("[", end="")
    for i in range(len(myList) - 1):
        print(str(round(myList[i], 7)), end=",")
    print(str(round(myList[-1])), end="]\n")


# performing the computation of the data
def calculate():
    dataset = [[0, 0], [1, 0], [2, 1], [1, 2], [3, 1], [4, 1], [5, 2], [3, 3], [2, 5]]
    labels = [0, 0, 0, 0, 0, 1, 1, 1, 1]
    lr = LogisticRegression()
    MSEList = lr.train(dataset, labels, 20)
    predictedLabels = lr.classify(dataset, 0.5)
    print(predictedLabels)
    printRounded(MSEList)


calculate()
