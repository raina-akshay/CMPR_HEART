def train(kf, n=0.2, k=10):
    import pandas as pd
    from sklearn.neural_network import MLPClassifier as mlp
    from sklearn.metrics import confusion_matrix, accuracy_score
    from datahandle import datasetpartition as dsp
    from sklearn.model_selection import KFold
    from sklearn.model_selection import cross_val_score
    import statistics as st    
    try:
        X_train, X_test, y_train, y_test=dsp(part=kf,m=n,f=k)
        clf= mlp(solver='sgd', hidden_layer_sizes=(200,), random_state=1, max_iter=1000)
        clf.fit(X_train, y_train)
        print('\n Multilayer Perceptron Network trained with sgd solver!!')
    except:
        splt=dsp(part=kf,m=n,f=k)
        for trn_id, tst_id in splt:
            X_trn, X_tst, y_trn, y_tst = X[trn_id], X[tst_id] ,\
                                         y[trn_id], y[tst_id]
        clf= mlp(solver='sgd', hidden_layer_sizes=(200,), random_state=1, max_iter=1000)
        clf.fit(X_trn, y_trn)
        
        
