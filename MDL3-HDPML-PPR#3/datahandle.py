import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split as split

class handle_data:
    def __init__(self,filename='cleveland',col_names=None):
        self.data = filename + '.csv'
        self.df = None
        self.status=None
        if col_names is None:
            self.col_names=['age', 'sex', 'cp', 'trestbps', 
                             'chol', 'fbs', 'restecg', 
                             'thalach', 'exang', 'oldpeak', 
                             'slope', 'ca', 'thal', 'presence']
        else:
            self.col_names=col_names
    
    def dat_to_csv(self):
        import os
        if not (os.path.exists(self.data) or os.path.exists('../'+self.data) or os.path.exists('../datasets/'+self.data)):     
            try:
                import csv
                file=self.data[0:-4]+'.dat'
                new_file = self.data
                DATASET_FINAL_FILE_PATH = '../datasets/' + new_file
                with open(file, 'r') as f:
                    dat = f.readlines()
                #Change the delimeter from ' ' to ','
                for i, r in enumerate(dat):
                    dat[i] = dat[i].replace(' ', ',')
                
                #Make more clear
                new_data = []
                for i, r in enumerate(dat):
                    row = dat[i].split(',')
                    row[-1] = row[-1][0]
                    new_data.append(row)
                #writing into the csv file
                with open(DATASET_FINAL_FILE_PATH, 'w', newline='') as writeFile:
                    writer = csv.writer(writeFile)
                    writer.writerow(self.col_names)
                    for r in new_data:
                        writer.writerow(r)
            except:
                print('Please check if at least the data in .dat exists, is not corrupt, and has the right structure!')
        else:
            pass
    def read_data(self):
            # import pandas as pd
            self.dat_to_csv()
            try:
                self.df=pd.read_csv(self.data)
                self.sttus='The dataset {} was found in current directory'.format(self.data)
            except FileNotFoundError:
                try:
                    self.df=pd.read_csv('../'+ self.data)
                    self.status='The dataset {} was found in previous directory'.format(self.data)
                except:
                    pass
            finally:
                if self.df is None:
                    try:
                        self.df=pd.read_csv('../datasets/' + self.data)
                        self.status='The dataset {} was found in ../datasets/ directory'.format(self.data)
                    except:
                        self.status='The dataset {} was not found in any directory in either in .csv or .dat format'.format(self.data)
    def partition(self):
        X = self.df.iloc[:, :-1].values
        y = self.df.iloc[:, -1].values
        X = StandardScaler().fit_transform(X)
        X_train, X_test, y_train, y_test = split(X, y, test_size=0.20)
        return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    dat=handle_data('cleveland')
    dat.read_data()
    X_train, X_test,y_train, y_test=dat.partition()