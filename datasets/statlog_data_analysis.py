import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

df=pd.read_csv('statlog.csv')

#Check for any missing values in the dataset
df.isnull().sum()

#sort dataframe rows wrt the feature: age
sort_by_age=df.sort_values(by=['age'])
#Plot1(Age Vs Cholestrol)
plt.plot(sort_by_age['age'],sort_by_age['chol'], 'g:',linewidth=1, markersize=10)
plt.xlabel('Age');  plt.ylabel('Cholestrol')

# Plot2(distribution of presence vs age)
sb.set_context(context="paper", font_scale = 2, rc = {"font.size": 20,"axes.titlesize": 25,"axes.labelsize": 20}) 
sb.catplot(kind = 'count', data = df, x = 'age', hue = 'presence', order = df['age'].sort_values().unique())
plt.title('Variation of Age for each presence class')
plt.show()

# Plot3(barplot of age vs sex with hue = presence)
sb.catplot(kind = 'bar', data = df, y = 'age', x = 'sex', hue = 'presence')
plt.title('Distribution of age vs sex with the presence class')
plt.show()
# df['sex'] = df.sex.map({'female': 0, 'male': 1})

#ANALYSING VARIOUS STATISTICAL MEASURES OF FEATURES AND INTRA- FEATURES; [Mean, Std, Min, Max etc.]
pd.set_option("display.float", "{:.2f}".format)
dfx = df.drop(columns=["sex","presence"])
dfx.describe()

#Plot4(No. of people with heart disease vs No. of people without heart disease)
df.presence.value_counts().plot(kind="bar",width=0.1,color=["lightgreen","salmon"],legend=1,figsize=(8,5))
plt.ylabel("No. of People", fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(["No. of people without heart disease"],fontsize=12);
plt.show()

#Plot5(Correlation Matirx Heatmap)
corr_matrix = df.corr()
mask = np.zeros_like(corr_matrix, dtype = np.bool)
mask[np.triu_indices_from(corr_matrix)] = True
fig, ax = plt.subplots(figsize=(22, 10))
ax = sb.heatmap(corr_matrix,mask=mask,annot=True,linewidths=0.5,fmt=".2f",cmap="YlGn");
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5);

#Plot6(Correlation with presence)
plt.figure(figsize=(20,12))
df.drop('presence', axis=1).corrwith(df.presence).plot(kind='bar', grid=True, title="Correlation with presence",color="lightgreen");

#Plot7(Categorical and Continous Values)
categorical_val = []
continous_val = []
for column in df.columns:
    print('-------------------------------')
    print(f"{column} : {df[column].unique()}")
    if len(df[column].unique()) <= 10:
        categorical_val.append(column)
    else:
        continous_val.append(column)
        
#Plot8(Categorical Values Histogram)  
plt.figure(figsize=(20, 16))
for i, column in enumerate(categorical_val, 1):
    plt.subplot(3, 3, i)
    df[df["presence"] == 2][column].hist(bins=35, color='red', label='People with heart disease',alpha=0.8)
    df[df["presence"] == 1][column].hist(bins=35, color='green', label='People without heart disease',alpha=0.5)
    plt.legend(fontsize=12)
    plt.xlabel(column)
    plt.ylabel("No. of People")
   
#Plot9(Continous Values Histogram); Alternate of Plot2
plt.figure(figsize=(20, 16))
for i, column in enumerate(continous_val, 1):
    plt.subplot(3, 2, i)
    df[df["presence"] == 2][column].hist(bins=35, color='red', label='People with heart disease', alpha=0.8)
    df[df["presence"] == 1][column].hist(bins=35, color='green', label='People without heart disease',alpha=0.5)
    plt.legend(fontsize=12)
    plt.xlabel(column)
    plt.ylabel("No. of People")

#Plot10(Scatter Plot(Age Vs Max Heart Rate))
plt.figure(figsize=(15, 10))
plt.scatter(df.age[df.presence==2],df.thalach[df.presence==2],c="red",s=75)
plt.scatter(df.age[df.presence==1],df.thalach[df.presence==1],c="green",alpha=0.5)
plt.title("Heart Disease in function of Age and Max Heart Rate",fontsize=14)
plt.xlabel("Age", fontsize=14)
plt.ylabel("Max Heart Rate", fontsize=14)
plt.legend(["Disease", "No Disease"],fontsize=18);

#Plot11(Scatter Plot(Age Vs Serum Cholestoral(mg/dl))); Alternate to Plot1
plt.figure(figsize=(15, 10))
plt.scatter(df.age[df.presence==2],df.chol[df.presence==2],c="red",s=75)
plt.scatter(df.age[df.presence==1],df.chol[df.presence==1],c="green",alpha=0.5)
plt.title("Heart Disease in function of Age and Serum Cholestoral(mg/dl)",fontsize=14)
plt.xlabel("Age", fontsize=14)
plt.ylabel("Serum Cholestoral(mg/dl)", fontsize=14)
plt.legend(["Disease", "No Disease"],fontsize=18);

#Plot12(Scatter Plot(Age Vs Resting Blood Pressure))
plt.figure(figsize=(15, 10))
plt.scatter(df.age[df.presence==2],df.trestbps[df.presence==2],c="red",s=75)
plt.scatter(df.age[df.presence==1],df.trestbps[df.presence==1],c="green",alpha=0.5)
plt.title("Heart Disease in function of Age and Resting Blood Pressure",fontsize=14)
plt.xlabel("Age", fontsize=14)
plt.ylabel("Resting Blood Pressure", fontsize=14)
plt.legend(["Disease", "No Disease"],fontsize=18);
