def datasetpartition(part=0,n=0.2,k=0):
    import pandas as pd
    from sklearn.model_selection import train_test_split as tts
    import os
    from pathlib import Path
    try:
        n
        if os.path.exists("cleveland.csv"):
            print('dataset_found')
        else:
            print('dataset not found. Now changing cwd to search for it. will return back here if found in datasets folder')
            p = Path(os.getcwd())
            os.chdir(str(p.parent) + '\datasets')
        df=pd.read_csv("cleveland.csv")
        X = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values
        X_train, X_test, y_train, y_test = tts(X,y,test_size=n,random_state=0)
        p = Path(os.getcwd())
        os.chdir(str(p.parent) + '\MDL1-MLP-PPR#1')
        print('remember that i always give first precedence to partitioning in ratios,i.e. using n')
        return pd.DataFrame(X_train), pd.DataFrame(X_test),pd.DataFrame(y_train),pd.DataFrame(y_test)
    except:
        if bool(part)==0:
            print('YOU DID NOT MENTION THE PARTITIONING RATIO AND ASKED ME TO NOT USE K- FOLD CV. PLEASE RECONSIDER YOUR CHOICES')
        elif bool(part)==1: 
            print('edit the k- fold validation expressions here')
        else:
            print("PLEASE RECHEK YOUR INPUT ARGUMENTS. I COULD NOT GET THEM!")
    