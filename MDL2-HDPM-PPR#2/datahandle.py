def convert_data():
    import os
    from pathlib import Path
    
    if os.path.exists("statlog.csv"):
        print('dataset found')
    else:
        print('dataset not found. Now changing cwd to search for it. will return back here if found in datasets folder')
        p = Path(os.getcwd())
        os.chdir(str(p.parent) + '\datasets')
        if os.path.exists("statlog.csv"):
            print('dataset found')
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
                writer.writerow(['age', 'sex', 'chest_pain', 'blood_press', 
                                 'serum_chol', 'blood_sugar', 'electrocard', 
                                 'max_heart_rate', 'induced_ang', 'oldpeak', 
                                 'peak_st_seg', 'major_ves', 'thal', 'presence'])
                for r in new_data:
                    writer.writerow(r)
        else:
            print('There is no file corresponding to the Statlog dataset, be it in .csv or .dat format')
        p = Path(os.getcwd())
        os.chdir(str(p.parent) + '\MDL2-HDPM-PPR#2')