# import keras as kr 
# import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from numpy import loadtxt


# first neural network with keras tutorial
# load dataset and split into input(X) and output (y) variables
file1 = r'F:\FirefoxDownloads\pima-indians-diabetes.csv'
dataset = loadtxt(file1, delimiter=',')
X = dataset[:, 0:8]
y = dataset[:, 8]

# #define the keras model
# model = kr.models.Sequential()
# model.add(kr.layers.Dense(12, input_dim=8, activation='relu'))
# model.add(kr.layers.Dense(8, activation='relu'))
# model.add(kr.layers.Dense(1, activation='sigmoid'))
#define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)

# evaluate the keras model
# _, accuracy = model.evaluate(X, y)
# print('Accuracy: %.2f' % (accuracy*100))

#make class predictions with the model
predictions = model.predict_classes(X)

# summarize the first 5 cases
for i in range(5):
  print('%s => %d (expercted %d)' % (X[i].tolist(), predictions[i], y[i]))