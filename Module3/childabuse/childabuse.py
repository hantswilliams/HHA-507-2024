import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

### child abuse data

### loading way 1 ## based off of the API 
# df = pd.read_csv('https://healthdata.gov/resource/ej22-ej5b.csv?$limit=6000')

### loading way 2 ## local file 
df = pd.read_csv('./Module3/childabuse/childabusedata.csv')

#### describing the data model 
df.shape
len(df)
df.columns

### question? shouldnt there only be 200 rows based on 
### assumption of 4 rows per state and 50 states

df['State'].value_counts()
df['Year'].value_counts()
df['Table'].value_counts()


national = df[df['State'] == 'National']
national.head()

child_age = df[df['Table'] == 'Child Victims by Age']
child_age['Characteristic Label'].value_counts()
child_age['Measure'].value_counts()
child_age.columns
child_age.head()

child_age_count = child_age[child_age['Measure'] == 'Victims (unique count) by age']
child_age_count_5 = child_age_count[child_age_count['Characteristic Label'] == 'Age 5']
child_age_count_5 = child_age_count_5[child_age_count_5['State'] != 'National']

child_age_count_5['Value'].describe()

## plot value counts
plt.figure(figsize=(10, 6))
sns.histplot(child_age_count_5['Value'], bins=3, kde=True)
plt.title('Distribution of Child Abuse Victims (Age 5)')
plt.xlabel('Number of Victims')
plt.ylabel('Frequency')
plt.show()


