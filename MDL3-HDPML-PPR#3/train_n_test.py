from datahandle import handle_data
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.linear_model import LogisticRegression as lr
from sklearn.naive_bayes import GaussianNB as gnb

dat=handle_data('cleveland')
dat.read_data()
X_train, X_test,y_train, y_test=dat.partition()

models = [rfc(), dtc(), lr(), gnb()]

def pred_prob(model):
    model.fit(X_train, y_train)
    true = y_test
    pred = model.predict(X_test)
    prob = model.predict_proba(X_test)
    return true, pred, prob