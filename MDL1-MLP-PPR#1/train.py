#import pandas as pd
from sklearn.neural_network import MLPClassifier as mlp
from datahandle import datasetpartition as dsp

X_train, X_test, y_train, y_test=dsp(part=0)
clf= mlp(solver='sgd', hidden_layer_sizes=(5,2), random_state=1, max_iter=1000)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)