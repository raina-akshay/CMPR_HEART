import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df=pd.read_csv('cleveland.csv')

#Check for any missing values in the dataset
df.isnull().sum()

#sort dataframe rows wrt the feature: age
sort_by_age=df.sort_values(by=['age'])
#plot the age vs cholestrol
plt.plot(sort_by_age['age'],sort_by_age['chol'], 'g:',linewidth=1, markersize=10)
plt.xlabel('Age');  plt.ylabel('Cholestrol')

# distribution of target vs age 
sb.set_context(context="paper", font_scale = 2, rc = {"font.size": 20,"axes.titlesize": 25,"axes.labelsize": 20}) 
sb.catplot(kind = 'count', data = df, x = 'age', hue = 'target', order = df['age'].sort_values().unique())
plt.title('Variation of Age for each target class')
plt.show()

# barplot of age vs sex with hue = target
sb.catplot(kind = 'bar', data = df, y = 'age', x = 'sex', hue = 'target')
plt.title('Distribution of age vs sex with the target class')
plt.show()
df['sex'] = df.sex.map({'female': 0, 'male': 1})

#desc=data.describe()
#desc
#ANALYSING VARIOUS STATISTICAL MEASURES OF FEATURES AND INTRA- FEATURES
#measures = pd.DataFrame(columns=['Mean','Variance','Std.Deviation'])
#measures



