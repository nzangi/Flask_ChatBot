from math import exp
import random

random.seed(0)


class LogisticRegression:
    def __init__(self, weight=0.1, alpha=0.15, learning_rate=0.001):
        self.alpha = alpha
        self.weight = weight
        self.learning_rate = learning_rate

    def predict(self, row, coefficients):
        y = coefficients[0]
        for i in range(len(row) - 1):
            y += coefficients[i + 1] * row[i]
        return 1.0 / (1.0 + exp(-y))

    def train(self, dataset, labels, n=200):
        count = 0
        err = []
        for row in dataset:
            row.append(labels[count])
            count += 1

        coef = [self.weight for i in range(len(dataset[0]))]

        for epoch in range(n):
            random.shuffle(dataset)
            sum_error = 0
            for row in dataset:
                y = self.predict(row, coef)
                error = row[-1] - y
                sum_error += error ** 2
                coef[0] = coef[0] + self.learning_rate + self.alpha * error * y * (1.0 - y)
                for i in range(len(row) - 1):
                    coef[i + 1] = coef[i + 1] + self.learning_rate + self.alpha * error * y * (1.0 - y) * row[i]
            err.append(sum_error)
        self.coefficient = coef
        return err
#predicting the labels either 0,1
    def classify(self, dataset, threshold):
        predicted_values = []
        for row in dataset:
            y = self.predict(row, self.coefficient)
            if (y <= threshold):
                predicted_values.append(0)
            else:
                predicted_values.append(1)
        return predicted_values



def printRounded(myList):
    print("[", end="")
    for i in range(len(myList) - 1):
        print(str(round(myList[i], 7)), end=", ")
    print(str(round(myList[-1], 7)), end="]\n")


lr = LogisticRegression()
dataset = [[0, 0], [1, 0], [2, 1], [1, 2], [3, 1], [4, 1], [5, 2], [3, 3], [2, 5]]
labels = [0, 0, 0, 0, 0, 1, 1, 1, 1]
MSEList = lr.train(dataset, labels, 20)
predictedLabels = lr.classify(dataset, 0.5)
print(predictedLabels)
printRounded(MSEList)



