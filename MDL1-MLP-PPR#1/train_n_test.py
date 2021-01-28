def train(kf, n=0.2, k=10):
    from sklearn.neural_network import MLPClassifier as mlp
    from datahandle import datasetpartition as dsp
    try: 
        X_train, X_test, y_train, y_test=dsp(part=kf,m=n,f=k)
       #TRAINING
        clf= mlp(solver='sgd', hidden_layer_sizes=(200,), random_state=1, max_iter=1000)
        clf.fit(X_train, y_train)
        print('\n Multilayer Perceptron Network trained with sgd solver!!')
       #TESTING
        predictions=clf.predict(X_test)
    except:
        X,y,splt=dsp(part=kf,m=n,f=k)
        predictions={}; y_test={}; i=1;     
        for trn_id, tst_id in splt:
            X_trn, X_tst, y_trn, y_tst = X[trn_id], X[tst_id] ,\
                                         y[trn_id], y[tst_id]
           #TRAINING
            clf= mlp(solver='sgd', hidden_layer_sizes=(200,), random_state=1, max_iter=1000)
            clf.fit(X_trn, y_trn)
            print('\n Multilayer Perceptron Network trained with sgd solver!!')
           #TESTING
            pred=clf.predict(X_tst)
            predictions[i]=pred; y_test[i]=y_tst; i+=1;
    finally:
        return y_test,predictions
        
    