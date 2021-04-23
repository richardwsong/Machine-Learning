# import pickle
# infile = open("file2", "rb")
# vals = pickle.load(infile)
# infile.close()
# X_train = vals[0]
# X_test = vals[1]
# y_train = vals[2]
# y_test = vals[3]

def euclidean (a1, a2):
    dist = 0
    for i in range(0, len(a1)):
        dist += (a1[i]-a2[i])**2
    return dist

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits

X_digits, y_digits = load_digits(return_X_y=True)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_digits, y_digits)

k = 5
kmeans = KMeans(n_clusters=k)
y_pred = kmeans.fit_predict(X_train)
array = kmeans.cluster_centers_

it = -1
success = 0
for i in X_test:
    it+=1
    clust = -1
    val = 100000000
    for j in range(0,5):
        dist = euclidean(i, array[j])
        if dist<val:
            val = dist
            clust = j
    iterate = 0
    dist = 10000000
    for j in range(0, len(y_pred)):
        if y_pred[j] != clust:
            continue
        else:
            val = euclidean(X_train[j], i)
            if val < dist:
                dist = val
                iterate = j
    if y_train[iterate] == y_test[it]:
        success += 1
print(success/it)


# model = KNeighborsClassifier(n_neighbors=1)
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)
# print(classification_report(y_test, predictions))
#
#
#  import pickle
#  infile = open("file2", "rb")
#  vals = pickle.load(infile)
# infile.close()
# X_train = vals[0]
# X_test = vals[1]
#  y_train = vals[2]
# y_test = vals[3]
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import classification_report
#
# model = KNeighborsClassifier(n_neighbors=1)
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)
# print(classification_report(y_test, predictions))
#
# MNIST dataset, 60k train and 10k test. 97% accuracy in 30 seconds
#
# Do MNIST with k=5. Iterate through the test points and compare with each of the cluster centroids. With the closest centroid, iterate through the points in it and compare Euclidean distance between the coordinates. Find the smallest Euclidean Distance and compare y values.
#
#
# def euclidean(a1, a2):
#     dist = 0
#     for i in range(0, 28):
#         dist += (a1[i] - a2[i]) ** 2
#     return dist
#
#
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import classification_report
# from sklearn.cluster import KMeans
# from sklearn.datasets import load_digits
#
# X_digits, y_digits = load_digits(return_X_y=True)
#
# from sklearn.model_selection import train_test_split
#
# X_train, X_test, y_train, y_test = train_test_split(X_digits, y_digits)
#
# k = 5
# kmeans = KMeans(n_clusters=k)
# y_pred = kmeans.fit_predict(X_train)
# array = kmeans.cluster_centers_
#
# it = -1
# success = 0
# for i in X_test:
#     it += 1
#     clust = -1
#     val = 100000000
#     for j in range(0, 5):
#         dist = euclidean(i, array[j])
#         if dist < val:
#             val = dist
#             clust = j
#     iterate = 0
#     dist = 10000000
#     for j in range(0, len(y_pred)):
#         if j != clust:
#             continue
#         else:
#             val = euclidean(X_train[j], i)
#             if val < dist:
#                 dist = val
#                 iterate = j
#     if y_train[iterate] == y_test[it]:
#         success += 1
# print(success / it)
