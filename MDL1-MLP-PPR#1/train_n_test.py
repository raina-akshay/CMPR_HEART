def traintest(kf, n, k):
    from sklearn.neural_network import MLPClassifier as mlp
    from datahandle import datasetpartition as dsp
    try: 
        X_train, X_test, y_train, y_test=dsp(part=kf,m=n,f=k)
       #TRAINING
        clf= mlp(solver='sgd', hidden_layer_sizes=(200,), random_state=1, max_iter=1000)
        clf.fit(X_train, y_train)
       #TESTING
        predictions=clf.predict(X_test)
        prob=clf.predict_proba(X_test)
    except:
        X,y,splt=dsp(part=kf,m=n,f=k)
        predictions={}; y_test={}; prob={}; i=1;     
        for trn_id, tst_id in splt:
            X_trn, X_tst, y_trn, y_tst = X[trn_id], X[tst_id] ,\
                                         y[trn_id], y[tst_id]
           #TRAINING
            clf= mlp(solver='sgd', hidden_layer_sizes=(200,), random_state=1, max_iter=1000)
            clf.fit(X_trn, y_trn)
           #TESTING
            pred=clf.predict(X_tst)
            proba=clf.predict_proba(X_tst)
            predictions[i]=pred; y_test[i]=y_tst; prob[i]=proba; i+=1;
    finally:
        print('\n Multilayer Perceptron Network trained with sgd solver!!')
        return y_test,predictions,prob
        
    
