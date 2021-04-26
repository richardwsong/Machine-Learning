import pickle
infile = open("file2", "rb")
vals = pickle.load(infile)
infile.close()
X_train = vals[0]
X_test = vals[1]
y_train = vals[2]
y_test = vals[3]

from sklearn import svm, metrics

clf = svm.SVC(kernel='poly', degree=3, coef0=1, C=5)
clf.fit(X_train, y_train)
predicted = clf.predict(X_test)

print(f"Classification report for classifier {clf}:\n"
      f"{metrics.classification_report(y_test, predicted)}\n")

# Classification report for classifier SVC(C=5, coef0=1, kernel='poly'):
#               precision    recall  f1-score   support
#
#            0       0.99      0.99      0.99      1773
#            1       0.99      0.99      0.99      1964
#            2       0.98      0.98      0.98      1817
#            3       0.97      0.97      0.97      1709
#            4       0.98      0.98      0.98      1700
#            5       0.97      0.97      0.97      1558
#            6       0.98      0.98      0.98      1679
#            7       0.98      0.98      0.98      1852
#            8       0.98      0.98      0.98      1715
#            9       0.97      0.96      0.97      1733
#
#     accuracy                           0.98     17500
#    macro avg       0.98      0.98      0.98     17500
# weighted avg       0.98      0.98      0.98     17500
#~200 seconds