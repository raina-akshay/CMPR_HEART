def convert_data(): #searches for data, convertes it if not in csv format and then returns a DF
    import os
    from pathlib import Path
    import pandas as pd
    if os.path.exists("statlog.csv"):
        print('dataset found in current directory')
        return pd.read_csv('statlog.csv')
    else:
        print('dataset not found. Now changing cwd to search for it. will return back here if found in datasets folder')
        p = Path(os.getcwd())
        os.chdir(str(p.parent) + '\datasets')
        if os.path.exists("statlog.csv"):
            print('dataset found in /datasets sub- directory')
            return pd.read_csv('statlog.csv')
        elif os.path.exists('statlog.dat'):
            import csv
            data_fldr = os.getcwd()
            new_file = 'statlog.csv'
            DATASET_FINAL_FILE_PATH = os.path.join(data_fldr, new_file)
            with open('statlog.dat', 'r') as f:
                data = f.readlines()
            #Change the delimeter from ' ' to ','
            for i, r in enumerate(data):
                data[i] = data[i].replace(' ', ',')
            #Make more clear
            new_data = []
            for i, r in enumerate(data):
                row = data[i].split(',')
                row[-1] = row[-1][0]
                new_data.append(row)
            #writing into the csv file
            with open(DATASET_FINAL_FILE_PATH, 'w', newline='') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerow(['age', 'sex', 'cp', 'trestbps', 
                                 'chol', 'fbs', 'restecg', 
                                 'thalach', 'exang', 'oldpeak', 
                                 'slope', 'ca', 'thal', 'presence'])
                for r in new_data:
                    writer.writerow(r)
            return pd.read_csv('statlog.csv')
        else:
            print('There is no file corresponding to the Statlog dataset, be it in .csv or .dat format')
        p = Path(os.getcwd())
        os.chdir(str(p.parent) + '\MDL2-HDPM-PPR#2')
        
def fs():
    from sklearn.feature_selection import mutual_info_classif as mic
    import matplotlib.pyplot as plt
    import pandas as pd
    data=convert_data(); X=data.iloc[:,0:13]; y=data.iloc[:,13]
    imp=mic(X,y)
    feat_imp=pd.Series(imp)
    feat_imp.plot(kind='barh',color='teal')
    plt.show()
    return data

fs()
#in case of ':' indexing, second digit isnt included...but in case of it as single number, it is the number it is, i.e. if the number is 'n' u get the col no. 'n+1'
    
