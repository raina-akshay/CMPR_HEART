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
    mut_info=pd.Series(imp); mut_info.index=X.columns; mut_info.sort_values(ascending=False)
    # mut_info.plot(kind='barh',color='teal')
    # plt.show()
    mut_info.sort_values(ascending=False).plot.bar(figsize=(20, 8))
    mut_info.plot(kind='barh',color='teal')
    plt.show()
    return data, mut_info

data, info=fs()
#in case of ':' indexing, second digit isnt included...but in case of it as single number, it is the number it is, i.e. if the number is 'n' u get the col no. 'n+1'

#DBSCAN
X=data[['age','thalach']].iloc[:,:].values
from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=8,min_samples=5,)
model = dbscan.fit(X)
labels=model.labels_
#identifying the points which makes up our core points
import numpy as np
sample_cores=np.zeros_like(labels,dtype=bool)
sample_cores[dbscan.core_sample_indices_]=True
#Calculating the number of clusters
n_clusters=len(set(labels))- (1 if -1 in labels else 0)
#Scatter plot for visualizing outliers
import matplotlib.pyplot as plt
plt.figure(figsize=(15, 10))
plt.scatter(data.age,data.thalach,c=labels,s=75)
plt.title("Outlier detection using Age and Max Heart Rate",fontsize=14)
plt.xlabel("Age", fontsize=14)
plt.ylabel("Max Heart Rate", fontsize=14)
#Remove Outlier
x=np.where(labels==-1)
for i in list(x[0]):
    data = data.drop(data.index[i])

#split
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
print(y)
print(X)
#SMOTE-ENN
from collections import Counter
from imblearn.combine import SMOTEENN
print('Original dataset shape %s' % Counter(y))
resample = SMOTEENN(sampling_strategy="minority")
X_res, y_res = resample.fit_resample(X, y)
print('Resampled dataset shape %s' % Counter(y_res))