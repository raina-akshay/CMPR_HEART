def datasetpartition():
    import pandas as pd
    from sklearn.model_selection import train_test_split as tts
    import os
    from pathlib import Path
    if os.path.exists("cleveland.csv"):
        print('dataset_found')
    else:
        print('dataset not found. Now changing cwd to search for it. will return back here if found in datasets folder')
        p = Path(os.getcwd())
        os.chdir(str(p.parent) + '\datasets')
    df=pd.read_csv("cleveland.csv")
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    X_train, X_test, y_train, y_test = tts(X,y,test_size=0.15,random_state=0)
    p = Path(os.getcwd())
    os.chdir(str(p.parent) + '\MDL1-MLP-PPR#1')
    return X_train, X_test, y_train, y_test
    
datasetpartition()
# print(X_train)