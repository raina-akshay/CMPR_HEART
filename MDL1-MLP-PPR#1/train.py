#import pandas as pd
from sklearn.neural_network import MLPClassifier as mlp
from sklearn.metrics import confusion_matrix, accuracy_score
from datahandle import datasetpartition as dsp
#from sklearn.model_selection import cross_val_score
#import pandas as pd

X_train, X_test, y_train, y_test=dsp(part=0,n=0.15)
clf= mlp(solver='sgd', hidden_layer_sizes=(200,), random_state=1, max_iter=1000)
clf.fit(X_train, y_train)
pred=clf.predict(X_test)
predictions = clf.score(X_test,y_test)

cm=confusion_matrix(y_test, pred)
print(cm)

acc=accuracy_score(y_test,pred)
print(acc)

##f=pd.read_csv('cleveland.csv')
#a = f.iloc[:, :-1].values
#b = f.iloc[:, -1].values

#score=cross_val_score(clf, a, b, cv=10)