class traintest:
    from sklearn.neural_network import MLPClassifier as mlp
    from datahandle import handle_data as hd
    dat=hd()
    dat.read_data()
    
    def __init__(self):
        print('''\t 'kf: if k-fold required (boolean, optional, default=True)' \n \t 'n: proportion to split data if kf=0 (float(0-1), optional, default=0.2)' \n \t 'k: folds for partition if kf=1 (integer, optional, default=10)' ''')
        self.kf=input('\t ENTER A VALUE (OPTIONAL: HIT ENTER TO SKIP) FOR kf: \t') or 'True'
        self.n=input('\t ENTER A VALUE (OPTIONAL: HIT ENTER TO SKIP) FOR n: \t') or 0.2; self.n=float(self.n) 
        self.k=input('\t ENTER A VALUE (OPTIONAL: HIT ENTER TO SKIP) FOR k: \t') or 10; self.k=int(self.k) 
        
        self.part_op=None
    
    def kfold(self, result):
        if not len(result)==3:
            print('kFold not possible!')
        else:
            X,y,splt=result
            predictions={}; y_test={}; prob={}; i=1;
            
            for trn_id, tst_id in splt:
                X_trn, X_tst, y_trn, y_tst = X[trn_id], X[tst_id] ,\
                                             y[trn_id], y[tst_id]
               #TRAINING
                clf= self.mlp(solver='sgd', hidden_layer_sizes=(200,), random_state=1, max_iter=1000)
                clf.fit(X_trn, y_trn)
               #Evaluation
                pred=clf.predict(X_tst)
                proba=clf.predict_proba(X_tst)
                predictions[i]=pred; y_test[i]=y_tst; prob[i]=proba; i+=1;
        print('\n Multilayer Perceptron Network trained with sgd solver and kfold!!!')
        return y_test,predictions,prob
    
    def split(self,result):
        if not len(result)==4:
            print('The data- split is not possible!')
        else:
            #TRAINING
            X_train, X_test, y_train, y_test = result
            clf=self.mlp(solver='sgd',hidden_layer_sizes=(200,),random_state=1,max_iter=1000)
            clf.fit(X_train, y_train)
            
            #Evaluation
            predictions=clf.predict(X_test)
            prob=clf.predict_proba(X_test)
            print('\n Multilayer Perceptron Network trained with sgd solver and data- split!!!')
            return y_test,predictions,prob
        
    def run(self):
        if self.kf in ['true','True','1','TRUE']:#executes only when part is set as one of ['true','True','1','TRUE']
            self.kf = True
            self.part_op=self.dat.partition(part=self.kf,m=self.n,f=self.k)
            return self.kfold(result=self.part_op)
        elif self.kf in ['false','False','0','FALSE']:#executes only when the argument, 'part' is set as one of ['false','False','0','FALSE']
            self.kf = False
            self.part_op=self.dat.partition(part=self.kf,m=self.n,f=self.k)
            return self.split(result=self.part_op)
        else:
            print('''THE ARGUMENT FOR'PART' IS NOT OF TYPE BOOLEAN. PLEASE RECHECK!''' )
            
            
            
            
if __name__ == '__main__':
    tnt = traintest()
    true, pred, proba = tnt.run()