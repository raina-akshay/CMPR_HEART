def boolean(a):
    if str(a) in ['true','True','1','TRUE']:
        return 1
    elif str(a) in ['false','False','0','FALSE']:
        return (str(a) + 2)
    else:
        return '''THE ARGUMENT FOR'PART' IS NOT OF TYPE BOOLEAN. PLEASE RECHECK!''' 

def datasetpartition(part,n=0.2,k=10):
    import pandas as pd
    from sklearn.model_selection import train_test_split as tts
    from sklearn.model_selection import KFold
    import os
    from pathlib import Path
    
   #Now search for the dataset and read the x_values in X and y_values in Y 
    if os.path.exists("cleveland.csv"):
        print('dataset_found')
    else:
        print('dataset not found. Now changing cwd to search for it. will return back here if found in datasets folder')
        p = Path(os.getcwd())
        os.chdir(str(p.parent) + '\datasets')
        df=pd.read_csv("cleveland.csv")
        X = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values
    
    #Now as per the input arguments, split the dataset
    try: #executes only when part is not set as one of ['false','False','0','FALSE']
        temp= boolean(part)
        if temp ==1:
            kf = KFold(n_splits=k, shuffle=True, random_state=0)
            for train_index, test_index in kf.split(X):
                X_train, X_test = X[train_index], X[test_index]
                y_train, y_test = y[train_index], y[test_index]
            print('NOW IMPLEMENTING {}- FOLD'.format(k))
            return X_train, X_test, y_train, y_test
        else:
            print(temp) #tells the user that the type of input for argument 'part' is invalid
 
    except: #executes only when the argument, 'part' is set as one of ['false','False','0','FALSE']
        X_train, X_test, y_train, y_test = tts(X,y,test_size=n,random_state=0)
        p = Path(os.getcwd())
        os.chdir(str(p.parent) + '\MDL1-MLP-PPR#1')
        print('NOW PARTITIONING THE DATASET USING n=', n)
        return pd.DataFrame(X_train), pd.DataFrame(X_test),pd.DataFrame(y_train),pd.DataFrame(y_test)






