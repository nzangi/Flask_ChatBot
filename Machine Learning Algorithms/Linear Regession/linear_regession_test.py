# importing libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from linear_regression import LinearRegression

# loading dataset
X, Y = datasets.make_regression(n_samples=1000, n_features=1, noise=20, random_state=4)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=4)

# plotting the graph
# fig = plt.figure(figsize=(8,8))
# plt.scatter(X[:,0],Y,color = 'b',marker='o',s = 40)
# plt.show()

regressor = LinearRegression(lr=0.01)
regressor.fit(X_train, Y_train)
predicted = regressor.predict(X_test)


# calculate MSE
def mse(y_true, y_predicated):
    return np.mean((y_true - y_predicated) ** 2)


mse_value = mse(Y_test, predicted)
print(mse_value)

# plot graph
y_predict_line = regressor.predict(X)
cmap = plt.get_cmap("viridis")
fig = plt.figure(figsize=(8, 8))
m1 = plt.scatter(X_train, Y_train, color=cmap(0.9), s=10)
m2 = plt.scatter(X_train, Y_train, color=cmap(0.5), s=10)
plt.plot(X, y_predict_line, color='black', linewidth=2, label="Prediction")
plt.show()

# print X and Y datashape
# print(mse)
# print(X_train.shape)
# print(Y_train.shape)
