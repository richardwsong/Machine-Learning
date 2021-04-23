import pickle
infile = open("file2", "rb")
vals = pickle.load(infile)
infile.close()
X_train = vals[0]
X_test = vals[1]
y_train = vals[2]
y_test = vals[3]

from keras import models
from keras import layers
from keras.utils import to_categorical

network = models.Sequential()
network.add(layers.Dense(784, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(784, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(784, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(784, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))
network.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

network.fit(X_train, y_train, epochs=5, batch_size=64)
test_loss, test_acc = network.evaluate(X_test, y_test)
print('test_acc:', test_acc, 'test_loss', test_loss)