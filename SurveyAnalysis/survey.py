import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('D:\Samip\VS\Python\SurveyAnalysis\survey_results_public.csv')
df.head()
df.shape
df['BetterLife'].value_counts(normalize=True)
df['MgrMoney'].value_counts(normalize=True)

df['SocialMedia'].value_counts().plot(kind="bar", figsize=(15,7), color="#61d199")
plt.xlabel('SocialMedia')
plt.ylabel('Count')
plt.title('Social Media Counts')
plt.show() 
said_no = df[df['BetterLife'] == 'No']
said_no.head(3)
said_no.shape
said_no['BetterLife'].value_counts()

said_yes=df[df['BetterLife']=='Yes']
said_yes.head()
said_yes.shape
said_yes['BetterLife'].value_counts()

print(said_no['Age'].mean(), 
      said_yes['Age'].mean(),
      said_no['Age'].median(),
      said_yes['Age'].median()
     )

over_50=df[df['Age']>=50]
under_25=df[df['Age']<=25]
print(over_50['BetterLife'].value_counts(normalize=True))
print(under_25['BetterLife'].value_counts(normalize=True))
print(len(over_50))
print(len(under_25))



filtered_1 = df[(df['BetterLife'] == 'Yes') & (df['Country'] == 'India')]
print(filtered_1['BetterLife'].value_counts())
print(filtered_1['Country'].value_counts())

filtered=df[(df['BetterLife']=='Yes') & (df['Age']>50) & (df['Country']=='India') &~ (df['Hobbyist'] =='Yes')  &~ (df['OpenSourcer'] == "Never")]
filtered

df['LanguageWorkedWith'].head()
uses_python=df['LanguageWorkedWith'].str.contains('Python')
uses_python.value_counts(normalize=True)

lang_list=df['LanguageWorkedWith'].str.split(';',expand=True)
lang_df=lang_list.stack().value_counts()
lang_df.plot(kind='bar', figsize=(15,7), color="#61d199")
plt.show()