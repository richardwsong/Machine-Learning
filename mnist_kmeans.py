# from keras.datasets import mnist
# from matplotlib import pyplot
# from tensorflow import keras
# import numpy as np
# from sklearn.cluster import KMeans
# from sklearn.linear_model import LogisticRegression
#
# def load_dataset():
#     (trainX, trainY), (testX, testY) = mnist.load_data()
#
#     trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
#     testX = testX.reshape((testX.shape[0], 28, 28, 1))
#
#     trainY = keras.utils.to_categorical(trainY)
#     testY = keras.utils.to_categorical(testY)
#
#     return trainX, trainY, testX, testY
#
#
# def prep_pixels(train, test):
#     # convert from integers to floats
#     train_norm = train.astype('float32')
#     test_norm = test.astype('float32')
#     # normalize to range 0-1
#     train_norm = train_norm / 255.0
#     test_norm = test_norm / 255.0
#     # return normalized images
#     return train_norm, test_norm
#
# trainX, trainY, testX, testY = load_dataset()
# log_reg = LogisticRegression(random_state=42)
# log_reg.fit(trainX, trainY)
# log_reg.score(testX, testY)
# from sklearn.datasets import load_digits
# X_digits, y_digits = load_digits(return_X_y=True)
import pickle
from sklearn.datasets import fetch_openml

# X_digits, y_digits = fetch_openml('mnist_784', version=1, cache=True, as_frame=False, return_X_y=True)
#
# outfile = open("file", 'wb')
# pickle.dump((X_digits, y_digits), outfile)
# outfile.close()
#
# print("done")
#
# infile = open("file", 'rb')
# val = pickle.load(infile)
# infile.close()
# from sklearn.model_selection import train_test_split
#
# X_train, X_test, y_train, y_test = train_test_split(val[0], val[1])
#
# outfile = open("file2", 'wb')
# pickle.dump((X_train, X_test, y_train, y_test), outfile)
# outfile.close()
# print("done")

infile = open("file2", "rb")
vals = pickle.load(infile)
infile.close()
X_train = vals[0]
X_test = vals[1]
y_train = vals[2]
y_test = vals[3]

from sklearn.linear_model import LogisticRegression


from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
pipeline = Pipeline([
 ("kmeans", KMeans(n_clusters=40)),
 ("log_reg", LogisticRegression()),
])
pipeline.fit(X_train, y_train)
print(pipeline.score(X_test, y_test))

# from sklearn.model_selection import GridSearchCV
#
# param_grid = dict(kmeans__n_clusters=range(2,100))
# grid_clf = GridSearchCV(pipeline, param_grid, cv=3, verbose=2)
# grid_clf.fit(X_train, y_train)
# print(grid_clf.best_params_)
# print(grid_clf.score(X_test, y_test))